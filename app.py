import os
from flask import Flask, request, make_response
from importlib import import_module
import pickle
import inspect


app = Flask(__name__)

def load_tests(test_module):
    
    module = import_module(test_module)
    members = inspect.getmembers(module, inspect.isfunction)
    return {member[0]: member[1] for member in members}

@app.route("/hello")
def hello():
    return "hello world"

@app.route("/test/<to_test>", methods=['POST'])
def test(to_test):

    test_module = f"test_{to_test}"

    if not os.path.exists(f'./{test_module}.py'):
        return make_response('Wrong assignment/lab', 400)


    avail_tests = load_tests(f'{test_module}')
    
    try:
        function = pickle.loads(request.data)
    except:
        return make_response('Invalid function', 400)

    tester = avail_tests.get(f"test_{function.__name__}")
    
    if tester:
        status = tester(function)
        return {'status': status}
    
    return make_response('Invalid function', 400)


if __name__ == "__main__":
    app.run(host='localhost')