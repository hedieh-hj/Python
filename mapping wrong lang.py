
persian_to_english = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y',
    'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p', 'ج': '[', 'چ': ']',
    'ش': 'a', 'س': 's', 'ی': 'd', 'ب': 'f', 'ل': 'g', 'ا': 'h',
    'ت': 'j', 'ن': 'k', 'م': 'l', 'ک': ';', 'گ': "'", 'پ': '\\',
    'ظ': 'z', 'ط': 'x', 'ز': 'c', 'ر': 'v', 'ذ': 'b', 'د': 'n',
    'ئ': 'm', 'و': ',', '؟': '?'
}

english_to_persian = {v: k for k, v in persian_to_english.items()}

def convert_text(text, direction='en_to_fa'):
    if direction == 'en_to_fa':
        mapping = english_to_persian
    elif direction == 'fa_to_en':
        mapping = persian_to_english
    else:
        raise ValueError("error in converter direction'en_to_fa' or 'fa_to_en' ")
    
    return ''.join([mapping.get(char, char) for char in text])

def main():
    print("converter")
    print("for exit eneter 'exit'")
    print("for change direction of convert eneter 'switch' word")
    print("direction: eng to persian(if your wrong text is english)")
    direction = 'en_to_fa'  #default direction

    while True:
        try:
            user_input = input(f"\nenter your wrong text({direction}): ").strip()
            if user_input.lower() == 'exit':
                print("exit.")
                break
            elif user_input.lower() == 'switch':
                direction = 'fa_to_en' if direction == 'en_to_fa' else 'en_to_fa'
                # print(f"converter: {'en_to_fa' if direction == 'en_to_fa' else 'pa_to_en'}")
                continue
            converted = convert_text(user_input, direction)
            print(f"converted text: {converted}")
        except KeyboardInterrupt:
            print("\nfor exit press Ctrl+C.")
            break
        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    main()
