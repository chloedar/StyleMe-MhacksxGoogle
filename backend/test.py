from gemini import wardrobe, websearch
import argparse

def trigger_functions(mode, query, images=None):
    #this function calls the the correct function based off of mode
    print(query)
    if (mode == 'wardrobe'):
        pass
    else:
        response = websearch(query)
        print("successfully called websearch")

    #shopping
    #sustain
    
    #web

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input query",nargs='+',
                        type=str)
    args = parser.parse_args()

    print(trigger_functions("else", str(args.i[0])))