import requests

def wardrobe(query, image_folder):
    model = genai.GenerativeModel('gemini-pro-vision')
    chat = model.start_chat(history=[])

    query_str = "You are a style expert giving style advice. Help form an outfit based off of the style prompt given with the images provided. If a video link is provided, analyze the video for style reference for recommendation. Style prompt:"+ query 
    resp_list = []
    resp_list.append(query)

    for imag in image_folder:
        resp_list.append(image)

    response = model.generate_content(resp_list, stream=True)
    response.resolve()

    return to_markdown(response.text)

def sustain(query_item):
    # this function will search database and return links
    # have no access to apis
    curse = styleme.model.get_db()
    split_li = query_item.split()
    list_links =[]
    for item in split_li: 
        cur = curse.execute('''SELECT itemname, productlink from sustain 
                            WHERE itemname = ? ''', (item))
        list_links.append(cur.fetchall())
    return list_items
def search_web(query_item):
    # this function returns a list of links related to the items returned from gemini 
    list_links = []
    for item in query_item:
        item_str = item.replace(" ", "+")
        resp = requests.get(f'https://www.googleapis.com/customsearch/v1?key=...&cx=f1eba0467912b4a28&q={item_str}')
        list_links.append(resp)

def websearch(query, image=None):
    model = genai.GenerativeModel('gemini-pro-vision')
    # chat history
    # chat = model.start_chat(history=[])
    queryy = '''Return all responses in JSON format, the JSON should include an array of items with a suggested items and a parameter that explains the overall outfit. 
        Example JSON: [{'suggestedItems':[],
            "outfitParameter": ""
            }]
        You are a style expert giving style advice. If a video link is provided, analyze the video for style reference for recommendation. Help form an outfit based off of the style prompt given and the images if provided: '''
    query_str = queryy+ query 
    resp_list = []
    resp_list.append(query)

    if image:
        for imag in image_folder:
            resp_list.append(image)

    response = model.generate_content(resp_list, stream=True)
    response.resolve()
    output = to_markdown(response.text)


