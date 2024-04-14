from gemini import websearch, wardrobe_integrated
import argparse
import requests
import google.generativeai as genai

import PIL
from PIL import Image
#import PIL.Image
import os
import json

import sqlite3

genai.configure(api_key=os.environ['OPENAI_API_KEY'])

# def parse_json(input_json):
#     opening_brace_index = input_json.find('{')
#     closing_brace_index = input_json.rfind('}')
#     print(len(input_json))
#     print(closing_brace_index)
#     input_json = input_json[opening_brace_index:closing_brace_index + 1]
#     print(input_json)
#     output = json.loads(input_json)
#     for x in output["suggestedItems"]:
#         print(x)
#     return output

# def wardrobe_integrated(query, folder='test_images_16/'):
#     num_input_images = 16
#     # outputs both images and text description
#     # hard-coding input images for now
#     # Install the Python SDK
#     # a = !ls '/content/drive/MyDrive/mhacksxgoogle/images_compressed/'
#     # folder = 'test_images_16/' #currently hardcoded
#     i=0
#     imgs = []

#     #img_address_dict = {}
#     for file in os.listdir(folder):
#         if(i<num_input_images):
#             #img = PIL.Image.open(f'{folder}{file}')
#             #print(f'{folder}{file}')
#             img = Image.open(f'{folder}{file}')
#             #img_address_dict[file] = img
#             imgs.append(img)
#             # print(img)
#             # print(imgs[i])
#             # print(img.filename)
#             i=i+1
#             if(i==num_input_images):
#                 break

#     #print(img_address_dict['denimjeans.jpg'])
            
#     labelled_images={}
#     img_labelling_instruction = "You are an image-labeller. I will provide you images of various items of clothing one-by-one and want you to label each image with a string of upto 3 words (no commas). Give me no output besides this label. Include no commas"
#     img_labelling_model = genai.GenerativeModel('gemini-pro-vision')

#     print(len(imgs))

#     for i in range(num_input_images):
#         response = img_labelling_model.generate_content([img_labelling_instruction, imgs[i]])
#         #print(response.text)
#         a = response.text
#         b =a.strip()
#         labelled_images[b] = imgs[i]

#     print("labels successfully generated")

#     flattened_dict = []
#     for i in labelled_images.keys():
#         flattened_dict.append(i)
#         flattened_dict.append(labelled_images[i])

#     labelled_images_16 = list(labelled_images.keys())[0:num_input_images]
#     flattened_dict_32 = flattened_dict[0:num_input_images*2]

#     fashion_prompt_2 = """Return all responses in JSON format, the JSON should include an array of items (suggested items) and a parameter that explains the overall outfit. ONLY RETURN ONE SET OF CURLY BRACES IN THE JSON.
#         Example JSON: [{"suggestedItems":["red hat", "flare pants", "cowboy boots"],
#             "outfitParameter": "This outfit contains a red hat and flare pants. It will look great on you!"
#             }] You are my best friend and a fashion expert. %s I have attached pictures of various items from my wardrobe. Could you put together a suitable outfit for me, using only the images provided?
#         Input format: (item description 1, image 1, item description 2, image 2, ... item description n, image n). Please only use exactly 3 outputs from the following list for suggestedItems: %s""" % (query, labelled_images_16)

#     fashion_model_2 = genai.GenerativeModel('gemini-pro-vision')
#     response = fashion_model_2.generate_content([fashion_prompt_2, *flattened_dict_32])

    
#     #helper function for wardrobe_image function
#     def print_images(a: str):
#         #b=a.split(', ')
#         #print(b)
#         #type(b)
#         for i in a:
#             try:
#                 i = i.strip()
#                 #print(i)
#                 #print(labelled_images[i])
#                 result_images.append(labelled_images[i].filename)
#             except:
#                 pass

#     a = parse_json(response.text.strip())
#     #print(type(a))
#     #print(a)
#     #json_object = json.loads(response.text.strip())
#     #  print(type(json_object["suggestedItems"]))

#     result_images = []
#     #print(response.text.strip())
#     #print("\n\n")
#     #print(type(json_object))
#     #print(len(json_object))
#     #print(json_object)
#     print_images(a["suggestedItems"])
#     #print("\n\n\n")
#     #print(a["suggestedItems"])
#     #print("\n\n\n")
#     #print(a["outfitParameter"])
#     #print_images(json_object["suggestedItems"])

#     #print(json_object["outfitParameter"])

#     # this will print the word output
#     # result_images is a list of jpg images that should be displayed to user
#     #print(result_images)

#     output_dictionary = {}
#     output_dictionary["message"] = a["outfitParameter"]
#     z=0
#     for i in result_images:
#         output_dictionary[z]=i
#         z=z+1

#     return output_dictionary


def trigger_functions(mode, query, images=None):
    #this function calls the the correct function based off of mode
    if (mode == 'wardrobe'):
        response = wardrobe_integrated(query)
        print("successfully called wardrobe integrated")
        print(response)
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