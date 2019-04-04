from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return '<h1>Hello World !!!</h1>'


"""
Tipos se SQLAlchemy
db.String
db.Text
db.Integer
db.Float
db.Boolean
db.Date
db.DateTime
db.Time

Por defecto se asume que el nombre de la columna es igual al de la variable

    username = db.Column(db.String(255))
    username = db.Column('user_name', db.String(255))

También se asume que la tabla tiene le mismo nombre que la clase, en el caso
de que no sea así, se puede especicar el nombre de la misma.

    class User(db.Model):
        __tablename__ = 'user_table_name'
        ...

Si no creamos el método __init__ SQLAlchemy creará uno por defecto, que espera
recibir por parámetros los nombres y los valores de las columnas.
"""
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = usernme

    def __repr__(self):
        return "<User '{}'>".format(self.username)


if __name__ == '__main__':
    app.run()

