from main import app, db, User, Post, Comment, Tag, migrate
from sqlalchemy.sql.expression import not_, or_

"""
export FLASK_APP=manage.py
flask shell
db.create_all()
exit()

sqlite3 database.db .tables

user = User(username='Toni')
db.session.add(user)
db.session.commit()

users = User.query.all()
users
    [<User 'Toni'>]

users = User.query.limit(10).all()
users = User.query.order_by(User.username).all()
users = User.query.order_by(User.username.desc()).all()
user = User.query.first()
user.username 
    'Toni'

Acceso por primary key
user = User.query.get(1)

Paginaciones (primera de paginas de 10 elementos)
paginas = User.query.paginate(1, 10)
paginas.pages            (Número de páginas)
paginas.page             (Página actual)
paginas.has_prev         (True si existe página previa)
paginas.has_next         (True si existe página siguiente)
paginas.items            (lista de registros iterable con for)
paginas = paginas.next() (Para obtener la página siguiente, si no existe permanece en la actual)
paginas = paginas.prev() (Para obtener la página anterior, si no existe permanece en la actual)

Filtros
users = User.query.filter_by(username='Toni').all()
users = User.query.order_by(User.username.desc()).filter_by(username='Toni').limit(2).all()
user = User.query.filter(User.id > 1).all()


from sqlalchemy.sql.expression import not_, or_
user = User.query.filter(User.username.in_(['Toni']), User.password == None).first()
user = User.query.filter(not_(User.password == None)).first()
user = User.query.filter(or_(not_(User.password == None), User.id >= 1)).first()

Actualizaciones
User.query.filter_by(username='Toni').update({'password': 'test'})
db.session.commit()

Borrado
user = User.query.filter_by(username='Paula').first()
db.session.delete(user)
db.session.commit()

Para inicializar repositorio migrate
export FLASK_APP=manage.py
flask db init

El siguiente comando guarda la estructura actual 
flask db migrate -m "Versión inicial"

El siguiente comando muestra los comandos DDL para generarlo
flask db upgrade --sql

Para actualizar la estructura
flask db upgrade

Para volver a una versión anterior
flask db downgrade 7ded34bc4fb

"""

@app.shell_context_processor
def crear_contexto_shell():
    return dict(
        app=app, 
        db=db, 
        User=User,
        Comment=Comment,
        Post=Post,
        Tag=Tag,
        migrate=migrate
    )