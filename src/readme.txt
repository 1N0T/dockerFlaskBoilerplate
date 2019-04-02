Hay un bug en pip en Ubuntu que coloca una versión incorrecta a pkg-resources. 
Como workarround.

pip3 freeze | grep -v "pkg-resources" > requirements.txt

sudo docker build -t flask .
sudo docker run --rm -d -p 5000:8000 flask
