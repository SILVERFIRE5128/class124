from flask import Flask, jsonify, request
app= Flask(__name__)

tasks= [
    {
        'id':1,
        'title': u'buy groceries',
        'description': u'buy milk, cheese, fruits, chocolates',
        'done':False
    },

    {
        'id':2,
        'title': u'learn python',
        'description': u'need to find good python tutorial',
        'done':False
    }
]

@app.route('/add-data', methods= ['POST'])

def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide data'
            },400)

    task= {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False
    }

    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })

@app.route('/get-data')

def get_task():
    return jsonify({
        'data':tasks
    })

if (__name__== '__main__'):
    app.run(debug= True)