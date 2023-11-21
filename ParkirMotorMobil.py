import streamlit as st
from datetime import datetime #modul untuk waktu saat ini ketika akan keluar

TARIF_JAM_PERTAMA_MOTOR = 2000.0  # Biaya parkir untuk jam pertama (motor)
TARIF_PER_JAM_MOTOR = 2000.0      # Biaya parkir per jam setelah melewati jam pertama untuk motor

TARIF_JAM_PERTAMA_MOBIL = 5000.0  # Biaya parkir untuk jam pertama (mobil)
TARIF_PER_JAM_MOBIL = 5000.0      # Biaya parkir per jam setelah melewati jam pertama untuk mobil

# Function to calculate parking fee and cache the result

def hitung_tarif_parkir(jam_masuk, menit_masuk, jam_keluar, menit_keluar, jenis_kendaraan): #mendefinisikan hitungan tarif parkir kendaraan
    durasi_jam = jam_keluar - jam_masuk
    durasi_menit = menit_keluar - menit_masuk

    if durasi_menit < 0:
        durasi_jam -= 1
        durasi_menit += 60

    durasi_parkir = durasi_jam + durasi_menit / 60.0 #menghitung durasi waktu parkir per 60 menit

    if jenis_kendaraan == "Motor":
        tarif_jam_pertama = TARIF_JAM_PERTAMA_MOTOR #Setting waktu untuk tarif motor di jam pertama
        tarif_per_jam = TARIF_PER_JAM_MOTOR #Setting waktu untuk tarif motor di jam berikutnya
    elif jenis_kendaraan == "Mobil":
        tarif_jam_pertama = TARIF_JAM_PERTAMA_MOBIL #Setting waktu untuk tarif mobil di jam pertama 
        tarif_per_jam = TARIF_PER_JAM_MOBIL #Setting waktu untuk tarif mobil di jam berikutnya
    else:
        st.error("Jenis kendaraan tidak valid.")
        return 0, 0, 0

    biaya_parkir = tarif_jam_pertama if durasi_parkir <= 1.0 else tarif_jam_pertama + int(durasi_parkir) * tarif_per_jam #Mengatur agar tarif flat ke jam berikutnya agar menghitung berdasarkan durasi per jam 

    return durasi_jam, durasi_menit, biaya_parkir

def format_durasi(jam, menit):
    return f"{jam} jam {menit} menit"

def main():
    st.title("Aplikasi Penghitung Tarif Parkir") #Tampilan awal pada halaman

    # Pilih jenis kendaraan di halaman pertama
    jenis_kendaraan = st.sidebar.radio("Pilih Jenis Kendaraan:", ["Motor", "Mobil"]) #Memilih tampilan halaman untuk parkir motor dan mobil

    if jenis_kendaraan == "Motor": #Mengatur tampilan halaman untuk Motor
        st.header("Parkir Motor")
        st.write("Tarif parkir jam pertama 2000 berlaku kelipatan") #Memberitahu pada halaman yaitu tarif berlaku 2000 rupiah di setiap jamnya
        # Input Nomor kendaraan
        Kendaraan = st.text_input("Masukkan Nomor kendaraan Motor: ") #Menginput nomor kendaraan motor
    elif jenis_kendaraan == "Mobil": #Mengatur tampilan halaman untuk Mobil
        st.header("Parkir Mobil")
        st.write("Tarif parkir jam pertama 5000 berlaku kelipatan") #Memberitahu pada halaman yaitu tarif berlaku 5000 rupiah di setiap jamnya
        # Input Nomor kendaraan
        Kendaraan = st.text_input("Masukkan Nomor kendaraan Mobil: ") #Menginput nomor kendaraan mobil

    # Masukkan waktu masuk kendaraan
    jam_masuk = st.number_input("Masukkan jam masuk:", min_value=0, max_value=23) #Mengatur waktu (Jam) dari 0-23
    menit_masuk = st.number_input("Masukkan menit masuk:", min_value=0, max_value=59) #Mengatur waktu (menit) dari 0-59

    # Menghitung waktu keluar dengan modul datetime untuk menginput waktu saat ini ketika kendaraan keluar
    waktu_keluar = datetime.now() 
    jam_keluar = waktu_keluar.hour
    menit_keluar = waktu_keluar.minute

    # Menampilkan waktu keluar pada halaman website
    st.info(f"Waktu Keluar Sekarang: {jam_keluar:02d}:{menit_keluar:02d}")

    # Menghitung total tarif parkir berdasarkan waktu masuk dan keluar
    if st.button("Hitung Tarif"):
        durasi_jam, durasi_menit, biaya_parkir = hitung_tarif_parkir(
            jam_masuk, menit_masuk, jam_keluar, menit_keluar, jenis_kendaraan
        )
        durasi_parkir_formatted = format_durasi(durasi_jam, durasi_menit)
        st.success(f"Durasi Waktu Parkir: {durasi_jam} jam {durasi_menit} menit") #Tampilan durasi waktu parkir kendaraan
        st.success(f"Biaya Parkir: Rp {biaya_parkir:,.2f}") #Tampilan total biaya parkir pada kendaraan

if __name__ == "__main__":
    main()
