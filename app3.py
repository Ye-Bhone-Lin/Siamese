import re
from typing import Dict, Any
import streamlit as st
class BurmeseConverter:
    def __init__(self):
        self.font_dictionary = {
                    '္': '်', '်': 'ျ', 'ျ': 'ြ', 'ြ': 'ွ', 'ွ': 'ှ', 'ႆ': 'ဿ', 'ဳ': 'ု', 'ဴ': 'ူ', 'ဿ': 'ူ',
                    '၀': 'ဝ', '၎': '၎င်း', 'ၚ': 'ါ်', 'ၠ': '္က', 'ၡ': '္ခ', 'ၢ': '္ဂ', 'ၣ': '္ဃ', 'ၥ': '္စ',
                    'ၦ': '္ဆ', 'ၧ': '္ဆ', 'ၨ': '္ဇ', 'ၩ': '္ဈ', 'ၪ': 'ဉ', 'ၫ': 'ည', 'ၬ': '္ဋ', 'ၭ': '္ဌ',
                    'ၮ': 'ဍ္ဍ', 'ၯ': 'ဍ္ဎ', 'ၰ': '္ဏ', 'ၱ': '္တ', 'ၲ': '္တ', 'ၳ': '္ထ', 'ၴ': '္ထ', 'ၵ': '္ဒ',
                    'ၶ': '္ဓ', 'ၷ': '္န', 'ၸ': '္ပ', 'ၹ': '္ဖ', 'ၺ': '္ဗ', 'ၻ': '္ဘ', 'ၼ': '္မ', 'ၽ': 'ျ',
                    'ၾ': 'ြ', 'ၿ': 'ြ', 'ႀ': 'ြ', 'ႁ': 'ြ', 'ႂ': 'ြ', 'ႃ': 'ြ', 'ႄ': 'ြ', 'ႅ': '္လ', 'ႇ': 'ှ',
                    'ႈ': 'ှု', 'ႉ': 'ှူ', 'ႊ': 'ွှ', 'ႎ': 'ိံ', 'ႏ': 'န', '႐': 'ရ', '႑': 'ဏ္ဍ', '႒': 'ဋ္ဌ',
                    '႓': '္ဘ', '႔': '့', '႕': '့', '႖': '္တွ', '႗': 'ဋ္ဋ', 'ၤ': 'င်္'
                }
        
    def burmese_to_romanization(self, text: str) -> str:
        """
        Convert Burmese text to Romanized form.
        
        :param text: Burmese text input
        :return: Romanized text output
        """
        burmese_to_roman: Dict[str, str] = {
        'က': 'k', 'ခ': 'K', 'ဂ': 'g', 'ဃ': 'G', 'င': 'c', "၏": "E", "၍": "rx", "၌": "Nx", "င်္": "f",
        'စ': 's', 'ဆ': 'S', 'ဇ': 'z', 'ဈ': 'Z', "ဉ": "q", 'ည': 'Q', "ဋ": "tx", "ဌ": "Tx", "ဍ": "dx", "ဎ": "Dx", "ဏ": "nx",
        "ရ": "r", "ဓ": "D", "တ": "t", "ထ": "T", "ဒ": "d", "န": "n", "ပ": "p", "ဖ": "P", "ဗ": "b", "ဘ": "B", "မ": "m",
        "ယ": "y", "ဝ": "w", "သ": "j", "ဟ": "h", "အ": "a", 'လ': 'l', "ဠ": "lx", "ဣ": "ix", "ဤ": "Ix", "၊": "/", "။": "//", "ဥ": "Ux", "ဦ": "OO", "ဧ": "ax", "ဩ": "O", "ဪ": "OR", "ါ": "A", "ာ": "A", "ိ": "i", "ီ": "I","ေ": "e",
        "ု": "u", "ူ": "U", "ဲ": "L", "ံ": "N", "့": ".", "း": ":", "ျ": "Y", "ြ": "R", "ွ": "W", "ှ": "H","၎":"4",
        "ဿ": "jx", "်": ""
    }

        try:
            text = re.sub(r"([က-အ|ဥ|ဦ](င်္|[က-အ][ှ]*[့း]*[်]|([က-အ]္)|[ါ-ှႏꩻ][ꩻ]*){0,}|.)", r"\1 ", text.strip())
            text = re.sub(r"[\s]{1}", r",", text) # 3 line paung p try
            text = re.sub(r"[,]{3}",r" ",text) # 3 line paung p try
            text = re.sub(r",$",r'',text) # 3 line paung p try
            text = re.sub(r"(([က-အ])္ ([က-အ]))", r"\2် \3", text)

            # List of custom rules for converting specific word patterns to Romanized forms
            rules = [
                (re.compile(r'ကျွန် မ '), "q'm "),
                (re.compile(r'ကျွန် တော် '), "q't "),
                (re.compile(r'ကျွန်ုပ် '), 'Q" '),
            ]
            for rule in rules:
                text = rule[0].sub(rule[1], text)
            text = re.sub(r'([‌ေ][က-ဪ]*[ာါ]*[်])', r'\1F', text)

            # Perform Romanization by replacing Burmese characters with Roman equivalents
            for burmese_char, roman_char in sorted(burmese_to_roman.items(), key=lambda x: len(x[0]), reverse=True):
                text = text.replace(burmese_char, roman_char)


            text = re.sub(r' ,', "", text)
            return text
        except Exception as e:
            raise Exception(f"An error occurred during Burmese_to_Romanization: {e}")

    def romanization_to_burmese(self,burmese_text):
        
        
            burmese_to_roman = {
            'က': 'k', 'ခ': 'K', 'ဂ': 'g', 'ဃ': 'G', 'င': 'c', "၏": "E", "၍": "rx", "၌": "Nx", "င်္": "f",
            'စ': 's', 'ဆ': 'S', 'ဇ': 'z', 'ဈ': 'Z', "ဉ": "q", 'ည': 'Q', "ဋ": "tx", "ဌ": "Tx", "ဍ": "dx", "ဎ": "Dx", "ဏ": "nx",
            "ရ": "r", "ဓ": "D", "တ": "t", "ထ": "T", "ဒ": "d", "န": "n", "ပ": "p", "ဖ": "P", "ဗ": "b", "ဘ": "B", "မ": "m",
            "ယ": "y", "ဝ": "w", "သ": "j", "ဟ": "h", "အ": "a", 'လ': 'l', "ဠ": "lx", "ဣ": "ix", "ဤ": "Ix", "်":"F"
        }

            burmese_to_roman.update({
            "၊": "/", "။": "//", "ဥ": "Ux", "ဦ": "OO", "ဧ": "ax", "ဩ": "O", "ဪ": "OR", "ါ": "A", "ာ": "A", "ိ": "i", "ီ": "I","ေ": "e",
            "ု": "u", "ူ": "U", "ဲ": "L", "ံ": "N", "့": ".", "း": ":", "ျ": "Y", "ြ": "R", "ွ": "W", "ှ": "H","၎":"4",
            "ဿ": "jx"
        })
            roman_to_burmese = {v: k for k, v in burmese_to_roman.items()}

            try:
                def roman_to_special_words(text):
                    reverse_rules = [
                        (re.compile(r"q'm"), 'ကျွန် မ '),
                        (re.compile(r"q't"), 'ကျွန် တော် '),
                        (re.compile(r'Q"'), 'ကျွန်ုပ် '),
                    ]
                    for rule in reverse_rules:
                        text = rule[0].sub(rule[1], text)
                    return text

                def romanize_burmese(text):
                    romanized_text = text
                    for burmese_char, roman_char in sorted(roman_to_burmese.items(), key=lambda x: len(x[0]), reverse=True):
                        romanized_text = romanized_text.replace(burmese_char, roman_char)
                    return romanized_text

                transformed_text = ""
                burmese_text = re.sub(r"(,)",r'\1 ',burmese_text)
                burmese_text = roman_to_special_words(burmese_text)
                for word in burmese_text.split(" "):
                    word = romanize_burmese(word)
                    word = re.sub(r"([ခဂငဒဝပ]ေ*)ာ", r"\1ါ", word)
                    word = re.sub(r"([က-အ])(.*)([က-အ])", r"\1\2\3်", word)
                    word = re.sub(r"််", "်", word)
                    transformed_text += word + " "
                    transformed_text = re.sub(r"၎ငး", "၎င်း", transformed_text)

                return re.sub(r",\s*",r"",transformed_text)

            except Exception as e:
                return f"An error occurred during Romanization_to_Burmese: {e}"


st.title("Burmese Romanization Converter")

converter = BurmeseConverter()

# Input options
option = st.radio(
    "Choose a conversion type:",
    ("Burmese to Romanization", "Romanization to Burmese")
)

input_text = st.text_area("Enter your text:", height=200)

if st.button("Convert"):
    if option == "Burmese to Romanization":
        output_text = converter.burmese_to_romanization(input_text)
    else:
        output_text = converter.romanization_to_burmese(input_text)
    
    st.subheader("Converted Text:")
    st.text_area("Result:", value=output_text, height=200, disabled=True)