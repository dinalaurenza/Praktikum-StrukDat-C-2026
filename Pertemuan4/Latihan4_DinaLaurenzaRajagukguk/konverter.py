# konverter.py

from kurs import kurs

def konversi(dari, ke, jumlah):
    if dari == "IDR":
        return jumlah / kurs[ke]
    elif ke == "IDR":
        return jumlah * kurs[dari]
    else:
        # Konversi antar mata uang asing lewat IDR
        dalam_idr = jumlah * kurs[dari]
        return dalam_idr / kurs[ke]
