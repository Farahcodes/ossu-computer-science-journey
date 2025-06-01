# Finger Exercise Lecture 5
# Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your code should print out aceg.

my_str = "abcdefg"
# This slice starts at the beginning, goes to the end, with a step of 2
even_chars_string = my_str[::2]
print(even_chars_string)