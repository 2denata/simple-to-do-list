from flask_sqlalchemy import SQLAlchemy

# ORM buat atur db
db = SQLAlchemy()

# Model tabel database task
class Todo(db.Model):
    # id
    id = db.Column(db.Integer, primary_key=True)

    # nama task
    task = db.Column(db.String(200))

    # prioritas (low, medium, atau high)
    priority = db.Column(db.String(10), default='medium')  # high/medium/low
    
    # udah dilakukan atau belum
    is_completed = db.Column(db.Boolean, default=False)