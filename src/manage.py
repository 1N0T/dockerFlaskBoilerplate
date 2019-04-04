from main import app, db, User

"""
export FLASK_APP=manage.py
flask shell
db.create_all()
exit()

sqlite3 database.db .tables
"""

@app.shell_context_processor
def crear_contexto_shell():
    return dict(app=app, db=db, User=User)