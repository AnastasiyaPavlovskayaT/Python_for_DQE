# The Python script to solve Module 2 'Collections' home task.

# the random module is imported to the program by keyword 'import' to use a function which generates random numbers
import random

# the string module is imported to use string.ascii_letters for choosing letters for keys
# string.ascii_letters it is 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import string

# the collections module is imported
import collections

# creation of a list of random number of dicts (from 2 to 10); dict's random numbers of keys is letter; dict's values should be a number (0-100),
random_list_of_dicst = [{random.choice(string.ascii_letters):random.randint(0,100) for i in range(random.randint(0,10))} for i in range(2,random.randint(2,10))]

# the test data to check the algorithm: random_list_of_dicst =  [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

# generted random_list_of_dicst list output
print('Сreated list of random number of dicts:\n ',random_list_of_dicst)

# announce auxiliary dict; defaultdict is an inherited class
#default items are created with list (), which returns a new empty list object
auxiliary_dict = collections.defaultdict(list)

# merging all the generated dictionaries of the list into one dict by keys - values ​​are the lists of values ​​of merged dicts
# defaultdict auxiliary_dict is using in the algorithm because we need to get an element with a key that is not currently in the dictionary
for dict_element in random_list_of_dicst:
    for key,value in dict_element.items():
        auxiliary_dict[key].append(dict_element[key])

# print(auxiliary_dict)

# announce empty common dict
common_dict = {}

# find the maximum value in the list for each key and its index
# add the updated key value and maximum value to the common dict
for key_letter,list_value in auxiliary_dict.items():
    if len(list_value) > 1:
        common_dict.update({key_letter+str('_')+str(list_value.index(max(list_value))+1):max(list_value)})
    else:
        common_dict.update({key_letter: max(list_value)})

# common dict output
print('Resulted common dict:\n', common_dict)

# for test data common dict should be {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
