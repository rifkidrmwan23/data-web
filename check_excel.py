import pandas as pd

try:
    # Pastikan path ke file Excel sudah benar
    df = pd.read_excel('C:/path/to/your/excel/data_form.xlsx')
    print(df.head())  # Menampilkan beberapa baris pertama dari file Excel
except FileNotFoundError as e:
    print("File tidak ditemukan:", e)
except Exception as e:
    print("Terjadi kesalahan lain:", e)
