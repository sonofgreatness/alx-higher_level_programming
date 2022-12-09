#!/usr/bin/python3"""
"""
Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

    You can assume the number will be between 1 to 3999.
    def roman_to_int(roman_string) must return an integer
    If the roman_string is not a string or None, return 0

"""
def checkLast2digits(string_ = "IX") ->int:
    dictionary = {'IX': 9, 'IV': 4, 'II': 2}
    keysList  = dictionary.keys()

    for elements in keysList:
        if elements == string_:
            return dictionary[string_]

def sumMaker(character_ = 'I') -> int:
    dictionary = {'X' :10, 'I':1, 'L' :50,'D' :500, 'C':100, 'V' :5}
    keysList  = dictionary.keys()

    for elements in keysList: 
        if elements == character_:
            return dictionary[character_]

def roman_to_int(roman_string):

    number_dictionary = {'X' : 10, 'I': 1, 'L' : 50,'D' : 500, 'C': 100}
    input_length = len(roman_string)
    sum_ = 0;
    if input_length >= 2:
        for i in range(0, input_length - 2):
            sum_ += sumMaker(roman_string[i])

        sum_ += checkLast2digits(roman_string[input_length - 2 :])
        return sum_
    elif input_length == 1:
        return sumMaker(roman_string)
