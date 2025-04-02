import os

# Ambil path direktori skrip ini
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # secret key flask
    SECRET_KEY = 'nata'  # Jangan pakai ini di production!

    # Path DB SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    # Nonaktif notif db
    SQLALCHEMY_TRACK_MODIFICATIONS = False