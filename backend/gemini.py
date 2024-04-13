import requests



def wardrobe(query, image_folder):

    model = genai.GenerativeModel('gemini-pro-vision')
    chat = model.start_chat(history=[])
    query_str = ""+ query 
    resp_list = []
    resp_list.append(query)

    for image in image_folder:
        resp_list.append(image)

    response = model.generate_content(resp_list, stream=True)
    response.resolve()

    return to_markdown(response.text)