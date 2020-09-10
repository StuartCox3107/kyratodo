import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app.config["MONGO_DBNAME"] = ("task_manager")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)