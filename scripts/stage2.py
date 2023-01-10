messed_string: str = input('Insert your string here: ')

cleaned_string: str = ''.join(character for character in messed_string if character.isalnum())
print(cleaned_string)