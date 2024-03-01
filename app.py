from flask import Flask, request, make_response
import pickle


app = Flask(__name__)

def load_tests():
    import test_a1
    
    avail_tests = {}

    for i in dir(test_a1):
        if i.startswith('test'):            
            avail_tests[i] = getattr(test_a1, i)

    return avail_tests


@app.route("/test", methods=['POST'])
def test():

    avail_tests = load_tests()
    function = pickle.loads(request.data)
    tester = avail_tests.get(f"test_{function.__name__}")
    
    if tester:
        status = tester(function)
        return {'status': status}
    
    return make_response('Invalid test', 400)

if __name__ == "__main__":
    app.run(host='localhost')