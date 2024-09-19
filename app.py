from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Fungsi untuk membaca data dari file Excel
def get_form_data():
    try:
        # Baca file Excel (pastikan nama file dan path benar)
        df = pd.read_excel('data_form.xlsx')
        print("Data Excel berhasil dibaca:", df.head())  # Debugging
        form_data = df.iloc[0].to_dict()  # Ambil data baris pertama
        return form_data
    except FileNotFoundError as e:
        print("File Excel tidak ditemukan:", e)
        return {}

# Route untuk menampilkan form
@app.route('/')
def form():
    data = get_form_data()  # Ambil data dari Excel
    print("Data dikirim ke template:", data)  # Debugging
    return render_template('form_with_autofill.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
    