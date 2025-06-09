from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime

# Ici nous créons des instances de l'application et de l'API 
app = Flask(__name__)
api = Api(app)

# Ici, nous créons une classe qui réagira lorsque l'API sera requêtée. Cette classe hérite de la classe "Resource" que nous avons importée.
# La fonction "get" est la fonction par défaut lorsque nous requêtons une API.
# Ici elle retournera systématiquement un dictionnaire, toujours identique.
class my_API_class(Resource):
    def get(self, forname, lastname):
        now=datetime.now()
        sentence = 'Hi ' + forname + ', welcome in my API' 
        Date = now.strftime("%d/%m/%Y %H:%M:%S")
        sentence = 'Hi ' + forname + ' ' + lastname + ', welcome in my API on ' + Date  
        return {'hello'  : sentence}

class my_API_class1(Resource):
    def get(self, adresse):
        now=datetime.now()
        sentence1 = adresse 
        Date = now.strftime("%d/%m/%Y %H:%M:%S")
        sentence1 = sentence1 + ' ' + "at" + Date  
        return {sentence1}
    
# Nous devons ensuite ajouter la ressource à notre classe
api.add_resource(my_API_class, '/<string:forname>''/<string:lastname>' )

api.add_resource(my_API_class1, '/<string:adresse>')




# L'API sera lancée ici dans le script. Pour l'instant, tu peux laisser l'argument debug = True
if __name__ == '__main__':
    app.run(debug=True)

