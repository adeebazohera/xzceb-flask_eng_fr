"""Module using MyMemory translator to convert english to french and french to english"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Function to convert english text to french"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Function to convert french text to english"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
