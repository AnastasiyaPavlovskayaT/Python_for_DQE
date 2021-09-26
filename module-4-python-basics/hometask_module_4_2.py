# The Python script to solve Module 4  - module 3 'String Object' home task.


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


def fix_iz(string):
    import re
    return re.sub(r'(\siz\s)', ' is ', string, flags=re.IGNORECASE)

def normilize_string(string):
    import re
    normalized_string = ''
    for sentence in re.split(r'(\S.*?\.)', string):
      normalized_string = normalized_string + sentence.capitalize()
    return normalized_string


def additional_sentence(string):
    import re
    return ' '.join(list(map(lambda word: word.rstrip('.'), re.findall(r'\b\w*?\b\.', string)))).strip().capitalize() + '.'

def add_sentence(string, add_string, paragraph_number):
    import re
    new_paragraph = re.split(r'(\r)', string)
    new_paragraph[paragraph_number] = re.split(r'(\r)', string)[paragraph_number] + ' ' + add_string
    return ''.join(new_paragraph)



def count_whitespaces(string):
    import re
    return len(re.findall(r'[\s]', string))

print('------------------------------------')
print('Resulted processed text')
print('------------------------------------')
print(add_sentence(normilize_string(fix_iz(given_string)), additional_sentence(normilize_string(fix_iz(given_string))), 2))


print('------------------------------------')
print('Count of spaces and whitespaces:', count_whitespaces(given_string))
print('------------------------------------')


