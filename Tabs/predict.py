import streamlit as st

from web_maintenance import predict

def app(df, x, y):

    st.title("Halaman Prediksi Services Kendaraan")

    col1, col2, col3 = st.columns (3)

    with col1:
        Vehicle_Model = st.number_input ('Jenis Kendaraan')
    with col1:
        Mileage = st.number_input ('Kilometer')
    with col1:
        Maintenance_History = st.number_input ('Riwayat Perbaikan')
    with col1:
        Reported_Issues = st.number_input ('Riwayat Keluhan')
    with col1:
        Vehicle_Age = st.number_input ('Usia Kendaraan')
    with col1:
        Fuel_Type = st.number_input ('Jenis BBM')
    with col2:
        Transmission_Type = st.number_input ('Jenis Transmisi')
    with col2:
        Engine_Size = st.number_input ('Ukuran Mesin')
    with col2:
        Odometer_Reading = st.number_input ('Odometer')
    with col2:
        Last_Service_Date = st.number_input ('Tanggal Services Terakhir')
    with col2:
        Warranty_Expiry_Date = st.number_input ('Tanggal Kadaluwarsa')
    with col2:
        Owner_Type = st.number_input ('Pemilik')
    with col3:
        Insurance_Premium = st.number_input ('Premi Asuransi')
    with col3:
        Service_History = st.number_input ('Riwayat Services')
    with col3:
        Accident_History = st.number_input ('Riwayat Kecelakaan')
    with col3:
        Fuel_Efficiency = st.number_input ('Efisiensi BBM')
    with col3:
        Tire_Condition = st.number_input ('Kondisi Ban')
    with col3:
        Brake_Condition = st.number_input ('Kondisi Rem')
    with col3:
        Battery_Status = st.number_input ('Status Baterai')

    features = [Vehicle_Model,Mileage,Maintenance_History,Reported_Issues,Vehicle_Age,Fuel_Type,Transmission_Type,Engine_Size,Odometer_Reading,Last_Service_Date,Warranty_Expiry_Date,Owner_Type,Insurance_Premium,Service_History,Accident_History,Fuel_Efficiency,Tire_Condition,Brake_Condition,Battery_Status]

    # Tombol Prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x, y, features)
        score = score
        st.info("Prediksi Sukses...")
    
    if (prediction == 1):
        st.warning("Kendaraan tersebut disarankan melakukan services rutin kendaraan")
    else:
        st.success("Kendaraan tersebut aman dari maintenance services rutin kendaraan")

    st.write("Model yang digunakan memiliki tingkat akurasi", (score*100),"%")