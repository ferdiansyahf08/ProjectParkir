import streamlit as st
from datetime import datetime

TARIF_JAM_PERTAMA = 3000.0  # Biaya parkir untuk jam pertama
TARIF_PER_JAM = 3000.0  # Biaya parkir per jam setelah jam pertama

# List to store entered vehicle numbers
entered_vehicle_numbers = []

def hitung_tarif_parkir(jam_masuk, menit_masuk, jam_keluar, menit_keluar): #Mendefinisikan waktu tarif parkir
    # Hitung durasi parkir dalam jam
    durasi_jam = jam_keluar - jam_masuk
    durasi_menit = menit_keluar - menit_masuk

    # Menangani kasus jika durasi menit negatif
    if durasi_menit < 0:
        durasi_jam -= 1
        durasi_menit += 60

    # Hitung biaya parkir 
    durasi_parkir = durasi_jam + durasi_menit / 60.0 #menghitung durasi waktu parkir per 60 menit
    biaya_parkir = TARIF_JAM_PERTAMA if durasi_parkir <= 1.0 else TARIF_JAM_PERTAMA + int(durasi_parkir) * TARIF_PER_JAM #Mengatur agar tarif flat ke jam berikutnya agar menghitung berdasarkan durasi per jam 

    return durasi_jam, durasi_menit, biaya_parkir

def main():
    st.title("Aplikasi Penghitung Tarif Parkir") #Tampilan halaman
    st.write("Tarif parkir per jam Rp.3000") #Menginformasikan tarif parkir pada halaman

    # Input Nomor kendaraan
    kendaraan = st.text_input("Masukkan Nomor kendaraan: ") #Menginput nomor kendaraan pada halaman

    # Input waktu masuk
    jam_masuk = st.number_input("Masukkan jam masuk:", min_value=0, max_value=23)
    menit_masuk = st.number_input("Masukkan menit masuk:", min_value=0, max_value=59)

    # Menghitung waktu keluar ke waktu terkini dengan modul datetime
    waktu_keluar = datetime.now()
    jam_keluar = waktu_keluar.hour
    menit_keluar = waktu_keluar.minute

    # Input waktu keluar sebagai waktu terkini agar ditampilkan di halaman
    st.info(f"Waktu Keluar Sekarang: {jam_keluar:02d}:{menit_keluar:02d}")
    
    # Menginformasikan Parkir
    if st.button("Informasi Parkir"):
        durasi_jam, durasi_menit, biaya_parkir = hitung_tarif_parkir(jam_masuk, menit_masuk, jam_keluar, menit_keluar)
        st.success(f"Nomor Kendaraan: {kendaraan}") #Menampilkan nomor kendaraan
        st.success(f"Durasi Waktu Parkir: {durasi_jam} jam {durasi_menit} menit") #Menampilkan durasi waktu parkir
        st.success(f"Total Biaya Parkir: Rp {biaya_parkir:,.2f}") #Menampilkan total biaya parkir

if __name__ == "__main__":
    main()