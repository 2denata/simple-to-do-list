from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    # Field input tugas (wajib diisi)
    task = StringField('Task', validators=[DataRequired()])

    # Dropdown buat pilih prioritas tugas
    priority = SelectField('Priority', choices=[
        ('high', 'High Priority 🔴'), 
        ('medium', 'Medium Priority 🟡'), 
        ('low', 'Low Priority 🟢')
    ])

    # Tombol submit buat tambah tugas
    submit = SubmitField('Add Task')