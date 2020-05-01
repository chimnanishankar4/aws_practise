#2. Write a Python program to find the most common elements and their counts of a specified text.
from collections import Counter
list=[1,2,3,4,1,2,6,7,3,8,1]
cnt=Counter(list)
print(cnt.most_common())
