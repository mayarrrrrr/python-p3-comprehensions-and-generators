#!/usr/bin/env python3

def return_evens(num_list):
    # new_list = []
    # for num in num_list:
    #     if (num % 2 == 0):
    #         new_list.append(num)
    # return new_list  
    
    new_list = [num for num in num_list if (num % 2 == 0)]  
    return new_list

print(return_evens([0,1,3,5,7,8,9]))

def make_exclamation(sentence_list):
    
    # new_sentence_list = []
    
    # for item in sentence_list:
    #     new_item = item + "!"
    #     new_sentence_list.append(new_item)
    # return new_sentence_list 
    
    new_sentence_list = [item + "!" for item in sentence_list ]  
    return new_sentence_list
     

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))