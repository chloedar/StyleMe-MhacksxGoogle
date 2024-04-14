from gemini import wardrobe, websearch, search_web, sustain
import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# will be a flask route
# @app.route()
# def receive_user_input():
#     pass

@app.route('/outfit/', methods=['POST'])
def trigger_functions(images=None):
    mode = flask.request.form.get('mode')
    query = flask.request.form.get('query')

    #this function calls the the correct function based off of mode
    try:
        if (mode == 'wardrobe'):
            response = wardrobe_integrated(query)
            print("successfully called wardrobe integrated")
            for i in response:
                print(i)
            pass
        else:
            resp_list, outfit_summary = websearch(query)
            # print("RESP LIST IN API.PY:", resp_list)
            # print("OUTFIT SUMMARY IN API.PY:", outfit_summary)
            # print("successfully called websearch")
            if (mode == 'search_web'):
                list_links = search_web(resp_list)
                print("LIST LINKS: ", list_links)
            else:
                print("IN SUSTAIN MODE")
                json_output = sustain(query)
                print("JSON OUTPUT", json_output)
    except:
        flask.abort(500, 'Something went wrong. Please try again.')

    #shopping
    #sustain
    
    #web

if __name__ == "__main__":
    app.run()