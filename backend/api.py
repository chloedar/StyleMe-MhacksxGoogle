from gemini import wardrobe_integrated, websearch, search_web, sustain
import flask
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

# will be a flask route
# @app.route()
# def receive_user_input():
#     pass

@app.route('/outfit/', methods=['POST'])
def trigger_functions(images=None):
    print("inside trigger_functions")
    mode = flask.request.json.get('mode')
    query = flask.request.json.get('query')

    # for key in flask.request.json:
    #     print(key)

    print("got mode and query")
    print("mode: ", mode)
    print("query", query)

    #this function calls the the correct function based off of mode
    try:
        if (mode == 'wardrobe'):
            response = wardrobe_integrated(query)
            print("successfully called wardrobe integrated")
            for i in response:
                print(i)
        else:
            print("calling websearch")
            resp_list, outfit_summary = websearch(query)
            # print("RESP LIST IN API.PY:", resp_list)
            # print("OUTFIT SUMMARY IN API.PY:", outfit_summary)
            # print("successfully called websearch")
            if (mode == 'search_web'):
                print("calling search_web")
                list_links = search_web(resp_list)
                print("LIST LINKS: ", list_links)
                return list_links
            else:
                print("IN SUSTAIN MODE")
                json_output = sustain(query)
                print("JSON OUTPUT", json_output)
                return json_output
    except BaseException as e:
        print(e)
        flask.abort(500, 'Something went wrong. Please try again.')
    #shopping
    #sustain
    
    #web

if __name__ == "__main__":
    app.run()