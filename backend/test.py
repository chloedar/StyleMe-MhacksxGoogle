from gemini import websearch, search_web
import argparse

def trigger_functions(mode, query, images=None):
    #this function calls the the correct function based off of mode
    
    if (mode == 'wardrobe'):
        pass
    else:
        resp_list, outfit_summary = websearch(query)
        var = search_web(resp_list)
        return var

    #shopping
    #sustain
    
    #web

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-i", help="input query",nargs='+',
    #                     type=str)
    # args = parser.parse_args()
    query = "I want to be styled like this link:https://www.tiktok.com/@wisdm8?lang=en"
    print(query)
    print(trigger_functions("else", query))