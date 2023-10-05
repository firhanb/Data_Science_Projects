import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Prediksi Untuk Mengevaluasi "Churn Rate"')

    # Membuat Sub Header
    st.subheader('Analisis Dataset Telco Customer Churn (Kaggle)')

    # Menambahkan Gambar
    image = Image.open('churn.jpg')
    st.image(image, caption = 'churn_customer')

    # Menambahkan Deskripsi
    st.write('Analisis ini bertujuan untuk memprediksi secara akurat kelompok pelanggan (Customer) yang berhenti berlangganan atau tidak lagi membeli produk dari suatu perusahaan. Analisis ini akan membantu dalam memahami konsep Churn rate, yaitu salah satu indikator apakah bisnis berjalan dengan baik. Churn rate adalah metrik yang menggambarkan jumlah pelanggan yang membatalkan atau tidak memperbarui langganan mereka dengan perusahaan. Jadi, semakin tinggi tingkat churn, semakin banyak pelanggan yang berhenti membeli dari bisnis Anda, yang secara langsung memengaruhi pendapatan dari bisnis yamg akan diterima. Berdasarkan hal ini, membangun model prediktif terkait analisis churn menjadi sumber referensi yang penting bagi keberlangsungan suatu bisnis.')

    st.write('Dataset yang digunakan adalah data yang tersedia pada Website Kaggle, komunitas data Online, bagian dari dataset bernama *Telco Customer Churn*. Data ini diperoleh dengan lisensi dari website kaggle dengan link sebagai berikut: https://www.kaggle.com/datasets/blastchar/telco-customer-churn?datasetId=13996&sortBy=voteCount')

    # Meload DataFrame
    df = pd.read_csv('data_cleaned.csv')

    st.title('Why is analyzing customer churn important?')

    st.write('Churn rate adalah persentase banyaknya jumlah customer yang berhenti berlangganan atau tidak lagi membeli produk. Menghitung churn rate sangat penting karena bisa menjadi tolok ukur apakah suatu bisnis mampu mempertahankan pelanggan dengan baik. Terutama, untuk jenis bisnis yang menjual produk dengan sistem berlangganan. Dengan model bisnis tersebut, pendapatan bisnis berasal dari setiap customer yang melakukan pembelian berulang. Jika customer berhenti membeli, di sanalah terjadi churn yang membahayakan bisnis. Churn rate seoptimal mungkin perlu dievaluasi secara berkala, misalnya setiap minggu, bulan, atau tahun. Tujuannya, untuk mengevaluasi keadaan bisnis secara lebih tepat. Ini adalah metrik yang penting, terutama dalam industri dimana akuisisi pelanggan bersifat kompetitif dan mahal.')

    st.write('### Pentingnya Churn Rate:')

    st.write('**1.Revenue Implications:** Tingkat churn yang tinggi dapat menyebabkan hilangnya pendapatan secara signifikan. Khususnya dalam industri berbasis langganan (seperti telekomunikasi), basis pelanggan yang stabil atau berkembang sering kali penting untuk mendapatkan keuntungan.')

    st.write('**2.Customer Acquisition Cost (CAC):** Mendapatkan pelanggan baru umumnya lebih mahal daripada mempertahankan pelanggan yang sudah ada. Jika sebuah bisnis kehilangan pelanggan yang sudah ada (churn yang tinggi) dan menghabiskan banyak uang untuk mendapatkan pelanggan baru, hal ini dapat dengan cepat mengikis keuntungan.')

    st.write('**3.Market Feedback:** Meningkatnya Churn Rate dapat menandakan ketidakpuasan pelanggan. Hal ini mungkin disebabkan oleh masalah produk, penawaran produk kompetitor yang lebih baik, atau perubahan kebutuhan pasar.')

    st.write('### Analisis Kasus Pada Perusahaan Telekomunikasi:')

    st.write('Perusahaan telekomunikasi sering kali beroperasi di lingkungan yang sangat kompetitif, sehingga retensi pelanggan menjadi hal yang penting. Inilah mengapa analisis prediktif, khususnya terkait churn, sangat penting. Model prediktif dapat mengidentifikasi pelanggan yang kemungkinan besar akan berhenti berlangganan dalam waktu dekat, sehingga memungkinkan perusahaan mengambil tindakan proaktif, seperti penawaran khusus atau komunikasi yang ditargetkan, untuk mempertahankan mereka. Dengan menganalisis perilaku dan umpan balik pelanggan, perusahaan dapat mengidentifikasi alasan untuk churn dan mengatasi masalah mendasar. Mungkin kelompok demografis tertentu merasa kurang terlayani, atau wilayah tertentu mengalami gangguan layanan. Daripada membelanjakan uang secara seragam untuk semua pelanggan, perusahaan telekomunikasi dapat mengalokasikan sumber daya secara lebih efisien, dengan fokus pada segmen berisiko tinggi atau pelanggan bernilai tinggi yang didapat dari hasil analisis prediksi. Dengan memahami perilaku pelanggan, perusahaan telekomunikasi dapat menawarkan paket atau paket yang dipersonalisasi, meningkatkan kepuasan dan mengurangi keinginan pelanggan untuk beralih ke pesaing.')

    st.title('Eksplorasi Data Analysis (EDA):')

    st.write('#### Contoh Analisis Data Perusahaan Telekomunikasi: (*Sumber Data: Kaggle Dataset*)')

    # Menampilkan Visualisasi Presentase Churn
    def plot_presentase_churn():
        churn_counts = df['Churn'].value_counts()
        churn_counts.index = ['Not-Churn Customer' if x == 'No' else 'Churn Customer' for x in churn_counts.index]
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
        text_properties = {'fontsize': 15, 'fontweight':'bold'} 
        axes[0].pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', 'r'], textprops=text_properties)
        axes[0].set_title("Presentase Customer Churn", fontweight='bold', fontsize=16)
        sns.countplot(data=df, x='Churn', ax=axes[1], palette=['#4CAF50', 'r'])
        axes[1].set_title("Perbandingan Jumlah Customer Churn Vs. Non-Churn", fontsize=16, fontweight='bold')
        axes[1].set_xlabel("Customer Type")
        axes[1].set_ylabel("Jumlah Customer")
        axes[1].set_xticklabels(['Not-Churn Customer', 'Churn Customer'])
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_presentase_churn()

    st.write('*Contoh Dataset ini adalah terkait data transaksi dan profil customer dari suatu perusahaan telekomunikasi berdomisili di Amerika Serikat.*')
    st.write('--> Terlihat mayoritas pada data ini adalah customer yang berstatus Non-churn, sehingga dalam konteks analisis ini, variabel target yang akan diprediksi tergolong tidak seimbang (imbalanced data).')
    st.write('--> Sekitar 26% customer dari data ini merupakan Churn Customers atau memilih untuk berhenti menjadi pelanggan, sehingga perusahaan kehilangan seperempat dari pendapatannya yang diperoleh dari customer tersebut.')
    st.write('--> Dilihat dari jumlahnya, sekitar 1800 customer yang churn. Sedangkan jika dievaluasi dari presentase-nya, angka 26% termasuk kategori tinggi, yang mengindikasikan adanya cukup banyak pelanggan yang merasa tidak puas dengan produk atau layanan yang disediakan perusahaan saat ini.')

    # Visualisasi Perbandingan Churn dengan Profil Customer
    def plot_churn_profile():
        text_properties = {'fontsize': 15, 'fontweight':'bold'} 
        colors_palette = ['#FF0000', '#FF8361']
        def plot_pie_for_column(column_name, ax, labels_map=None):
            grouped = df.groupby([column_name, 'Churn']).size().unstack().fillna(0)
            ax.pie(grouped['Yes'], labels=grouped.index, autopct='%1.1f%%', startangle=90, colors=colors_palette[:len(grouped)], textprops=text_properties)
            ax.set_title(f"%Churn dari Status {column_name}", fontweight='bold', fontsize=18)
        fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20, 5))
        plot_pie_for_column('gender', axes[0])
        plot_pie_for_column('SeniorCitizen', axes[1])
        plot_pie_for_column('Partner', axes[2])
        plot_pie_for_column('Dependents', axes[3])
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_churn_profile()

    st.write('Dilihat perbandingan berdasarkan gender, antara Customer/pelanggan pria dan wanita hampir sama atau sebanding terkait jumlah customer yang berhenti menjadi pelanggan perusahaan. Mayoritas customer adalah pelanggan yang tergolong usia muda yang berhenti menjadi pelanggam. Hanya sekitar 25% dari seluruh pelanggan yang tergolong lanjut usia yang memutuskan untuk berhenti menjadi pelanggan, namun angka ini juga menunjukkan chrurn rate yang cukup tinggi pada customer lanjut usia. Berdasarkan status Partner, terlihat lebih banyak pelanggan yang berstatus belum menikah yang memilih untuk berhenti menjadi pelanggan, sedangkan 36% dari customer yang memutuskan untuk berhenti menjadi pelanggan adalah customer yang sudah menikah. Jika dilihat dari jumlah tanggungannya (Dependents), hanya sekitar 17% dari total customer yang meninggalkan perusahaan adalah pelanggan yang memiliki tanggungan atau anak, sedangkan mayoritas pelanggan yang keluar adalah yang belum memiliki tanggungan sama sekali.')
    st.write('')

    # Visualisasi Perbandingan Jumlah Pelanggan Perusahaan
    def plot_comp_prod():
        yes_counts = df[['PhoneService', 'MultipleLines', 'StreamingTV', 'StreamingMovies']].apply(lambda x: x.value_counts().get('Yes', 0))
        internet_counts = df['InternetService'].value_counts().reindex(['DSL', 'Fiber optic']).fillna(0)
        final_counts = pd.concat([yes_counts, internet_counts])
        total_customers = len(df)
        percentages = (final_counts / total_customers) * 100
        norm = plt.Normalize(final_counts.min(), final_counts.max())
        colors = plt.cm.Reds(norm(final_counts.values))  
        fig, ax = plt.subplots(figsize=(12, 7))
        bars = ax.bar(final_counts.index, final_counts.values, color=colors)
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, '{:.1f}%'.format((yval/total_customers)*100), ha='center', va='bottom')
        ax.set_ylabel('Jumlah Customers', fontweight='bold', fontsize=14)
        ax.set_title('Perbandingan Jumlah Pelanggan Perusahaan', fontsize=18, fontweight='bold')
        ax.tick_params(axis='x', labelsize=14)
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_comp_prod()

    st.write('Dapat diidentifikasi bawha perusahaan memiliki layanan jasa penyedia telekomunikasi Telepon, layanan Streaming, dan layanan penyediaan internet. Mayoritas pelanggan perusahaan adalah pengguna layanan PhoneService, atau bisa dikatakan hampir semua pelanggan menggunakan layanan telepon. Pada layanan internet, "Fiber Optic" merupakan layanan yang lebih banyak dipilih dibandingkan dengan "DSL".Terkait layanan Streaming, pelanggan memiliki preferensi yang sama untuk kedua produk streaming.')

    st.write('')

    # Membuat Visialisasi Perbandingan Jumlah Customers Berdasarkan Segmen "Additional Product"
    def plot_add_product():
        comp_service = df[['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport']]
        yes_counts = comp_service.apply(lambda x: x.value_counts().get('Yes', 0))
        total_customers = len(df)
        percentages = (yes_counts / total_customers) * 100
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(yes_counts.index, yes_counts.values, color='orange')
        for bar in bars:
            width = bar.get_width()
            ax.text(width - (0.03 * total_customers), 
                    bar.get_y() + bar.get_height()/2, 
                    '{:.1f}%'.format((width/total_customers)*100), 
                    ha='center', va='center', color='black', fontweight='bold')
        ax.set_xlabel('Jumlah Pelanggan/Subscribers', fontsize=14, fontweight='bold')
        ax.set_title('Perbandingan Jumlah Pelanggan untuk Layanan Servis Tambahan', fontweight='bold', fontsize=16)
        plt.tight_layout()
        plt.show()   
        st.pyplot(plt)
    # Streamlit code
    plot_add_product()

    st.write('\nData diatas menampilkan layanan tambahan yang disediakan oleh perusahaan apabila pelanggan berminat upgrade dari layanan utama. Online Backup dan Device Protection merupakan layanan tambahan yang lebih banyak dipilih oleh pelanggan.')

    st.write('')

    st.write('#### Analisis "Churn Rate" Berdasarkan Lini Produk dan Layanan Perusahaan')
    # Visualisasi Pie Chart Untuk Perbandingan Churn Berdasarkan Segmen Produk 
    def plot_all_prod():
        text_properties = {'fontsize': 16, 'fontweight':'bold'}
        colors = ['#FF0000','#FF8361', '#FFAF9F']  # Menetapkan Warna Pie Chart
        cmap = mpl.colors.LinearSegmentedColormap.from_list("", colors)
        def plot_pie_for_column(column_name, ax):
            grouped = df.groupby([column_name, 'Churn']).size().unstack().fillna(0)
            if column_name == 'PhoneService':
                grouped = grouped.reindex(['Yes', 'No'])
            if column_name == 'InternetService':
                grouped = grouped.reindex(['Fiber optic', 'DSL', 'No'])
            norm = mpl.colors.Normalize(vmin=0, vmax=grouped['Yes'].sum())
            pie_colors = [cmap(norm(value)) for value in grouped['Yes']]
            ax.pie(grouped['Yes'], labels=grouped.index, autopct='%1.1f%%', startangle=90, colors=colors, textprops=text_properties)
            ax.set_title(f"%Churn Layanan {column_name}", fontsize=23, fontweight='bold')
        fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 12))
        plot_pie_for_column('PhoneService', axes[0][0])
        plot_pie_for_column('MultipleLines', axes[0][1])
        axes[0][2].axis('off')
        plot_pie_for_column('InternetService', axes[1][0])
        plot_pie_for_column('StreamingTV', axes[1][1])
        plot_pie_for_column('StreamingMovies', axes[1][2])
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_all_prod()

    st.write('Dari total customer yang berhenti menggunakan layanan perusahaan, hanya sekitar 9% yang bukan pelanggan Phone Service, sedangkan mmayoritas 90% merupakan customer yang subscribe atau berlanggananan PhoneService. Dalam hal ini, mayoritas pelanggan ada kecenderungan yang cukup besar merasa tidak puas terhadap layanan ini. Sekitar 45% dari pelanggan yang berhenti merupakan pelanggan yang memiliki layanan MultipleLines atau layanan telepon dengan jaringan lebih dari satu. Berdasarkan produk layanan internet, hampir 70% customer yang meninggalkan perusahaan adalah pelanggan yang subscribe layanan Fiber optic. Sedangkan untuk layanan internet DSL, hanya sekitar 24% pelanggan yang meninggalkan perushaan bersumber dari layanan ini. Kira-kira 40% dari total keseluruhan pelanggan yang unsubscribe merupakan pelanggan yang sebelumnya subscribe terhadap layanan Streaming TV dan Movies.')

    st.write('')

    # Visualisasi Perbandingan Churn Berdasarkan Segmen Layanan Jasa
    def plot_churn_addit():
        pie_colors = ['#FF0000', '#FF8361']
        text_properties = {'fontsize': 14, 'fontweight':'bold'}
        def plot_pie_for_column(column_name, ax):
            grouped = df.groupby([column_name, 'Churn']).size().unstack().fillna(0)
            ax.pie(grouped['Yes'], labels=grouped.index, autopct='%1.1f%%', startangle=90, colors=pie_colors, textprops=text_properties)
            ax.set_title(f"%Churn Layanan {column_name}", fontsize=14, fontweight='bold')
        fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(18, 5))
        plot_pie_for_column('OnlineSecurity', axes[0])
        plot_pie_for_column('OnlineBackup', axes[1])
        plot_pie_for_column('DeviceProtection', axes[2])
        plot_pie_for_column('TechSupport', axes[3])
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_churn_addit()

    st.write('Hanya sekitar 15% dari customer yang memutuskan berhenti adalah customer yang sebelumnya pengguna layanan Online Security dan Layanan TechSupport. Hal ini menunjukkan adanya kecenderungan pelanggan merasa puas dalam pelayanan ini dibandingkan dengan pelayanan produk lainnya. Berdasarkan layanan Online Backup dan Device Protection, kira-kira sekitar 28-29% customer yang berhenti langganan berasal dari layanan ini. ')

    st.write('')
    st.write('#### Perbandingan Customer Berdasarkan Tipe Kontrak')  

    # Visualisasi Perbandingan Customer Berdasarkan Tipe Kontrak
    def plot_cont_type():    
        text_properties = {'fontsize': 10, 'fontweight':'bold'}
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
        grouped = df[df['Churn'] == 'Yes']['Contract'].value_counts()
        colors = ['#FF0000','#FF8361', '#FFAF9F']
        labels = grouped.index
        axes[0].pie(grouped, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, textprops=text_properties)
        axes[0].set_title("%Churn Berdasarkan Tipe Kontrak", fontsize=15, fontweight='bold')
        contract_counts = df['Contract'].value_counts().sort_index()
        bars = axes[1].bar(contract_counts.index, contract_counts, color=colors)
        axes[1].set_title("Jumlah Customers Berdasarkan Tipe Kontrak", fontsize=15, fontweight='bold')
        axes[1].set_ylabel("Jumlah Customers", fontweight='bold')
        axes[1].set_xlabel("Tipe Kontrak", fontweight='bold')
        for bar in bars:
            yval = bar.get_height()
            axes[1].text(bar.get_x() + bar.get_width()/2, yval + 20, yval, ha='center', va='bottom')
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_cont_type()

    st.write('Sebagian besar customer menggunakan layanan perusahaan dengan jangka waktu paket atau kontrak layanan bulanan. Sebagian lainnya adalah anatara customer yang menggunakan paket annual per tahuan atau paket kontrak 2 tahun. Terlihat bahwa mayoritas customer yang memilih untuk berhenti berlangganan paling banyak adalah customer yang memiliki paket bulanan, sehingga ada kecenderungan yang kuat pelanggan yang merasa paling tidak puas adalah pelanggan yang memiliki kontrak jangka pendek dengan perusahaan.')
    st.write('')

    # Visualisasi Perbandingan Customer Berdasarkan Metode Pembayaran
    def plot_pay_mtd():
        text_properties = {'fontsize': 14, 'fontweight':'bold'}
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
        payment_grouped = df[df['Churn'] == 'Yes']['PaymentMethod'].value_counts()
        colors_payment = ['#FF0000','#E96361','#FF8361', '#FFAF9F']
        labels_payment = payment_grouped.index
        axes[0].pie(payment_grouped, labels=labels_payment, autopct='%1.1f%%', colors=colors_payment, startangle=140, textprops=text_properties)
        axes[0].set_title("%Churn Berdasarkan Metode Pembayaran", fontsize=18, fontweight='bold')
        billing_grouped = df[df['Churn'] == 'Yes']['PaperlessBilling'].value_counts()
        colors_billing = ['#FF0000','#FF8361']
        labels_billing = billing_grouped.index
        axes[1].pie(billing_grouped, labels=labels_billing, autopct='%1.1f%%', colors=colors_billing, textprops=text_properties)
        axes[1].set_title("%Churn Berdasarkan Tagihan Elektronik", fontsize=18, fontweight='bold')
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_pay_mtd() 

    st.write('Mayoritas pelanggan yang tidak lanjut menggunakan produk perusahaan merupakan pelanggan yang membayar dengan cek elektronik. Terkait dengan hal ini, perlu dianalisis lebih lanjut apakah ada keterkaitan antara metode pembayaran dengan potensi churn atau pelanggan yang cancel subscription. Presentase Churn yang tinggi pada tagihan elektornik juga perlu dievaluasi apakah ada keterkaitan antara tagihan elektronik yang terlambat atau tidak akurat terkait tagihan yang diterbitkan melalui elektronik.')

    st.write('')
    st.write('#### Analisis "Churn Rate" Berdasarkan Periode Penggunaan Layanan')  

    # Membuat Visualisasi Customer Churn Berdasarkan Jangka Waktu Langganan
    def plot_time_cust():
        bins = list(range(0, 81, 10)) 
        labels = ['{}-{}'.format(i, i+10) for i in range(0, 71, 10)]
        df['tenure_range'] = pd.cut(df['tenure'], bins=bins, labels=labels, right=False)
        colors = ['#4CAF50', 'r'] 
        grouped = df.groupby(['tenure_range', 'Churn']).size().unstack().fillna(0)
        fig, ax = plt.subplots(figsize=(15, 7))
        grouped.plot(kind='bar', stacked=False, ax=ax, width=0.6, color=colors)
        bar_width = 0.3
        for i, (label, row) in enumerate(grouped.iterrows()):
            total = row.sum()
            for j, val in enumerate(row):
                percentage = f"{val / total * 100:.1f}%"
                x_pos = i - bar_width / 2 + j * bar_width
                y_pos = val + 5 
                ax.text(x_pos, y_pos, percentage, ha='center', va='center', rotation=0)
        ax.set_title('Perbandingan Jumlah Customer Berdasarkan Tenor/Jangka Waktu Berlangganan', fontweight='bold', fontsize=20)
        ax.set_xlabel('Jangka Waktu (Bulan)', fontweight='bold')
        ax.set_ylabel('Jumlah Customers', fontweight='bold')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_time_cust()

    st.write('Dapat teridentifikasi bahwa paling banyak jumlah pelanggan yang memutuskan cancel subscription adalah pada periode awal, yaitu antara 0 sampai 10 bulan atau bisa dikatakan pelanggan yang relatif baru. Terlihat pola semakin lama pelanggan sudah berlangganan, semakin kecil tingkat "Churn Rate", yang dapat diinterpretasikan bahwa semakin lama pelanggan telah menggunakan layanan perusahaan, maka tingkat loyalitasnya semakin tinggi sehingga probabilitas berpindah layanan atau berhenti menjadi pelanggan semakin minim. Dari visualisasi diatas, perusahaan ada kecenderungan lebih memprioritaskan pelanggan-pelanggan yang existing dibandingkan dengan nasabah yang baru, yang mungkin terkait dengan customer loyalty program yang baik dan lebih diprioritaskan untuk pelanggan-pelanggan yang setia sejak lama.')

    st.write('')
    st.write('#### Analisis Perbandingan Customer Churn Berdasarkan Tenor')

    # Visualisasi Perbandingan Customer Churn Berdasarkan Tenor dan Profil Customers
    # Mengelompokkan Kolom Visualisasi
    l1 = ['gender','SeniorCitizen','Partner','Dependents']  # Informasi Profil Customers
    l2 = ['PhoneService','MultipleLines','InternetService','StreamingTV','StreamingMovies',
        'OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport']  # Informasi Layanan
    l3 = ['Contract','PaperlessBilling','PaymentMethod']    # Informasi Metode Pembayaran
    def plot_tnr_profile():
        colors = ['#4CAF50', 'r']
        fig = plt.subplots(nrows = 2, ncols = 2, figsize = (15,10))
        for i in range(4):
            plt.subplot(2,2,i+1)
            ax = sns.boxplot(x = l1[i], y = 'tenure', data = df,hue = 'Churn', palette = colors);
            plt.subplots_adjust(hspace=0.3)
            plt.title('\ntenure vs ' + l1[i], fontweight='bold');
        st.pyplot(plt)
    # Streamlit code
    plot_tnr_profile()   

    st.write('Berdasarkan gender, baik pelanggan laki-laki atau peremupan memiliki kecenderungan pola yang sama, dimana lebih banyak pelanggan yang memutuskan berhenti berlangganan pada periode kisaran 0 sampai 25 bulan. Jika dilihat secara perbandingan umur, terlihat pelanggan dengan lanjut usia cenderung memiliki rentang waktu yang lebih lama untuk memutuskan berhenti berlangganan, sehingga bisa dikatakan layanan perusahaan lebih diterima dikalangan usia yang lebih tua. Berdasarkan status berkeluarga atau berpasangan, dapat dilihat ada kecenderungan layanan perusahaan lebih diminati oleh kalangan pelanggan yang sudah berkeluarga dan memiliki pasangan dibandingkan dengan kalangan yang belum menikah dan belum memiliki tanggungan.')
    st.write('')

    st.write('')
    st.write('#### Perbandingan Tenor, Tipe Kontrak, dan Tipe Pembayaran')

    # Visualisasi Perbandingan Tenor, Tipe Kontrak Layanan Customers, dan Tipe Pembayaran
    def plot_tnr_bill():
        colors = ['#4CAF50', 'r'] 
        fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(25, 7))
        for i in range(len(l3)):
            plt.subplot(1, 3, i + 1)
            ax = sns.boxplot(x=l3[i], y='tenure', data=df, hue='Churn', palette=colors)
            plt.title('tenure vs ' + l3[i], fontweight='bold', fontsize=20)
            ax.tick_params(axis='x', labelsize=17)  
            ax.tick_params(axis='y', labelsize=12)  
            def split_label(label):
                if len(label) <= 15:
                    return label
                mid = len(label) // 2  
                split_point = mid + label[mid:].find(' ') 
                if split_point == mid: 
                    split_point = label.rfind(' ', 0, mid)
                if split_point == -1: 
                    return label[:mid] + '\n' + label[mid:]
                return label[:split_point] + '\n' + label[split_point+1:]
        labels = [split_label(label.get_text()) for label in ax.get_xticklabels()]
        ax.set_xticklabels(labels, fontsize=12)
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_tnr_bill() 

    st.write('Terlihat berdasarkan tipe kontrak, pelanggan dengan tipe kontrak bulanan memiliki rata-rata memilih untuk berhenti berlangganan pada kisaran 1 sampai 20 bulan, sedangkan tipe kontrak yang lebih lama, seperti kontrak tahunan memiliki rata-rata berlangganan kisaran 30 bulan sampai 60 bulan. Pelanggan yang menerima tagihan elektronik terlihat memiliki rata-rata kisaran 1 sampai 30 bulan bagi pelanggan yang berhenti berlangganan. Untuk pelanggan perusahaan yang melakukan pembayaran dengan cek baik elekronik maupun "Mailed check" terlihat memiliki rata-rata berlangganan yang lebih sebentar dibandingkan dengan pelanggan yang memilik metode pembyaran trasnfer dan kartu kredit.')

    st.write('')
    st.write('#### Analisis "Churn Rate" Berdasarkan Tagihan yang dibayarkan oleh Pelanggan')

    # Membuat Visualisasi Perbandingan Jumlah Customer Bersasarkan Tagihan Per-bulan
    def plot_mth_pay():
        bins = np.arange(0, 121, 20)
        labels = [f'{i}-{i+19}' for i in range(0, 120, 20)]
        df['MonthlyChargeBin'] = pd.cut(df['MonthlyCharges'], bins=bins, labels=labels, right=False)
        colors = ['#4CAF50', 'r']
        grouped = df.groupby(['MonthlyChargeBin', 'Churn']).size().unstack(fill_value=0)
        ax = grouped.plot(kind='bar', stacked=False, figsize=(10, 6), width=0.8, color=colors)
        bar_width = 0.4
        for i, (label, row) in enumerate(grouped.iterrows()):
            total = row.sum()
            for j, val in enumerate(row):
                percentage = f"{val / total * 100:.1f}%"
                x_pos = i - bar_width / 2 + j * bar_width
                y_pos = val + 5 
                ax.text(x_pos, y_pos, percentage, ha='center', va='center', rotation=0)
        ax.set_xticklabels(labels, rotation=0)
        ax.set_xlabel('Kisaran Tagihan Per-Bulan', fontweight='bold')
        ax.set_ylabel('Jumlah Customers', fontweight='bold')
        ax.set_title('Jumlah Customers Berdasarkan Tagihan Bulanan', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_mth_pay() 

    st.write('Pelanggan paling banyak memiliki kisaran tagihan usd 80 sampai usd 99, sedangkan diurutan kedua terbanyak adalah kisaran usd 20 sampai usd 39, dan selanjutnya pada kisaran tagihan usd 60 sampai usd 79. Berdasarkan visualisasi diatas, terlihat ada kecenderungan untuk pelanggan yang memiliki tagigan yang besar memiliki "Churn Rate" yang juga semakin besar. Dapat dilihat pada rentang tagihan usd 80 hingga usd 99 sekitar 36% pelanggan yang berhenti berlangganan. Hal ini dapat mengindikasikan adanya kecendrungan ketidaksesuaian antara ekspektasi pelanggan terhadap tagihan yang dibayarkan.')

    st.write('')

    # Membuat Visualisasi Perbandingan Jumlah Customers Berdasarkan Total Tagihan
    def plot_yr_pay():
        bins = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 8000]
        labels = ['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000', '3000-3500', '> 3500']
        df['TotalChargeBin'] = pd.cut(df['TotalCharges'], bins=bins, labels=labels, right=False)
        colors = ['#4CAF50', 'r']
        grouped = df.groupby(['TotalChargeBin', 'Churn']).size().unstack(fill_value=0)
        ax = grouped.plot(kind='bar', stacked=False, figsize=(10, 6), width=0.8, color=colors)
        bar_width = 0.4
        for i, (label, row) in enumerate(grouped.iterrows()):
            total = row.sum()
            for j, val in enumerate(row):
                percentage = f"{val / total * 100:.1f}%"
                x_pos = i - bar_width / 2 + j * bar_width
                y_pos = val + 5 
                ax.text(x_pos, y_pos, percentage, ha='center', va='center', rotation=0)
        ax.set_xticklabels(labels, rotation=0)
        ax.set_xlabel('Total Tagihan', fontweight='bold')
        ax.set_ylabel('Jumlah Customers', fontweight='bold')
        ax.set_title('Perbandingan Jumlah Customers Berdasarkan Total Tagihan', fontweight='bold', fontsize=15)
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_yr_pay() 

    st.write('Mayoritas pelanggan memiliki total tagihan diatas usd 3500 per tahun atau pada kisaran tagihan yang paling besar. Namun, juga banyak pelanggan yang memiliki tagihan kurang dari usd 500 atau ini dapat diasumsikan pelanggan yang baru saja subscribe sehingga perhitungan tagihannya masih belum terkalkulasi pada saat data ini dikumpulkan. Jika dilihat berdasarkan presentase "Churn Rate", dapat dilihat bahwa nilai total tagihan 0 sampai usd 500 memiliki presentase yang paling besar, yaitu 41%. Hal ini mungkin terkait dengan banyaknya cancel subscription bagi pelanggan-pelanggan yang baru, sehingga total akumulasi tagihannya masih relatif sedikit.')

    st.write('')

    # Visualisasi Perbandingan Customers Berdasarkan Profil dan Tagihan Per-bulan
    def plot_yr_prf():
        colors = ['#4CAF50', 'r'] 
        fig = plt.subplots(nrows = 2,ncols = 2,figsize = (15,10))
        for i in range(4):
            plt.subplot(2,2,i+1)
            ax = sns.boxplot(x = l1[i],y = 'MonthlyCharges', data = df,hue = 'Churn', palette = colors);
            plt.subplots_adjust(hspace=0.3)
            plt.title('MonthlyCharges vs ' + l1[i], fontweight='bold');
        st.pyplot(plt)
    # Streamlit code
    plot_yr_prf() 

    st.write('Secara garis besar, terlihat pelanggan memiliki rata-rata kisaran usd 60 hingga usd 90 pada saat memutuskan cancel subsription. Jika dilihat berdasarkan gender, terlihat baik laki-laki dan perempuan memilki total tagihan yang tidak berbeda, dan juga sedikit kecenderungan pada tagihan yang lebih besar lebih banyak yang cancel subscription. Terlihat pelanggan dengan usia lanjut memiliki rentang rata-rata tagihan bulanan yang lebih besar dibandingkan dengan pelanggan yang lebih muda. Namun, kedua golongan memiliki kesamaan dimana rentang tagihan pelanggan yang cancel subsription berada pada kisaran usd 80 rata-rata tertingginya. Pada pelanggan yang memilki pasangan terlihat memiliki rata-rata rentang tagihan yang lebih besar dibandingkan dengan yang belum berpasangan. Hal ini wajar dimana ketika sudah berpasnagan, umumnya layanan uang diperlukan juga semakin banyak. Tagihan kisaran usd 70 hingga usd 100 adalah kisaran tagihan dimana pelanggan memtuskan untuk bergenti berlangganan. Pada pelanggan yang memiliki tanggungan maupun tidak memiliki tanggungan memilki kisaran yang hampir sama dalam pembayaran tagihan, pada rentang tagihan sampai $90. Dengan pola yang juga sama, dimana pada rata-rata yang tagihan yang lebih besar pelanggan memutuskan berhenti berlangganan.')

    st.write('')

    # Visualisasi Perbandingan Customers Berdasarkan Layanan dan Tipe Kontrak
    def plot_yr_bill():
        colors = ['#4CAF50', 'r']  
        fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(25, 7))
        for i in range(len(l3)):
            plt.subplot(1, 3, i + 1)
            ax = sns.boxplot(x=l3[i], y='MonthlyCharges', data=df, hue='Churn', palette=colors)
            plt.title('MonthlyCharges vs ' + l3[i], fontweight='bold', fontsize=20)
            # Increase the label sizes
            ax.tick_params(axis='x', labelsize=17)  
            ax.tick_params(axis='y', labelsize=12)  
        def split_label(label):
            if len(label) <= 15:
                return label
            mid = len(label) // 2  
            split_point = mid + label[mid:].find(' ') 
            if split_point == mid:  
                split_point = label.rfind(' ', 0, mid)
            if split_point == -1:
                return label[:mid] + '\n' + label[mid:]  
            return label[:split_point] + '\n' + label[split_point+1:]
        labels = [split_label(label.get_text()) for label in ax.get_xticklabels()]
        ax.set_xticklabels(labels, fontsize=15)
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    # Streamlit code
    plot_yr_bill() 

    st.write('Pada visualisasi diatas, terlihat ada kecenderungan untuk rata-rata tagihan yang lebih tinggi, pelanggan lebih memilih berhenti berlangganan. Hal ini konsiten terlihat pada pelanggan yang memiliki kontrak bulanan, tahunan, maupun tahunan. Pada kisaran tagihan yang lebih tinggi, pelanggan memutuskan untuk berhenti, dalam hal ini kisaran diatas $85. Pada pelanggan yang memiliki tagihan elektronik, terlihat memiliki kisaran yang tagihan lebih tigggi dibandingkan dengan non elektronik. Pelanggan yang tidak memiliki tagihan eletronik cenderung memutuskan langganan pada harga yang lebih rendah dikisaran usd 45 hingga usd 80. Pada pelanggan yang melakukan pembayaran tagihan "Mailed Check" terlihat memiliki rata-rata kisaran tagihan yang lebih rendah diabndingkan dengan pelanggan yang melakukan pembayaran dengan metode lain. Namun secara garis besar, terlihat pola yang mirip diantara semua tipe pembayaran pelanggan, dimana pelanggan yang memilih untuk berhenti berlangganan cenderung memiliki rata-rata tagihan yang tinggi.')