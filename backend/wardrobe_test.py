from gemini import wardrobe, websearch, wardrobe_integrated
import argparse


def trigger_functions(mode, query, images=None):
    #this function calls the the correct function based off of mode
    if (mode == 'wardrobe'):
        response = wardrobe_integrated(query)
        print("successfully called wardrobe integrated")
        for i in response:
            print(i)
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


    print(trigger_functions('wardrobe', args.i[0]))