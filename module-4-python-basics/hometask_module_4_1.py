# The Python script to solve Module 4  - module 2 'Collections' home task.

# declare and set function for creation of a list of random number of dicts (from 2 to 10)
# dictionaries random numbers of keys is letter; dictionaries values should be a number (0-100),
# the function has two parameters - upper bounds for generation of dict's values and number of dicts
def generate_list_of_dict(count_items=10, dict_values=100):
    import random
    import string
    random_list_of_dict = [{random.choice(string.ascii_letters): random.randint(0, dict_values)
                            for index_couple in range(random.randint(2, count_items))}
                           for index_dict in range(2, random.randint(2, count_items))]
    print('\nCreated list of random number of dicts:\n ', random_list_of_dict)
    return random_list_of_dict


# declare and set function map_func to combine all key values ​​from dictionaries
# the function has one parameter - the list of dictionaries
def map_func(random_list_of_dict):
    import collections
    auxiliary_dict = collections.defaultdict(list)
    for dict_element in random_list_of_dict:
        for key, value in dict_element.items():
            auxiliary_dict[key].append(dict_element[key])
    return auxiliary_dict


# declare and set function reduce_func to find max value for key
# and create new one dictionary with updated keys
# the function has one parameter - the dictionary
def reduce_func(auxiliary_dict):
    import collections
    common_dict = {}
    for key_letter, list_value in auxiliary_dict.items():
        if len(list_value) > 1:
            common_dict.update({key_letter + str('_') + str(list_value.index(max(list_value)) + 1): max(list_value)})
        else:
            common_dict.update({key_letter: max(list_value)})
    return common_dict


print('\nResulted common dict:\n', reduce_func(map_func(generate_list_of_dict(10, 100))))
