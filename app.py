#!flask/bin/python
import os
from flask import Flask, jsonify, url_for, json, request

app = Flask(__name__)

@app.route('/results', methods=['GET'])
def getResults():
    #read results.json from file
    fname = os.path.expanduser("~/Desktop/finishLine/ThwackTimingGateServer/data/results.json")
    with open(fname, mode='r') as feedsjson:
        data = json.load(feedsjson)

    #print(data)	#print fetched data for debugging

    #respond to GET request with json formatted results
    return jsonify(data)

@app.route('/idTable', methods=['GET'])
def getTable():
    fname = os.path.expanduser("~/Desktop/finishLine/ThwackTimingGateServer/data/table.json")
    with open(fname, mode='r') as tablejson:
        data = json.load(tablejson)

    print(data) #print fetched data for debugging

    #respond to GET request with json formatted results
    return jsonify(data)

@app.route('/idTable', methods=['POST'])
def setTable():
    fname = os.path.expanduser("~/Desktop/finishLine/ThwackTimingGateServer/data/table.json")

    data = request.get_json(force=True) #print fetched data for debugging
    print(data)

    with open(fname, mode='w') as f:
        f.write(json.dumps(data, indent=4))

    return 'OK'

if __name__ == '__main__':
	app.run(debug=True)
