#4.Write a Python program to find the occurrences of 10 most common words in a given text.
from collections import Counter
import re
text="""State government is arranging for food and
accommodation for migrant labourers of Chhattisgarh
who were stranded in other states and are returning. They
will be staying at temporary shelter homes in schools
and panchayat bhawans for 14 days"""
w= re.findall('\w+',text)
print(Counter(w).most_common(10))
