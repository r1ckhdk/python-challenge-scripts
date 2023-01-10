from typing import List

string: str = str(input('Insert string to decode here: '))
ascii_list: List[int] = []

for character in string:
    if ord(character) == 122:
        ascii_list.append(98)

    elif ord(character) == 121:
        ascii_list.append(97)

    elif 97 <= ord(character) <= 122:
        ascii_list.append(ord(character) + 2)

    else:
        ascii_list.append(ord(character))

decoded_string: str = ''
for character in ascii_list:
    decoded_string += chr(character)

print(decoded_string)