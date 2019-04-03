![logo](https://raw.github.com/1N0T/images/master/global/1N0T.png)

# dockerFlaskBoilerplate
Plantilla de container con aplicación Flask

Hay un bug en pip en Ubuntu que coloca una versión incorrecta a pkg-resources. 
Como workarround.
```
pip3 freeze | grep -v "pkg-resources" > requirements.txt
```

Para generar el container:
```
sudo docker build -t flask .
```

Para ejecutar la imagen generada
```
sudo docker run --rm -d -p 5000:8000 flask
```

Para interactuar con la aplicación.
```
export FLASK_APP=main.py
source venv/bin/activate
```

Podemos ejecutar la aplicación con:
```
flask run
```

Podemos interactuar con la  aplicación con:
```
flask shell
```
