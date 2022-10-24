from flask import Flask
from config import config
import routes.partidos as re
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_HOST'] = config['MONGO_URI']
db = MongoEngine()
db.init_app(app)

#Index
@app.route('/')
def index():
    return "<h1>Hola, bienvenidos a la registraduría Módulo Votaciones</h1>"

#routes
# Partido
app.add_url_rule('/', 'index', index)
app.add_url_rule('/partidos', 'find_partidos', re.find_partidos)
app.add_url_rule('/partidos/<partido_id>', 'find_partido', re.find_partido)
app.add_url_rule('/partidos', 'insert_partido', re.insert_partido, methods= ['POST'])
app.add_url_rule('/partidos/<partido_id>', 'update_partido', re.update_partido, methods= ['PUT'])
app.add_url_rule('/partidos/<partido_id>', 'delete_partido', re.delete_partido, methods= ['DELETE'])

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()