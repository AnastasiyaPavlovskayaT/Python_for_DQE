# The Python script to solve Module 3 'String Object' home task.

# the re (regular expression operations) module is imported
import re

# declare and set a variable of string type
given_string = 'homEwork:\n' \
         '\n' \
         '  tHis iz your homeWork, copy these Text to variable.\n' \
         '\n' \
         ' \n' \
         '\n' \
         '  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE' \
         ' witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n' \
         '\n' \
         ' \n' \
         '\n' \
         '  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n' \
         '\n' \
         ' \n' \
         '\n' \
         '  last iz TO calculate nuMber OF Whitespace characteRS in this Tex.' \
         ' caREFULL, not only Spaces, but ALL whitespaces. I got 87.\n'

# to replace "iz" where it is a mistake to "is" was used function sub
# to find all "iz" where it is a mistake was used regular expression
# \s - space
# was used an optional argument to set a flag for letter case ignoring
corrected_string = re.sub(r'(\siz\s)', ' is ', given_string, flags=re.IGNORECASE)

# to normalize text was used following operators
# was used method split to create a list of sentences (ends on dot) with regular expression
# \S - matches any non-whitespace character
# .* - quantifier, matches a single character in the string
# ? - lazy quantifier mode
# \. -  matches the character .
# declare empty string in order to collect normalized sentences into one new line

normalized_string = ''
for sentence in re.split(r'(\S.*?\.)', corrected_string):
    # was used concatenation operation and capitalize method to normalize every sentence
    normalized_string = normalized_string + sentence.capitalize()

# to create the additional sentence using with last words of each existing sentence
# was created the list of last words of each existing sentence
# was used function findall with regular expression
# \b - matches a backspace character
# \w - matches any word character
# * - quantifier, matches a single character in the string
# ? - lazy quantifier mode
# \. -  matches the character .
last_words = re.findall(r'\b\w*?\b\.', normalized_string)

# declare and set function cut_dot to cut the last symbol '.'


def cut_dot(word):
    return word.rstrip('.')


# was used function map to apply the function cut_dot to each word in the list last_words
# function list was used to transform object mat to list
cut_words = list(map(cut_dot, last_words))

# join last words - the elements cut_words list - to one sentence
# to normalize were used methods strip and capitalize
# '.' was added by concatenation operation
additional_sentence = ' '.join(cut_words).strip().capitalize() + '.'

# to add additional sentence  to the end of second paragraph was used function sub with regular expression
# was found end od the second paragraph and replaced by additional sentence
# was used an optional argument to set a flag for letter case ignoring
add_sentence = re.sub(r'( paragraph.)', ' paragraph. ' + additional_sentence, normalized_string, flags=re.IGNORECASE)
print('------------------------------------')
print('Resulted processed text')
print('------------------------------------')
print(add_sentence)

print('------------------------------------')
# to count all spaces and whitespaces was used function findall with regular expression
# \s matches any whitespace character (equivalent to [\r\n\t\f\v ])
print('Count of spaces and whitespaces:', len(re.findall(r'[\s]', given_string)))
print('------------------------------------')






