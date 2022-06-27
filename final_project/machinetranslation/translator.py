
'''Module to translate from english to french and from french to english'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['APIKEY']
URL = os.environ['URL']


authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def englishtofrench(english_text):
    '''translate word from english to french'''
    #raise exception in case of empty strings
    if english_text=="":
        raise Exception("Please enter the text you want to translate")
    model_id="en-fr"
        #translate from english to french
    french_text = language_translator.translate(
    text=english_text,
    model_id=model_id).get_result()
    return french_text

def frenchtoenglish(french_text):
    '''translate word from french to english'''
    #raise exception in case of empty strings
    if french_text=="":
        raise Exception("Please enter the text you want to translate")
    model_id="fr-en"
    #translate from english to french
    english_text = language_translator.translate(
    text=french_text,
    model_id=model_id).get_result()
    return english_text

