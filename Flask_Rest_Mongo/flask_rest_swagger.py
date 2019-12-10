from flask import Flask,request
from flask_restplus import Api,Resource,fields

flask_app = Flask(__name__)
flask_app.config.SWAGGER_UI_OAUTH_APP_NAME = 'Calculator'

app = Api(app=flask_app,
title=flask_app.config.SWAGGER_UI_OAUTH_APP_NAME,
description='A sample Calculator API',
)

name_space = app.namespace('/', description='Basic Arithmetics')
resource_fields = name_space.model('Integer', {
    'a': fields.Integer,
    'b': fields.Integer,
})

@name_space.route('/sum')
@name_space.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
class Sum(Resource):
    @name_space.doc(body=resource_fields)
    def post(self):
        answer = request.json['a'] + request.json['b']
        return {
                    "answer":answer
                }
 
@name_space.route('/subtract')
@name_space.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' } )
class Subtract(Resource):
    @name_space.doc(body=resource_fields)
    def post(self):
        answer = request.json['a'] - request.json['b']
        return {
                    "answer":answer
                }
            

if __name__=='__main__':
    flask_app.run()
