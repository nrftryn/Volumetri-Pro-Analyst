import streamlit as st

st.title('Volumetri Pro-Analyst')

st.write('Oleh Kelompok 9')
st.write('Hanna Laila Isnaini (2360134)')
st.write('Meylian Dwi Yasmien (2360174)')
st.write('Nazwa Kayla Aulianisya (2360212)')
st.write('Noor Rezky Fitriansyah (2360215)')
st.write('Rifda Nazwa Davina Alita (2360241)')

tab1, tab2, tab3 = st.tabs(['Informasi Titrasi', 'Informasi Konsentrasi', 'Kalkulator Konsentrasi'])

with tab1:
    st.header('Informasi Titrasi')
    st.write('Titrasi adalah proses penambahan larutan standar dari buret sedikit demi sedikit sampai jumlah zat yang direaksikan tepat ekuivalen satu sama lain.')
    st.write('Berikut ini terdapat penggolongan titrasi berdasarkan reaksi kimia :')

    titri_option = st.selectbox('Pilih Jenis Titrasi', ['None','Asidimetri - Alkalimetri','Redoks','Presipimetri','Kompleksometri'])
    
    if titri_option == 'Asidimetri - Alkalimetri' :
        st.subheader('Titrasi Asidimetri - Alkalimetri')
        st.write('adalah salah satu jenis titrasi yang digunakan untuk menentukan konsentrasi suatu asam atau basa dengan menggunakan larutan basa atau asam standar sebagai titran. Prinsip dasar dari titrasi asidi-alkalimetri adalah reaksi netralisasi antara asam dan basa.')

    if titri_option == 'Redoks' :
        st.subheader('Titrasi Reduksi Oksidasi (Redoks)')
        st.write('adalah titrasi yang digunakan untuk menentukan konsentrasi suatu zat dengan mengukur kemampuan oksidasi atau reduksinya. Dalam titrasi redoks, terjadi reaksi oksidasi-reduksi antara analit (zat yang akan ditentukan) dan titran (zat pengoksidasi atau pereduksi).')
        st.write('Contoh dari titrasi redoks yaitu :')
        st.write('Titrasi Permanganometri, yaitu titrasi yang menggunakan larutan kalium permanganat (KMnO4) sebagai titran.')
        st.write('Titrasi Iodometri, yaitu titrasi redoks yang melibatkan titrasi iodin yang diproduksi dalam reaksi dengan larutan standar natrium tiosulfat.')

    if titri_option == 'Presipimetri' :
        st.subheader('Titrasi Presipimetri (Pengendapan)')
        st.write('adalah salah satu jenis titrasi kuantitatif yang digunakan untuk menentukan konsentrasi suatu zat dengan cara mengendapkannya dalam bentuk senyawa yang tidak larut (presipitat), yang dimana semakin kecil kelarutan endapan maka semakin sempurna reaksinya. Contoh dari titrasi presipimetri adalah titrasi argentometri yaitu titrasi yang menggunakan larutan perak.')
    
    if titri_option == 'Kompleksometri' :
        st.subheader('Titrasi Kompleksometri')
        st.write('adalah salah satu jenis titrasi kuantitatif yang digunakan untuk menentukan konsentrasi suatu ion logam dalam larutan dengan menggunakan suatu senyawa pengompleks (komplekson) sebagai titran.')






with tab2:
    st.header('Informasi Konsentrasi')
    st.write('Larutan dalam ilmu kimia mempunyai arti yaitu campuran yang bersifat homogen dengan perbandingan komposisi sesuai dengan komponen penyusunnya. Pada umumnya, suatu larutan terdiri satu jenis zat terlarut dan satu pelarut. Solvent (pelarut) dan Solut (zat yang terlarut). Konsentrasi larutan adalah jumlah zat yang terlarut dalam setiap satuan larutan atau pelarut.')
    st.write('Secara sederhana, konsentrasi larutan dapat memberikan gambaran atau sebuah informasi tentang perbandingan jumlah zat terlarut dan jumlah pelarutnya. Konsentrasi larutan yang biasa dipakai pada laboratorium ada banyak jenisnya')
    st.write('Berikut ini terdapat konsentrasi larutan :')

    kons_option = st.selectbox('Pilih Jenis Konsentrasi', ['None','Normalitas','Molaritas','% Kadar (b/v)','% kadar (b/b)'])

    if kons_option == 'Normalitas':
        st.subheader('Normalitas (N)')
        st.write('Normalitas adalah jumlah ekuivalen suatu zat terlarut dibagi volume larutan dalam liter dengan simbol yang dimiliki yaitu N. Normalitas juga dikenal sebagai konsentrasi setara. Setara adalah banyaknya zat terlarut yang akan bereaksi dengan sejumlah tertentu (biasanya satu mol) reaktan lain.')
    
    if kons_option == 'Molaritas':
        st.subheader('Molaritas (M)')
        st.write('Molaritas dalam konsentrasi larutan dikenal dengan istilah konsentrasi molar atau molaritas dengan simbol yang dimiliki yaitu M. Molaritas digunakan untuk mendapatkan konsentrasi larutan secara kuantitatif. Dinyatakan sebagai jumlah mol suatu Solut dalam larutan dibagi dengan volume larutan yang ditentukan dalam liter.')

    if kons_option == '% kadar (b/b)':
        st.subheader('% Kadar (b/b)')
        st.write('Konsentrasi berat suatu larutan dinyatakan sebagai % (b/b). Dalam hal ini, volume masing-masing bahan kimia diabaikan dan hanya beratnya saja yang digunakan, persen berat sering digunakan karena persen ini tidak bergantung pada temperatur suhu.')

    if kons_option == '% Kadar (b/v)':
        st.subheader('% Kadar (b/v)')
        st.write('Konsentrasi massa larutan dinyatakan sebagai % (b/v) untuk berat per volume. Ini digunakan ketika bahan kimia padat dilarutkan dalam cairan.')


with tab3:
    st.header('Hitung Normalitas')

    default_value = 1.0000
    min_value = 0.0000
    max_value = 9999.0000
    
    massa1 = st.number_input('Masukkan nilai massa (mg)',format="%.4f",value=default_value,key='massa1')
    volume1 = st.number_input('Masukkan nilai volume titran (mL)',format="%.2f",value=default_value,key='volume1')
    BE1 = st.number_input('Masukkan nilai BE (mg/mgrek)',format="%.1f",value=default_value,key='BE1')
    FP1 = st.number_input('Masukkan nilai FP',format="%.0f",value=default_value,key='FP1')

    tombol = st.button('Hitung nilai normalitasnya')

    nilai_normalitas1=massa1/(BE1*volume1*FP1)
    if tombol:
        nilai_normalitas = massa1/(BE1*volume1*FP1)
        st.success(f'Nilai normalitas adalah {nilai_normalitas:.4f} N')


    st.header('Hitung Molaritas')

    default_value = 1.0000
    min_value = 0.0000
    max_value = 9999.0000
    
    massa2 = st.number_input('Masukkan nilai massa (mg)',format="%.4f",value=default_value,key='massa2')
    volume2 = st.number_input('Masukkan nilai volume titran (mL)',format="%.2f",value=default_value,key='volume2')
    BM2 = st.number_input('Masukkan nilai BM (mg/mmol)',format="%.1f",value=default_value,key='BM2')
    FP2 = st.number_input('Masukkan nilai FP',format="%.0f",value=default_value,key='FP2')

    tombol = st.button('Hitung nilai molaritasnya')

    nilai_molaritas1=massa2/(BM2*volume2*FP2)
    if tombol:
        nilai_molaritas = massa2/(BM2*volume2*FP2)
        st.success(f'Nilai molaritas adalah {nilai_molaritas:.4f} M')

    st.header('Hitung % Kadar (b/v)')
    Vtitran3 = st.number_input('Masukkan nilai volume titran (mL)',key='Vtitran3')
    Ntitran3 = st.number_input('Masukkan nilai normalitas titran (mgrek/ml)',format='%.4f', value=(nilai_normalitas1),key='Ntitran3')
    BE3 = st.number_input('Masukkan nilai BE (mg/mgrek)',format="%.1f",key='BE3')
    FP3 = st.number_input('Masukkan nilai FP',format="%.0f",key='FP3')
    Vtitrat3 = st.number_input('Masukkan nilai volume titrat (mL)',format="%.0f",key='Vtitrat3')

    tombol1 = st.button('Hitung nilai kadarnya',key='tombol1')

    if tombol1:
        nilai_kadar = (Vtitran3*Ntitran3*BE3*10**-3*FP3*100)/Vtitrat3 
        st.success(f'Persentase kadarnya adalah {nilai_kadar:.2f}% (b/v)')
    
    st.header('Hitung % Kadar (b/b)')
    Vtitran4 = st.number_input('Masukkan nilai volume titran (mL)', key='Vtitran4')
    Ntitran4 = st.number_input('Masukkan nilai normalitas titran (N)',format='%.4f', value=(nilai_normalitas1), key='Ntitran4')
    BE4 = st.number_input('Masukkan nilai BE (mg/mgrek)',format="%.1f", key='BE4')
    FP4 = st.number_input('Masukkan nilai FP',format="%.0f",key='FP4')
    mtitrat4 = st.number_input('Masukkan nilai massa sampel (mg)',format="%.0f",key='mtitrat4')

    tombol2 = st.button('Hitung nilai kadarnya',key='tombol2')

    if tombol2:
        nilai_kadar = (Vtitran4*Ntitran4*BE4*FP4*100)/mtitrat4 
        st.success(f'Persentase kadarnya adalah {nilai_kadar:.2f}% (b/b)')