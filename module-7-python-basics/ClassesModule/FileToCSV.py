def word_count(file_name):
    import re
    import string
    file = open(file_name, "r+")
    words = []
    word_count_dict = {}
    for text in file:
        Wnumb = re.findall(r'\b(\w+)\b', re.sub(r'(\sit\'s\s)', 'it is ', text.lower(), flags=re.IGNORECASE))  # words in file
        numb = re.findall(r'\b(\d+)\b', text)  # numbers in file
        for word in Wnumb:
            if word not in numb and True:
                words.append(word)
    dicstint_words = list(set(words))
    for i in dicstint_words:
        if i in words:
            word_count_dict.update({i: words.count(i)})
    return word_count_dict


def letter_func(file_name):
    import re
    import string
    import collections
    file = open(file_name, "r+")
    list_of_letters = []
    for text in file:
        unique_letters = set(text)
        let_count = {}
        for letter in unique_letters:
            if letter in string.ascii_letters:
                let_count[letter] = text.count(letter)
        list_of_letters.append(let_count)
    auxiliary_dict = collections.defaultdict(list)
    for dict_element in list_of_letters:
        for key, value in dict_element.items():
            auxiliary_dict[key].append(dict_element[key])
    all_letters = {}
    count_letter = []
    for key_letter, letter_count in auxiliary_dict.items():
        letter_count_dict = [0]
        if len(letter_count) > 0:
            letter_count_dict[0] = sum(letter_count)
            count_letter.append(sum(letter_count))
            all_letters.update({key_letter: letter_count_dict})

    result_dict = {}

    for key_all, value_all in all_letters.items():

        list_value = [0, 0, 0]

        if key_all.lower() not in result_dict.keys():
            result_dict.update({key_all.lower(): list_value})

        result_dict[key_all.lower()][0] += value_all[0]

        if key_all.isupper():
            result_dict[key_all.lower()][1] += value_all[0]

        result_dict[key_all.lower()][2] = round(result_dict[key_all.lower()][0] * 100 / sum(count_letter), 1)

    return result_dict

def txt_to_csv(txt_file_name):
    import csv
    with open('word-count.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file, delimiter='-', lineterminator='\n')
        dict_word = word_count(txt_file_name)
        for key, value in dict_word.items():
            writer.writerow([key, value])

    with open('letter-statistic.csv', 'w+') as csv_file:
        headers = ['letter', 'cout_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n', fieldnames=headers)
        writer.writeheader()
        letter_word = letter_func(txt_file_name)
        for key, value in letter_word.items():
            writer.writerow({'letter': key, 'cout_all': value[0], 'count_uppercase': value[1], 'percentage': value[2]})