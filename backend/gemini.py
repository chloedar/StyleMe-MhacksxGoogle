import requests
import google.generativeai as genai

import PIL
from PIL import Image
#import PIL.Image
import os
import json

import sqlite3

# genai.configure(api_key='AIzaSyCptcp0a4vTQRzXp-HbuWwMDPgK_jN3R-s')
genai.configure(api_key=os.environ['OPENAI_API_KEY'])

sustainability_items = {
    "items": {
        "sequin top": "https://www.depop.com/products/socutevtg-y2k-mind-code-halter-tie/",
        "flare pants": "https://www.depop.com/products/sbarnes880-bear-dance-sequin-flare-pants/",
        "platform shoes": "https://www.depop.com/products/aswithin-silver-chrome-color-shifting-rainbow/",
        "sequin dress":"https://www.thredup.com/featured/154093049?department_tags=juniors&referral_code=adwords_pla%2Cadwords_pla&iv_=__iv_p_1_a_19641507037_g__c__w__n_x_d_c_v__l__t__r__x_pla_y_8908102_f_online_o_151141830_z_US_i_en_j__s__e__h_9016852_ii__gg__vi__&gclsrc=aw.ds&gad_source=4&gclid=Cj0KCQjw2uiwBhCXARIsACMvIU2aroiu_fQVENG5mcdy0sYFzsOPsADd5OxF8RmH1HQZfbd-UEOSqeYaAppqEALw_wcB&featured_item=154093049", 
        "plaid skirt": "https://www.thredup.com/featured/156281952?department_tags=women&referral_code=adwords_pla%2Cadwords_pla&iv_=__iv_p_1_a_20527315115_g__c__w__n_x_d_c_v__l__t__r__x_pla_y_8908102_f_online_o_153337624_z_US_i_en_j__s__e__h_9016852_ii__gg__vi__&gclsrc=aw.ds&gad_source=1&gclid=Cj0KCQjw2uiwBhCXARIsACMvIU04cGIfnJcTLRO2CFXmuhb3GDLbs4oUN6xVLvsv-4I1NMvFycCqy6UaAtWBEALw_wcB&featured_item=156281952", 
        "professional blazer": "https://www.thredup.com/product/women-polyester-papaya-gray-blazer/165203478?query_id=892301933850443776&result_id=892301934160822272",
        "button up shirt":"https://www.depop.com/products/miarae28-ralph-lauren-button-up-size/",
        "dress pants": "https://www.depop.com/products/doubledee12-nwt-j-crew-black-dress/",
        "dress shoes": "https://www.thredup.com/product/women-deer-stags-black-flats/163516050?query_id=892302162343616512&result_id=892302165480931328&suggestion_id=892302162414919684",
        "graphic tee": "https://www.thredup.com/product/women-polyester-jerry-leigh-apparel-black-short-sleeve-t-shirt/165080241?query_id=892302762791772160&result_id=892302764372992000&suggestion_id=892302762846298124",
        "hoodie":"https://www.depop.com/products/xvqjos-red-gap-hoodie-dont-need/",
        "sweatpants":"https://www.depop.com/products/allthingsa2z-brand-new-xs-amazon-grey/",
        "beanie":"https://www.depop.com/products/loveclover-cream-crochet-ribbed-beanie-depop/",
        "cargo pants":"https://www.depop.com/products/sdubmi-hm-cargo-pants-size/",
        "sneakers":"https://www.depop.com/products/yuhlol579-dark-green-converse-only-worn/",
        "tank top":"https://www.depop.com/products/angelikar-new-york-rhinestone-tank-top/",
        "denim jacket": "https://www.depop.com/products/tesskaardal-light-wash-jean-jacket/", 
        "cowboy boots": "https://www.depop.com/products/maasmega-faux-leather-cowboy-boots-boys/",
        "jean shorts": "https://www.depop.com/products/siennakloss20-super-super-cute-denim-jean/", 
        "plaid shirt":"https://www.depop.com/products/zayxoxzay-cute-oversized-green-plaid-button-up/", 
        "fringe dress": "https://www.depop.com/products/loloclothing1-sparkly-fringe-dress-with-feathers/", 
        "cowboy hat": "https://www.depop.com/products/kstylechoice-western-small-wire-straw-cowboy/",
        "bandana": "https://www.depop.com/products/detroit-cute-bandana/",
        "athletic shorts": "https://www.thredup.com/product/women-polyester-lululemon-athletica-gray-athletic-shorts/165366081?query_id=892306007647911936&suggestion_id=892306007706632214", 
        "sports bra":"https://www.thredup.com/product/women-lululemon-athletica-black-sports-bra/162694987?query_id=892305542264758272&result_id=892305542713548800",
        "puffer jacket":"https://www.depop.com/products/newwave_vintage-vintage-polo-ralph-lauren-brown/",
        "tennis skirt": "https://www.thredup.com/product/women-adidas-white-active-skort/165226473?query_id=892305747139723264&result_id=892305753468919808&suggestion_id=892305747206832132",
        "tennis shoes": "https://www.thredup.com/product/women-nike-gray-sneakers/162968957?query_id=892305840697843712&result_id=892305845269594112&suggestion_id=892305840752369682", 
        "leggings":"https://www.thredup.com/product/women-lululemon-athletica-black-leggings/165152653?query_id=892305542264758272&result_id=892305542713548800",
        "long pleated skirt":"https://www.depop.com/products/rewearropa-00s-red-pleated-floral-midi/",
        "short skirt":"https://www.depop.com/products/averirgcloset-tennis-skirt-pink-tennis-skirt/",
        "red cozy sweater": "https://www.depop.com/products/reisho-hm-wool-sweater-red-size/",
        "purple down jacket": "https://www.depop.com/products/jmwz-purple-patagonia-down-jacket-girls/",
        "ball gown":"https://www.depop.com/products/caileyapple-satin-plum-ball-gownbridesmaid-dress/",
        "casual dress":"https://www.depop.com/products/miss_gabbie7-floral-wrap-dress-with-side/",
        "earmuffs":"https://www.depop.com/products/_noname__-tan-earmuffs-brand-new/",
        "normal jeans":"https://www.depop.com/products/thisisdumbdotcom-womens-gray-distressed-jeans-streetwear/",
        "black jeans": "https://www.depop.com/products/a_mended-90s-guess-black-denim-jeans/",
        "floral shorts": "https://www.depop.com/products/bb_romerooo-flowy-floral-print-short-size/",
        "white shorts": "https://www.depop.com/products/linbob-white-levis-shorts/",
        "black shorts": "https://www.depop.com/products/lovecece-zara-high-waisted-mom-fit/",
        "red shirt": "https://www.thredup.com/product/women-silk-new-nexx-york-red-long-sleeve-silk-top/164348275?query_id=892307427914735616&result_id=892307434650845184&suggestion_id=892307427981844488",
        "red shorts": "https://www.thredup.com/product/women-cotton-jcrew-red-khaki-shorts/166053537?query_id=892307532877234176&result_id=892307541739765760&suggestion_id=892307532935954444", 
        "red heels": "https://www.thredup.com/product/women-michael-michael-kors-red-heels/164894668?query_id=892307700204732416&result_id=892307706441752576&suggestion_id=892307700284424192",
        "yellow beatles shirt": "https://www.depop.com/products/meowballz-the-beatles-graphic-t-shirt-no/",
        "yellow shorts": "https://www.depop.com/products/thriftylishy-hm-cottondenim-yellow-shorts-never/",
        "yellow shoes": "https://www.thredup.com/product/women-divided-by-h-and-m-yellow-sneakers/164912911?query_id=892307974252183552&result_id=892307980594012162&suggestion_id=892307974315098116",
        "green shirt":"https://www.thredup.com/product/women-cotton-jcrew-green-short-sleeve-button-down-shirt/165243375?query_id=892307828164648960&result_id=892307835869503488&suggestion_id=892307828227563520",
        "green cargo shorts": "https://www.depop.com/products/bellaaa123123-green-cargo-shorts-lightly-used/",
        "green flats":"https://www.depop.com/products/mteresaafonso-primark-green-slingback-flats/"
    }
}

# def wardrobe(query, image_folder):
#     # searches wardrobe with the images provided 
#     model = genai.GenerativeModel('gemini-pro-vision')

#     query_str = "You are a style expert giving style advice. Help form an outfit based off of the style prompt given with the images provided. If a video link is provided, analyze the video for style reference for recommendation. Style prompt:"+ query 
#     resp_list = []
#     resp_list.append(query)

#     for imag in image_folder:
#         resp_list.append(imag)

#     response = model.generate_content(resp_list, stream=True)
#     response.resolve()
#     x = response.text
#     return x


# def wardrobe_image(query, image_folder):
#     # to output images instead of text description
#     # hard-coding input images for now
#     # Install the Python SDK
#     # a = !ls '/content/drive/MyDrive/mhacksxgoogle/images_compressed/'
#     folder = 'test_images_16/' #currently hardcoded
#     i=0
#     imgs = []

#     for file in os.listdir(folder):
#         if(i<16):
#             #img = PIL.Image.open(f'{folder}{file}')
#             img = Image.open(f'{folder}{file}')
#             imgs.append(img)
#             i=i+1

#     labelled_images={}
#     img_labelling_instruction = "You are an image-labeller. I will provide you images of various items of clothing one-by-one and want you to label each image with a string of upto 3 words. Give me no output besides this label. Include no commas"
#     img_labelling_model = genai.GenerativeModel('gemini-pro-vision')

#     for i in range(16):
#         response = img_labelling_model.generate_content([img_labelling_instruction, imgs[i]])
#         print(response.text)
#         a = response.text
#         b =a.strip()
#         labelled_images[b] = imgs[i]

#     print("labels successfully generated")

#     flattened_dict = []
#     for i in labelled_images.keys():
#         flattened_dict.append(i)
#         flattened_dict.append(labelled_images[i])

#     labelled_images_16 = list(labelled_images.keys())[0:16]
#     flattened_dict_32 = flattened_dict[0:32]

#     fashion_prompt = f"""You are my best friend and a fashion expert. {query} I have attached pictures of various items from my wardrobe. Could you put together a suitable outfit for me, using only the images provided?
#     Input format: (item description 1, image 1, item description 2, image 2, ... item description n, image n). Output format: [item description a, item description b, item description c]. Please only use outputs from the list: {labelled_images_16}""" 

#     fashion_model = genai.GenerativeModel('gemini-pro-vision')
#     response = fashion_model.generate_content([fashion_prompt, *flattened_dict_32])
#     print(response.text)

#     #helper function for wardrobe_image function
#     def print_images(a: str):
#         b=a.split(', ')
#         #print(b)
#         #type(b)
#         for i in b:
#             try:
#                 i = i.strip()
#                 print(i)
#                 print(labelled_images[i])
#                 result_images.append(labelled_images[i])
#             except:
#                 pass

#     result_images = []
#     print_images(response.text)

#     return result_images

def wardrobe_integrated(query, folder='test_images_16/'):
    num_input_images = 16
    # outputs both images and text description
    # hard-coding input images for now
    # Install the Python SDK
    # a = !ls '/content/drive/MyDrive/mhacksxgoogle/images_compressed/'
    # folder = 'test_images_16/' #currently hardcoded
    i=0
    imgs = []

    #img_address_dict = {}
    for file in os.listdir(folder):
        if(i<num_input_images):
            #img = PIL.Image.open(f'{folder}{file}')
            #print(f'{folder}{file}')
            img = Image.open(f'{folder}{file}')
            #img_address_dict[file] = img
            imgs.append(img)
            # print(img)
            # print(imgs[i])
            # print(img.filename)
            i=i+1
            if(i==num_input_images):
                break

    #print(img_address_dict['denimjeans.jpg'])
            
    labelled_images={}
    img_labelling_instruction = "You are an image-labeller. I will provide you images of various items of clothing one-by-one and want you to label each image with a string of upto 3 words (no commas). Give me no output besides this label. Include no commas"
    img_labelling_model = genai.GenerativeModel('gemini-pro-vision')

    print(len(imgs))

    for i in range(num_input_images):
        response = img_labelling_model.generate_content([img_labelling_instruction, imgs[i]])
        #print(response.text)
        a = response.text
        b =a.strip()
        labelled_images[b] = imgs[i]

    print("labels successfully generated")

    flattened_dict = []
    for i in labelled_images.keys():
        flattened_dict.append(i)
        flattened_dict.append(labelled_images[i])

    labelled_images_16 = list(labelled_images.keys())[0:num_input_images]
    flattened_dict_32 = flattened_dict[0:num_input_images*2]

    fashion_prompt_2 = """Return all responses in JSON format, the JSON should include an array of items (suggested items) and a parameter that explains the overall outfit. ONLY RETURN ONE SET OF CURLY BRACES IN THE JSON.
        Example JSON: [{"suggestedItems":["red hat", "flare pants", "cowboy boots"],
            "outfitParameter": "This outfit contains a red hat and flare pants. It will look great on you!"
            }] You are my best friend and a fashion expert. %s I have attached pictures of various items from my wardrobe. Could you put together a suitable outfit for me, using only the images provided?
        Input format: (item description 1, image 1, item description 2, image 2, ... item description n, image n). Please only use exactly 3 outputs from the following list for suggestedItems: %s""" % (query, labelled_images_16)

    fashion_model_2 = genai.GenerativeModel('gemini-pro-vision')
    response = fashion_model_2.generate_content([fashion_prompt_2, *flattened_dict_32])

    
    #helper function for wardrobe_image function
    def print_images(a: str):
        #b=a.split(', ')
        #print(b)
        #type(b)
        for i in a:
            try:
                i = i.strip()
                #print(i)
                #print(labelled_images[i])
                result_images.append(labelled_images[i].filename)
            except:
                pass

    a = parse_json(response.text.strip())
    #print(type(a))
    #print(a)
    #json_object = json.loads(response.text.strip())
    #  print(type(json_object["suggestedItems"]))

    result_images = []
    #print(response.text.strip())
    #print("\n\n")
    #print(type(json_object))
    #print(len(json_object))
    #print(json_object)
    print_images(a["suggestedItems"])
    #print("\n\n\n")
    #print(a["suggestedItems"])
    #print("\n\n\n")
    #print(a["outfitParameter"])
    #print_images(json_object["suggestedItems"])

    #print(json_object["outfitParameter"])

    # this will print the word output
    # result_images is a list of jpg images that should be displayed to user
    #print(result_images)

    output_dictionary = {}
    output_dictionary["message"] = a["outfitParameter"]
    z=0
    for i in result_images:
        output_dictionary[z]=i
        z=z+1

    return output_dictionary

def sustain(style_prompt):
    # this function will search database and return links
    # have no access to apis
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    prompt = '''Return all responses in JSON format, the JSON should include an array of items with a suggested items and a parameter that explains the overall outfit. RETURN ONLY ONE SET OF CURLY BRACES IN THE JSON.
        Example JSON: [{"suggestedItems":["jean shorts", "plaid shirt", "cowboy boots"],
            "links": ["https://www.depop.com/products/siennakloss20-super-super-cute-denim-jean/", "https://www.depop.com/products/zayxoxzay-cute-oversized-green-plaid-button-up/" , "https://www.depop.com/products/maasmega-faux-leather-cowboy-boots-boys/"], 
            "outfitParameter": "Ooo have fun! This will look good. Cowboy boots are in style, pair them with denim shorts and a plaid shirt!"
            }]
        You are a style expert giving style advice. Make an outfit with the items in the indicated JSON based off of the indicated style prompt. Remember, RETURN ONLY ONE SET OF CURLY BRACES IN THE JSON. JSON: ''' + str(sustainability_items) + '''. . Style prompt: ''' + style_prompt

    response = model.generate_content(prompt, stream=True)
    response.resolve()
    print(response)

    parsed_response = parse_json(response.text)
    print(parsed_response)

    return parsed_response

    # output = parsed_response
    # suggestedItemsList = []
    # for x in output["suggestedItems"]:
    #     suggestedItemsList.append(x)

    # outfit_summary = output["outfitParameter"]

    # # print("RESP_LIST: ", suggestedItemsList)
    # # print("OUTFIT SUMMARY", outfit_summary)

    # return suggestedItemsList, outfit_summary

def search_web(query_items):
    # this function returns a list of links related to the items returned from gemini 
    list_links = {}
    for item in query_items:
        # list_links[item] = []
        item_str = item.replace(" ", "+")
        # print("ITEM STR:", item_str, "\n\n")
        resp = requests.get(f'https://www.googleapis.com/customsearch/v1?key=AIzaSyAnBvRr6Cy_OSRBXzmI0rtXn88FWXFFJmg&cx=f1eba0467912b4a28&q={item_str}')
        links = resp.json()
        # for key in links:
        #     print(key,":", links[key]) 
        list_links[item] = links["items"][0]["link"]
    return list_links

def websearch(query, image_folder=None):
    """Query Gemini."""
    # searches web for new outfit
    if (image_folder):
        model = genai.GenerativeModel('gemini-pro-vision')
    else:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
    # chat history
    # chat = model.start_chat(history=[])
    queryy = '''Return all responses in JSON format, the JSON should include an array of items with a suggested items and a parameter that explains the overall outfit. RETURN ONLY ONE SET OF CURLY BRACES IN THE JSON.
        Example JSON: [{'suggestedItems':["red hat", "flare pants", "cowboy boots"],
            "outfitParameter": "Ooo have fun! This will look good Cowboy boots are in style, pair them with flare pants!"
            }]
        You are a style expert giving style advice. If a link is provided, analyze the link for style reference for recommendation. Help form an outfit based off of the style prompt given and the images if provided. Remember, RETURN ONLY ONE SET OF CURLY BRACES IN THE JSON. Style prompt: '''
    # if video == True:

    # queryy = '''The previous text was the style prompt. You are a style expert giving style advice. If a video link was provided, analyze the video for style reference for recommendation. Help form an outfit based off of the style prompt given and the images if provided. 
    #         Return all responses in JSON format, the JSON should include an array of items with a suggested items and a parameter that explains the overall outfit. 
    #         Example JSON: [{'suggestedItems':["red hat", "flare pants", "cowboy boots"],
    #          "outfitParameter": "Ooo have fun! This will look good Cowboy boots are in style, pair them with flare pants!"
    #          }]'''
    # queryy = '''Format the following input into a JSON format.'''
    # TODO: defend against prompt injection
    # print(query, queryy)
    query_str = queryy + query # + query
    # print(query_str)
    resp_list = []
    resp_list.append(query_str)

    if image_folder:
        for imag in image_folder:
            resp_list.append(imag)

    response = model.generate_content(resp_list, stream=True)
    response.resolve()
    # print("RESPONSE: ", response.text)
    parsed_response = parse_json(response.text)
    # print("PARSED RESPONSE: ", parsed_response)
    output = parsed_response #.json()

    suggestedItemsList = []
    for x in output["suggestedItems"]:
        suggestedItemsList.append(x)

    outfit_summary= output["outfitParameter"]

    # print("RESP_LIST: ", suggestedItemsList)
    # print("OUTFIT SUMMARY", outfit_summary)

    return suggestedItemsList, outfit_summary

def parse_json(input_json):
    opening_brace_index = input_json.find('{')
    closing_brace_index = input_json.rfind('}')
    print(len(input_json))
    print(closing_brace_index)
    input_json = input_json[opening_brace_index:closing_brace_index + 1]
    print(input_json)
    output = json.loads(input_json)
    for x in output["suggestedItems"]:
        print(x)
    return output

def main():
    parse_json("""```json
[
  {
    "suggestedItems": [
      "Sequin jumpsuit or dress",
      "Platform shoes",
      "Metallic accessories (belt, earrings, necklace)",
      "Glitter eyeshadow and bold lipstick"
    ],
    "outfitParameter": "Embrace the glitz and glam of disco with a sequin jumpsuit or dress that catches the light with every move. Elevate your look with platform shoes for a groovy touch, and add metallic accessories for extra shine. Don't forget the glitter eyeshadow and bold lipstick to complete your dazzling disco ensemble."
  },
  {
    "suggestedItems": [
      "Wrap dress in a bold color or print",
      "High-heeled sandals or boots",
      "Statement jewelry",
      "Feathered hair accessory"
    ],
    "outfitParameter": "Channel your inner disco diva with a wrap dress in a vibrant color or eye-catching print. Pair it with high-heeled sandals or boots for a touch of sophistication, and accessorize with statement jewelry for a glamorous flair. Add a feathered hair accessory for a playful and whimsical touch."
  },
  {
    "suggestedItems": [
      "Wide-leg pants or flared jeans",
      "Crop top or halter top",
      "Chunky platform sandals",
      "Headscarf or headband"
    ],
    "outfitParameter": "Get groovy with wide-leg pants or flared jeans that allow for freedom of movement on the dance floor. Pair them with a crop top or halter top to show off some skin, and complete the look with chunky platform sandals for a retro vibe. Add a headscarf or headband for a stylish finishing touch."
  }
]
```""")

if __name__ == "__main__":
    main()