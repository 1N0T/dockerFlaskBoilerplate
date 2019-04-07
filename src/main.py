from flask import Flask
from flask_sqlalchemy import SQLAlchemy, event
from flask_migrate import Migrate
from config import DevConfig
import datetime

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# SQLite, por defecto no valida la existencia de claves externas, pero
# podemos forzarlo con este procedimiento
@event.listens_for(db.engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()



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
    username = db.Column(db.String(255), nullable=False, index=True, unique=True)
    password = db.Column(db.String(255))
    posts =db.relationship(
        'Post',
        backref = 'user',
        lazy = 'dynamic'
    )

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)



tags = db.Table (
    "post_tags",
    db.Column("post_id", db.Integer(), db.ForeignKey("post.id")),
    db.Column("tag_id", db.Integer(), db.ForeignKey("tag.id"))
)


class Post(db.Model):
    """ 
    Notese que se ha especificado un string como parámetro de db.ForeignKey
    ya que se podría dar la circuntancia de que no se hubiera creado todavía la 
    clase User. El valor asignado tiene que ser coincidente con el especificado
    en el parámetro backref de la relationship del objeto de clave externa.
    """
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime(), default=datetime.datetime.now)
    comments = db.relationship(
        'Comment',
        backref = 'post',
        lazy = 'dynamic'
    )
    tags = db.relationship (
        'Tag',
        secondary = tags,
        backref = db.backref('posts', lazy='dynamic')
    )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)



class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Tag '{}'>".format(self.title)



class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime(), default=datetime.datetime.now)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])



"""
user = User.query.get(1)
new_post = Post('Post Title')
new_post.user_id = user.id
db.session.add(new_post)
db.session.commit()

o también podriamos hacer:

user = User.query.get(1)
new_post = Post('Post Title')
user,posts.append(new_post)
db.session.add(user)
db.session.commit()

Podemos tratar user.posts como una lista, o como una query
user.posts.order_by(Post.publish_date.desc()).all()

Creo 3 etiquetas y guardo 2 
tag1 = Tag('tag 1')
tag2 = Tag('tag 2')
tag3 = Tag('tag 3')
db.session.add(tag1)
db.session.add(tag2)
db.session.commit()

Añado al no guardada a un post, al guardar éste, se guardará también el tag no guardado.
post2 = Post.query.get(2)
post2.tags.append(tag3)
db.session.add(post2)
db.session.commit()

"""

if __name__ == '__main__':
    app.run()
