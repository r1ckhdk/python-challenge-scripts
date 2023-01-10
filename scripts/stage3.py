from re import findall
from typing import List

string: str = input('Insert your string here: ')

string_list: List[str] = list(string)
patterns_found: List[str] = findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', string)

decoded_string: str = ''
for element in patterns_found:
    decoded_string += element

print(decoded_string)