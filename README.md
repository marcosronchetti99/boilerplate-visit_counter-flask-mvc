# Nuevo proyecto 
## Proyecto orientado a backend 
### Herramientas del proyecto

* Visual Atudio Code  
* trello 
* GitHub 

```
from flask import Flask
app = Flask(__name__)
app.config['count_visitas'] = 0

@app.route("/")
def holamundo():
    app.config['count_visitas'] = app.config['count_visitas'] + 1
    print(app.config['count_visitas'])
    return "¡Hola Mundo! Usted es la visita número " + str(app.config['count_visitas'])

# Hacemos que la función version sea un endpoint del web server
@app.route("/version/")
def version():
    v = '1.0'
    return v

if __name__ == "__main__":
    app.run()
```

> [name=marcos] estudiante 
> [name=felipe] profesor [](https:github.com/felipemoralesquerol) 

