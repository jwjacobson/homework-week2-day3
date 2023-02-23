#!/usr/bin/python

# Exercise 1
# Given an array of positive integers nums, return a list of all of the negative integers.
def negate(nums):
    negated_list = []
    for num in nums:
        negated_list.append(num * -1)
    return negated_list

def negate_comprehension(nums):
    return [num * -1 for num in nums]

# Exercise 2¶
# Given a string, return a list of all of the digits in the string.
def digit_extractor(s):
    digit_list = []
    for word in s:
        for char in word:
            if char.isdigit():
                digit_list.append(char)
    return digit_list
    
# Exercise 3
# Given a string digits, return a string of the digits + 1
def add_one(digits):
    return str(int(digits) +1)
