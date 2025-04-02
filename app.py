from flask import Flask, render_template, redirect, url_for, request, flash  # Import modul Flask
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy buat database
from forms import TodoForm  # Import form yang sudah dibuat
from models import Todo, db  # Import model Todo dan database
from config import Config  # Import konfigurasi dari config.py

app = Flask(__name__)  # Inisialisasi aplikasi Flask
app.config.from_object(Config)  # Load konfigurasi dari config.py
db.init_app(app)  # Hubungkan aplikasi dengan database

# Route utama (menampilkan daftar tugas)
@app.route('/')
def index():
    emergency_mode = request.args.get('emergency', False)  # Cek apakah mode emergency aktif
    todos = Todo.query.all()  # Ambil semua task dari database
    
    if emergency_mode:
        todos = [todo for todo in todos if todo.priority == 'high']  # Filter hanya task prioritas tinggi
    
    return render_template('index.html', todos=todos)  # Render template index.html

# Route buat nambah tugas baru
@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    form = TodoForm()  # Inisialisasi form
    if form.validate_on_submit():  # Cek apakah form valid
        try:
            new_todo = Todo(
                task=form.task.data,
                priority=form.priority.data
            )  # Buat objek Todo baru
            db.session.add(new_todo)  # Tambah ke database
            db.session.commit()  # Simpan perubahan
            flash('Task berhasil ditambahkan!', 'success')  # Tampilkan notifikasi sukses
            return redirect(url_for('index'))  # Arahkan balik ke halaman utama
        except Exception as e:
            db.session.rollback()  # Batalkan perubahan jika ada error
            flash(f'Error: {str(e)}', 'danger')  # Tampilkan pesan error
    
    return render_template('add.html', form=form)  # Render halaman tambah tugas

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    todo_to_delete = Todo.query.get(todo_id)
    
    if todo_to_delete:
        try:
            db.session.delete(todo_to_delete)
            db.session.commit()
            flash('Task berhasil dihapus!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return redirect(url_for('index'))

# Inisialisasi database saat aplikasi dijalankan
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)