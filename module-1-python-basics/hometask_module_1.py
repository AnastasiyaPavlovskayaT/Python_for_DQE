
# The Python script to solve Module 1 'Python Basics' home task.

import random # the random module is imported to the program by keyword 'import' to use a function which generates random numbers

# to sorting list of random numbers was defined the bubble_sort function - 'Bubble sort' algorithm is used

def bubble_sort(unsorted_list): # bubble_sort function is defined; the one arguments unsorted_list is used
    list_length = len(unsorted_list) - 1 #In bubble sorting, the number of iterations of the outer loop is determined by the long list minus one,
                                         # since when the second element falls into place, the first is already uniquely minimal and is in its place.
    sorted_flag = True # set flag of sorted element to true, because 'while' loop is working once logic condicions is true
    while sorted_flag: #the loop 'while' is started;the loop commands are executed if logic condicion after keyword 'while' is true
        sorted_flag = False # set flag of the sorted element to true; it needs to fixate that a related couple of elements were processed by the algorithm
        for i in range(list_length): # the 'for' loop is started to iterate over all the elements of the list
            if unsorted_list[i] > unsorted_list[i+1]: # comparing two adjacent list elements
                sorted_flag = True # set flag of sorted element to false; it needs to fixate that a related couple of elements were processed by the this part of algorithm
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i] # swapping two adjacent elements in places

random_list = [random.randint(0,1000) for i in range(100)] # the list of 100 random numbers from 0 to 1000 is created
#print(random_list) # uncomment it if random_list output is needed
bubble_sort(random_list) # the sort function bubble_sort' is applied to the random_list
#print(random_list) # uncomment it if sorted random_list output is needed

even_numbers = [i for i in random_list if i%2==0] # the list of even numbers from random_list is created; %  - integer division by 2
odd_numbers = [i for i in random_list if i%2!=0]  # the list of odd numbers from random_list is created; %  - integer division by 2

try: # the code block run in which an error is expected
    # the average of even and odd numbers optput; was used 'sum' (to summarize all elements) and 'len' (to count numbers in the even_numbers and odd_numbers list) functions.
    print('The average value of even numbers (elements of the random_list) = ', round(sum(even_numbers)/len(even_numbers),2)) # the average is rounded to 2 symbols after dot
    print('The average value of odd  numbers (elements of the random_list) = ', round(sum(odd_numbers)/len(odd_numbers),2)) # the average is rounded to 2 symbols after dot
except ZeroDivisionError: # define the type of exception is defined that we expect in the try block  - division by zero possible
    print('The randomize list contains zero elements.') # the error message output once division by zero is happened
finally: #irrespective of whether there is an exception or not, this block of code will always be executed
    print('The program run is finished.') # the program termination message


