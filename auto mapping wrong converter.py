# -*- coding: utf-8 -*-

# نگاشت دقیق کلیدهای کیبورد فارسی به انگلیسی
persian_to_english = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y',
    'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p', 'ج': '[', 'چ': ']',
    'ش': 'a', 'س': 's', 'ی': 'd', 'ب': 'f', 'ل': 'g', 'ا': 'h',
    'ت': 'j', 'ن': 'k', 'م': 'l', 'ک': ';', 'گ': "'", 'پ': '\\',
    'ظ': 'z', 'ط': 'x', 'ز': 'c', 'ر': 'v', 'ذ': 'b', 'د': 'n',
    'ئ': 'm', 'و': ',', '؟': '?'
}

english_to_persian = {v: k for k, v in persian_to_english.items()}

def convert_text(text, to_farsi=False):
    mapping = english_to_persian if to_farsi else persian_to_english
    return ''.join([mapping.get(char, char) for char in text])

def has_farsi(text):
    return any('\u0600' <= c <= '\u06FF' for c in text)

def has_english(text):
    return any('a' <= c.lower() <= 'z' for c in text)

def main():
    print("Simple Persian-English Keyboard Converter")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter your text: ").strip()
        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        if has_farsi(user_input):
            print("Converted (to English):", convert_text(user_input, to_farsi=False))
        elif has_english(user_input):
            print("Converted (to Persian):", convert_text(user_input, to_farsi=True))
        else:
            print("Cannot determine language. Try again.")

if __name__ == "__main__":
    main()
