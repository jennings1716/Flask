from flask import Flask,request
from flask_restplus import Api,Resource,fields
import pymongo
from pymongo import MongoClient
flask_app = Flask(__name__)
app = Api(app=flask_app)


model = app.model('Name Model',
                              {
                                "name":fields.String(required=True,description="Name:")
                              })
database = {"1":"first","2":"second","3":"third"}

@app.route('/hello')
class MainClass(Resource):
    def get(self):
        print("GET CALL")
        return {"status":"got new data"}

    def post(self):
        print(request)
        return {
                    "status":request.json['name']
                }
 
@app.route('/<string:todo_id>')
class TodoClass(Resource):
    def get(self,todo_id):
        print(todo_id)
        return {
                    "result":database[todo_id]
                }

    def post(self,todo_id):
        print(todo_id)
        database[todo_id]=request.json['name']
        print("type",request.json)
        post_id= collection.insert_one(request.json).inserted_id
        if post_id:
            return {
                        "result":request.json['name']+"data entered"
                    }
        else:
            return {"result":"err"}

if __name__=='__main__':
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.users
    collection = db.users
    flask_app.run()
