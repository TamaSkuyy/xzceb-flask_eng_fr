"""This module provides functions for translating text between languages
using the IBM Watson Language Translator."""

import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):
    """Translate text from English to French."""
    if english_text is None:
        return None
    translation_result = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation_result['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translate text from French to English."""
    if french_text is None:
        return None
    translation_result = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation_result['translations'][0]['translation']
    return english_text
