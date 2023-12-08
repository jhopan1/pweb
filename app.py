from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# IMPORT MODEL
# from Models.UserModel import db, bcrypt
# IMPORT CONTROLLER
# from Controllers.UserController import main_bp
from Controllers.RenderController import render_bp

app = Flask(__name__)
# Menambahkan path proyek ke dalam sys.path

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/pweb_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi objek SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(render_bp, url_prefix='/')

# Registrasi blueprint
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
