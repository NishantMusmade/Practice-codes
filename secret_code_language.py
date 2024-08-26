#A program to translate a message into secret code language. Use the rules below to translate normal English into secret code Language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string
# Decoding:
# if the word contains less than 3 characters, reverse it *
# else:
    #remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

import random
import string
import sys

while True: 
    flag = 1
    while flag==1:
        try:
            choice = int(input('Decode - 0\nEncode - 1\nExit - 3\nEnter your choice: '))
            flag = 0
        except:
            print('Invalid input...!')
    if choice == 3:
        sys.exit()
    if choice == 0:
        input_string = input("Enter the encrypted string: ")
        new_words = input_string.split()
        print(new_words)
        original_string = []
        for word in new_words:
        #if length of string is less than 3
            if len(word)<3:
                original_word = word[::-1]
                # print('\n The original string is : ',original_string)
            else:
                original_word = word[3:-3]
                original_word = original_word[-1]+original_word[:-1]
            original_string.append(original_word)
        original_string_final = ' '.join(original_string)
        print('\nThe original string is: ',original_string_final)
    else:
        input_string = input('Enter the string you want to encode: ')
        new_words = input_string.split()
        print(new_words)
        encrypted_string = []
        for word in new_words:
        #if length of string is less than 3
            if len(word)<3:
                encrypted_word = word[::-1]
            else:
                encrypted_word = word[1:] + word[0]

                #generating random string
                length_random_word = 3
                random_word_1 = ''.join(random.choices(string.ascii_lowercase, k = length_random_word))
                random_word_2 = ''.join(random.choices(string.ascii_lowercase, k = length_random_word))

                encrypted_word = random_word_1 + encrypted_word + random_word_2
            encrypted_string.append(encrypted_word)
        encrypted_string_final = ' '.join(encrypted_string)
        print('\nEncrypted string is: ',encrypted_string_final)


