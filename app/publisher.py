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

'''
class PublishJobs(Resource):

    def put(self, job_id):
        jobs[job_id] = request.form['data']
        #print(request.form['redis'])
        connection = redis.StrictRedis(host=os.environ.get('REDIS_SERVER'), port=6379, db=0)
        #connection.publish('jobs', json.loads(jobs[job_id]))
        connection.publish(os.environ.get('CHANNEL'), jobs[job_id])
        return {job_id: jobs[job_id]}

api.add_resource(PublishJobs, '/<string:job_id>')
'''


if __name__ == '__main__':
    app.run(debug=True)