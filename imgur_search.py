from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from imgurpython import ImgurClient
from random import randint

client_id = '3858e09e11ce18d'
client_secret = 'fd9ce9914d9e98815f9dda6af65f1cd2623c2dad'

app = Flask(__name__)
api = Api(app)

def getUrl(query):
    client = ImgurClient(client_id, client_secret)
    items = client.gallery_search(query, advanced=None, sort='time', window='all', page=0)
    random = randint(0, len(items))

    if len(items) == 0:
        url = None
    else:
        url = items[random].link
    return url


class ImgurSearch(Resource):
    def get(self, query):
        return getUrl(query)


class CatPic(Resource):
    def get(self):
        return getUrl('cats')


api.add_resource(ImgurSearch, '/<string:query>')
api.add_resource(CatPic, '/')

if __name__ == '__main__':
    app.run(debug=True)
