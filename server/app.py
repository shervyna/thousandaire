from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
import time

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

alpha_list = [
    {
        'id': uuid.uuid4().hex,
        'description': 'some explanation',
        'author': 'AAA',
        'settings':'setting A',
        'formula': 'formula A',
        'submitted': True,
    },
    {
         'id': uuid.uuid4().hex,
        'description': 'some explanation 2',
        'author': 'BBB',
        'settings':'setting B',
        'formula': 'formula B',
        'submitted': True,
    },
    {
        'id': uuid.uuid4().hex,
        'description': 'some explanation 3',
        'author': 'CCC',
        'settings':'setting C',
        'formula': 'formula C',
        'submitted': False,
    }
]

@app.route('/alpha', methods=['GET', 'POST'])
def all_alphas():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        alpha_list.append({
            'id': uuid.uuid4().hex,
            'description': post_data.get('description'),
            'author': post_data.get('author'),
            'settings':post_data.get('settings'),
            'formula': post_data.get('formula'),
            'submitted': False,
        })
        response_object['message'] = 'alpha added!'
    else:
        response_object['alphas'] = alpha_list
    return jsonify(response_object)

@app.route('/alpha/<alpha_id>', methods=['GET', 'PUT', 'DELETE'])
def single_alpha(alpha_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        return_alpha = ''
        for alpha in alpha_list:
            if alpha['id'] == alpha_id:
                return_alpha = alpha
        response_object['alpha'] = return_alpha
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_alpha(alpha_id)
        alpha_list.append({
            'id': uuid.uuid4().hex,
            'description': post_data.get('description'),
            'author': post_data.get('author'),
            'settings':post_data.get('settings'),
            'formula': post_data.get('formula'),
            'submitted': False,
        })
        response_object['message'] = 'alpha updated!'
    if request.method == 'DELETE':
        remove_alpha(alpha_id)
        response_object['message'] = 'alpha removed!'
    return jsonify(response_object)

def remove_alpha(alpha_id):
    for alpha in alpha_list:
        if alpha['id'] == alpha_id:
            alpha_list.remove(alpha)

if __name__ == '__main__':
    app.run()