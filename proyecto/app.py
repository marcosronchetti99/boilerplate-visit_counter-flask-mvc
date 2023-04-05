from flask import Flask
app = Flask(_name_)
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

if _name_ == "_main_":
    app.run()
