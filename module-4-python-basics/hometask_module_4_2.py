
# The Python script to solve Module 4  - module 3 'String Object' home task.

# declare and set function fix_iz to replace 'iz' to 'is'
# where is is a mistake
# function has one parameter - string


def fix_iz(string):
    import re
    return re.sub(r'(\siz\s)', ' is ', string, flags=re.IGNORECASE)


# declare and set function normalize_string
# to normalize string from letter cases point of view
# function has one parameter - string


def normalize_string(string):
    import re
    normalized_string = ''
    for sentence in re.split(r'(\S.*?\.)', string):
      normalized_string = normalized_string + sentence.capitalize()
    return normalized_string


# declare and set function additional_sentence
# to create one more sentence with last words of each existing sentence
# function has one parameter - string


def additional_sentence(string):
    import re
    return ' '.join(list(map(lambda word: word.rstrip('.'), re.findall(r'\b\w*?\b\.', string)))).strip().capitalize() + '.'


# declare and set function additional_sentence
# to create one more sentence with last words of each existing sentence
# function has three parameters
# 1 - proceed string
# 2 - string which shoud be added
# 3 - number of paragraph in which the additional sentence
# will be added at the end


def add_sentence(string, add_string, paragraph_number):
    import re
    new_paragraph = re.split(r'(\r)', string)
    new_paragraph[paragraph_number] = re.split(r'(\r)', string)[paragraph_number] + ' ' + add_string
    return ''.join(new_paragraph)


# declare and set function count_whitespaces
# to calculate number of whitespace characters
# function has one parameter - string


def count_whitespaces(string):
    import re
    return len(re.findall(r'[\s]', string))


# declare and set a variable of string type
given_string = 'homEwork:\n' \
               '\n' \
               '  tHis iz your homeWork, copy these Text to variable.\r' \
               '\n' \
               ' \n' \
               '\n' \
               '  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE' \
               ' witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\r' \
               '\n' \
               ' \n' \
               '\n' \
               '  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\r' \
               '\n' \
               ' \n' \
               '\n' \
               '  last iz TO calculate nuMber OF Whitespace characteRS in this Tex.' \
               ' caREFULL, not only Spaces, but ALL whitespaces. I got 87.\r'

print('------------------------------------')
print('Resulted processed text')
print('------------------------------------')
try:
    print(add_sentence(normalize_string(fix_iz(given_string)), additional_sentence(normalize_string(fix_iz(given_string))), 2))
except IndexError:
    print('Given string is empty.')


print('------------------------------------')
print('Count of spaces and whitespaces:', count_whitespaces(given_string))
print('------------------------------------')


