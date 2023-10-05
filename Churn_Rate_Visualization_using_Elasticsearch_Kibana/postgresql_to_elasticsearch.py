'''
=================================================
Program ini dibuat untuk melakukan automatisasi pngambilan data dari PostgreSQL dan menghubungkan file csv ke index Elasticsearch.
Dataset yang digunakan adalah dataset pada Website Kaggle, bagian dari dataset bernama *Telco Customer Churn* yang didalamnya 
tersedia informasi tentang data transaksi dan profil customer dari suatu perusahaan telekomunikasi.
=================================================
'''

# Import Libararies
import pandas as pd
from sqlalchemy import create_engine
from elasticsearch import Elasticsearch


# Mendefinisikan Fungsi automatisasi pngambilan data dari PostgreSQL
def get_data_from_postgresql(username, password, host, port, database_name, table_name):
    # Fungsi ini untuk mengambil data dari PostgreSQL
    
    # Membuat koneksi ke database PostgreSQL 
    database_url = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'
    engine = create_engine(database_url)

    # Membuat query untuk mengambil data dari database dan ditrasform ke dalam DataFrame
    data = pd.read_sql(f"SELECT * FROM {table_name}", engine)
    
    return data


# Penggunaan Fungsi Pengambilan data dari PostgreSQL 
data = get_data_from_postgresql('postgres', '101094', 'localhost', '5432', 'db_phase2', 'table_gc7')

# Menghapus Data Duplikat
data.drop_duplicates(inplace=True)

# Menyesuaikan nilai data dan format data yang tidak sinkron
data.totalcharges = pd.to_numeric(data.totalcharges, errors='coerce')
data[['onlinesecurity','onlinebackup','deviceprotection','techsupport','streamtv','streamingmovies']]= data[['onlinesecurity','onlinebackup','deviceprotection','techsupport','streamtv','streamingmovies']].replace('No internet service','No')
data['multiplelines']= data['multiplelines'].replace('No phone service','No')
data['seniorcitizen'].replace({0: 'No', 1: 'Yes'}, inplace=True)

# Menyesuaikan Nama Kolom
data.rename(columns={
    'customerid': 'customer_id', 'seniorcitizen': 'senior_citizen', 'phoneservice': 'phone_service', 'multiplelines': 'multiple_lines',
    'internetservice': 'internet_service', 'onlinesecurity': 'online_security', 'onlinebackup': 'online_backup', 'deviceprotection': 'device_protection',
    'techsupport': 'tech_support', 'streamtv': 'streaming_tv', 'streamingmovies': 'streaming_movies', 'paperlessbilling': 'paperless_billing',
    'paymentmethod': 'payment_method', 'monthlycharges': 'monthly_charges', 'totalcharges': 'total_charges'
}, inplace=True)

# Handling Missing Values
data['total_charges'].fillna(data['total_charges'].median(),inplace=True)

# Menyimpan data clean ke file CSV
data.to_csv('P2G7_firhan_data_clean.csv', index=False)


# Mendefinisikan Fungsi koneksi file csv ke index Elasticsearch.
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

# Penggunaan Fungsi memasukkan file csv ke index Elasticsearch 
es = Elasticsearch()
index_csv_to_elasticsearch(es, 'P2G7_firhan_data_clean.csv', 'p2g7_firhan_data_clean')
