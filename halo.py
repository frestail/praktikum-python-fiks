# halo.py - program python pertama
import datetime
from colorama import Fore, init

# Inisialisasi colorama agar warna otomatis mereset tiap baris
init(autoreset=True)

nama = input("masukan nama Anda: ")
umur = input("Masukkan umur Anda: ")
print(Fore.YELLOW + f"Umur Anda adalah {umur} tahun.")
print(Fore.CYAN + f"Halo, {nama}! Selamat datang di praktikum")
print(Fore.MAGENTA + "Semoga sukses!")

print("\n# --- Tambahkan kode perkiraan usia di baris paling bawah ---")
try:
    tahun_lahir = int(input(Fore.GREEN + "Masukkan tahun lahir Anda: "))
    tahun_sekarang = datetime.datetime.now().year
    usia = tahun_sekarang - tahun_lahir
    print(Fore.BLUE + f"Perkiraan usia Anda berdasarkan tahun lahir adalah {usia} tahun.")
except ValueError:
    print(Fore.RED + "Error: Masukkan angka yang benar!")
