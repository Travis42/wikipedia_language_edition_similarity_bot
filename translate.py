#!python3

# -*- coding: utf-8 -*-
import configparser
import os, requests, uuid, json

from utils import chunkstring, read_txt_to_string_in_chunks, write_string_to_txt_file

# https://docs.microsoft.com/en-us/azure/cognitive-services/Translator/quickstart-translate?pivots=programming-language-python


def translate(text):
    # grab MS credentials:
    config = configparser.ConfigParser()
    config.read("config.cnf")
    subscription_key = config.get('Translation', 'API_key')
    endpoint = config.get('Translation', 'endpoint_url')


    path = '/translate?api-version=3.0'
    params = '&to=en'
    constructed_url = endpoint + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    translated_text = ''
    for chunk in chunkstring(text):
        text_to_translate = [{
                            'text': chunk
                            }]
        # post request
        request = requests.post(constructed_url, headers=headers, json=text_to_translate)
        response = request.json()
        try:
            translated_text += json.loads(
                              json.dumps(
                                         response, 
                                         sort_keys=True, 
                                         indent=4, 
                                         ensure_ascii=False, 
                                         separators=(',', ': ')))[0]['translations'][0]['text']
        except KeyError: # doesn't seem to be critical.
            print('skipping these many characters: ', len(chunk))
            print('keyerror, whatever that means.')
            continue
    return translated_text


'''
# example output from endpoint:
[
    {
        "detectedLanguage": {
            "language": "en",
            "score": 1.0
        },
        "translations": [
            {
                "text": "Hallo Welt!",
                "to": "de"
            },
            {
                "text": "Salve, mondo!",
                "to": "it"
            }
        ]
    }
]
'''