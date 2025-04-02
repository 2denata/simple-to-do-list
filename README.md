# Todo List dengan Flask
## Tentang Proyek
Ini adalah aplikasi Todo List sederhana yang dibangun menggunakan Flask, framework web untuk Python. Flask sangat cocok untuk pengembang yang ingin membuat aplikasi web dengan Python secara cepat dan efisien.

Aplikasi ini memungkinkan pengguna untuk:
- Tambah task dengan tingkat prioritas (Low, Medium, High)
- Tampilkan daftar task dengan warna sesuai prioritas
- Emergency Mode: Hanya tampilkan task dengan prioritas tinggi
- Hapus task dengan mudah
- Notifikasi saat task berhasil ditambahkan

# Library yang Digunakan
- Python (Flask, Flask-WTF, Flask-SQLAlchemy)
- SQLite (untuk database lokal)
- Bootstrap 5 (untuk desain yang responsif)
## Installation

1. Pastikan Python Terinstal
Jika python belum terinstal, download dulu [di sini](https://www.python.org/downloads/). Lalu pastikan Python dapat diakses lewat terminal atau command prompt dengan menjalankan perintah berikut:

```bash
python --version  #py atau python
```
Jika Python sudah terinstal, perintah di atas akan menampilkan versi Python yang terpasang.

2. Clone Repository
Clone dari repository ini
```bash
git clone https://github.com/2denata/simple-to-do-list.git
```

3. Masuk ke folder `simple-to-do-list` lalu buat Virtual Environment:
- Buat virtual environment di dalam folder proyek
    ```bash
    python -m venv venv
    ```
- Aktifkan virtual environment:
    ```bash
    venv\Scripts\activate
    ```

4. Install Dependencies:
```bash
pip install -r requirements.txt
```

5. Jalankan program:
```bash
python app.py
```

6. Buka browser dan akses aplikasi:
```bash
http://127.0.0.1:5000
```

## Struktur file proyek

```
/
│── templates/           # Folder untuk file HTML (index.html, add.html, base.html)
diperlukan
│── app.py               # File utama untuk menjalankan aplikasi Flask
│── config.py            # Konfigurasi aplikasi
│── models.py            # Model database (Todo)
│── forms.py             # Formulir input menggunakan Flask-WTF
│── requirements.txt     # Daftar dependencies Python
│── README.md            # Dokumentasi proyek
```
