'''
Program ini dibuat untuk melakukan automatisasi langkah-langkah pemrosesan data menggunakan Airflow. Semua proses dilakukan dengan pipeline dan menggunakan konfigurasi melalui Docker. 
Langkah pemrosesan data ini dilakukan dengan Fungsi Directed Acyclic Graphs (DAGs) yang dijalankan melalui PythonOperator, dengan langkah pertama dalam pipeline ini adalah mengambil data dari database PostgreSQL.
Setelah proses pengambilan/fetch data, selanjutnya adalah pembersihan data, kemudian dimasukkan ke Elasticsearch untuk memfasilitasi eksplorasi data dan analisis visualisasi data. 
Tujuan utama program ini adalah memanfaatkan Airflow melalui konfigurasi environment Docker dalam mengatur pipeline yang mengintegrasikan data dari PostgreSQL ke dalam format data yang siap divisualisasikan menggunakan Kibana.

'''

# Instalasi libraries
from datetime import datetime, timedelta
import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
from sqlalchemy import create_engine
from elasticsearch import Elasticsearch

# Fungsi Pengambilan data dari PostgreSQL pada Docker container
def fetch_data_from_postgresql():
    def get_data_from_postgresql(username, password, host, port, database_name, table_name):
        # Fungsi automatisasi pengambilan data dari PostgreSQL
        database_url = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'
        engine = create_engine(database_url)
        # Membuat query untuk mengambil data dari database dan ditransform ke dalam DataFrame
        data = pd.read_sql(f"SELECT * FROM {table_name}", engine)
        return data
    # Penggunaan Fungsi Pengambilan data dari PostgreSQL pada Docker container 
    data = get_data_from_postgresql('airflow', 'airflow', 'postgres', '5432', 'db_phase2', 'table_m3')
    # Menyimpan hasil pengambilan data ke dalam direktori yang sesuai dengan konfigurasi Docker container
    data.to_csv('/opt/airflow/data/tmp_data.csv', index=False)

# Fungsi Data Cleaning 
def clean_and_save_data(**kwargs):
    data = pd.read_csv('/opt/airflow/data/tmp_data.csv')
    data.drop_duplicates(inplace=True)
    data.totalcharges = pd.to_numeric(data.totalcharges, errors='coerce')
    data[['onlinesecurity','onlinebackup','deviceprotection','techsupport','streamtv','streamingmovies']]= data[['onlinesecurity','onlinebackup','deviceprotection','techsupport','streamtv','streamingmovies']].replace('No internet service','No')
    data['multiplelines']= data['multiplelines'].replace('No phone service','No')
    data['seniorcitizen'].replace({0: 'No', 1: 'Yes'}, inplace=True)
    data.rename(columns={
        'customerid': 'customer_id', 'seniorcitizen': 'senior_citizen', 'phoneservice': 'phone_service', 'multiplelines': 'multiple_lines',
        'internetservice': 'internet_service', 'onlinesecurity': 'online_security', 'onlinebackup': 'online_backup', 'deviceprotection': 'device_protection',
        'techsupport': 'tech_support', 'streamtv': 'streaming_tv', 'streamingmovies': 'streaming_movies', 'paperlessbilling': 'paperless_billing',
        'paymentmethod': 'payment_method', 'monthlycharges': 'monthly_charges', 'totalcharges': 'total_charges'
            }, inplace=True)
    data['total_charges'].fillna(data['total_charges'].median(),inplace=True)
    # Menyimpan Hasil Data Cleaning ke file CSV
    data.to_csv('/opt/airflow/data/P2M3_firhan_data_clean.csv', index=False)

# Mendefinisikan Fungsi koneksi file csv ke index Elasticsearch
def index_to_elasticsearch():
    # Menggunakan IP Address Docker Host:
    es = Elasticsearch(hosts=["host.docker.internal:9200"])

    csv_path = '/opt/airflow/data/P2M3_firhan_data_clean.csv'
    es_index = 'p2m3_firhan_data_clean'

    def index_csv_to_elasticsearch(es_instance, csv_path, es_index):
        """
        Menghubungkan file csv ke index Elasticsearch
        Parameters:
        es_instance: Membuat koneksi Elasticsearch
        csv_path: direktori file csv
        es_index: Nama index Elasticsearch
        """
        df = pd.read_csv(csv_path)
        for _, r in df.iterrows():
            doc = r.to_json()
            res = es_instance.index(index=es_index, doc_type="doc", body=doc)
    
    # Penggunaan Fungsi transfer file csv ke index Elasticsearch 
    index_csv_to_elasticsearch(es, csv_path, es_index)

# Konfigurasi Airflow DAG 
default_args = {
    'owner': 'firhan',
    'depends_on_past': False,
    'retries': 1, # Jika ada proses yang gagal, sistem akan mencoba mengulanginya 1 kali  
    'retry_delay': timedelta(minutes=5), # penundaan selama 5 menit apabila terdapat kagagalan proses
    'start_date': dt.datetime(2023, 10, 1, 16, 20, 0) - dt.timedelta(hours=7) # Tanggal mulai untuk DAG ini ditetapkan menyesuaikan Timezone
}

dag = DAG(
    'milestone3_data_to_kibana',
    default_args=default_args,
    description='Pipeline untuk mengambil data dari PostgreSQL, cleaning, dan membuat indeks ke Elasticsearch',
    schedule_interval=timedelta(minutes=15), # Konfigurasi Waktu Pemrosesan Pipeline secara repetitif per 15 menit
    catchup=False
)

# Membuat konfigurasi task pada pipeline
t1 = PythonOperator(
    task_id='fetch_postgresql',
    python_callable=fetch_data_from_postgresql,
    dag=dag
)

t2 = PythonOperator(
    task_id='data_cleaning',
    python_callable=clean_and_save_data,
    dag=dag
)

t3 = PythonOperator(
    task_id='post_to_kibana',
    python_callable=index_to_elasticsearch,
    dag=dag
)

# Membuat konfigurasi urutan task pada pipeline
t1 >> t2 >> t3
