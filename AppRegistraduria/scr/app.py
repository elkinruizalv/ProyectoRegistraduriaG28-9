from flask import Flask
from config import config
import routes.partidos as rp
import routes.candidatos as rc
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
app.add_url_rule('/partidos', 'find_partidos', rp.find_partidos)
app.add_url_rule('/partidos/<partido_id>', 'find_partido', rp.find_partido)
app.add_url_rule('/partidos', 'insert_partido', rp.insert_partido, methods= ['POST'])
app.add_url_rule('/partidos/<partido_id>', 'update_partido', rp.update_partido, methods= ['PUT'])
app.add_url_rule('/partidos/<partido_id>', 'delete_partido', rp.delete_partido, methods= ['DELETE'])

# Candidato
app.add_url_rule('/', 'index', index)
app.add_url_rule('/candidatos', 'find_candidatos', rc.find_candidatos)
app.add_url_rule('/candidatos/<candidato_id>', 'find_candidato', rc.find_candidatos)
app.add_url_rule('/candidatos', 'insert_candidato', rc.insert_candidato, methods= ['POST'])
app.add_url_rule('/candidatos/<candidato_id>', 'update_candidato', rc.update_candidato, methods= ['PUT'])
app.add_url_rule('/candidatos/<candidato_id>', 'delete_candidato', rc.delete_candidato, methods= ['DELETE'])

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()