# main.py
from tabulate import tabulate
from kurs import kurs
from konverter import konversi

def tampilkan_kurs():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, f"{nilai:,}".replace(",", ".")])
    
    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

def main():
    tampilkan_kurs()
    
    daftar_mata_uang = ["IDR"] + list(kurs.keys())
    
    dari = input(f"Dari ({'/'.join(daftar_mata_uang)}): ").upper()
    ke = input(f"Ke ({'/'.join(daftar_mata_uang)}): ").upper()
    jumlah = float(input("Jumlah: "))
    
    hasil = konversi(dari, ke, jumlah)
    
    if ke == "IDR":
        print(f"{jumlah} {dari} = {format_rupiah(hasil)}")
    else:
        print(f"{format_rupiah(jumlah) if dari=='IDR' else jumlah} {dari} = {hasil:.2f} {ke}")

if __name__ == "__main__":
    main()
    