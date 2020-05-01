#1. Write a Python program that iterate over elements repeating each as many times as its count.
from collections import Counter
num=Counter(a=5,b=3,c=2)
print(list(num.elements()))
