# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tFADQmcCIX7OBFqd7fyzYhVToxP5G3_v
"""

#1.Length of a string
str=input("enter the string:")
print("Length of the input string is:",len(str))

#2. character frequency
def char_frequency(str1):
    dict={ }
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_frequency('google.com'))

#3.To get a single string from two string
def chars_mix_up(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    return new_a+'   '+new_b
print(chars_mix_up('abc','xyz'))

#4.String display in uppercase and lowercase 
user_input=input("what's your fav language?")
print("My fav language is",user_input.upper())
print("My fav language is",user_input.lower())

#5.To remove a newline in python
str1='python Exercise\n'
print(str1)
print(str1.rstrip())

#6. to count occurrence of a substring
str1="the quick brown fox jumps over the lazy dog."
print()
print(str1.count("fox"))
print()



#7. convert string in list
str1="apple,mango,banana"
print(f'list of items={str1.split(",")}')

#8. to print character of a string using loop
z=input("enter a string")
for i in z:
    print(i)

#9. to find the length without using len()
a='fridge'
count=0
for i in a:
   count=count+1
 print(count)