from flask import Flask, request
from flask_restful import Resource, Api
import redis
import os
app = Flask(__name__)
api = Api(app)

jobs = {}

@app.route("/", methods=['POST'])
def publishJobs():
    job=request.form.to_dict()
    #print(request.form['redis'])
    connection = redis.StrictRedis(host=os.environ.get('REDIS_SERVER'), port=6379, db=0)
    #connection.publish('jobs', json.loads(jobs[job_id]))
    connection.publish(os.environ.get('CHANNEL'), job)
    return str(job)

if __name__ == '__main__':
    app.run(debug=True)
