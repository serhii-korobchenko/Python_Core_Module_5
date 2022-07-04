import re

""" s = "I am 25 years old"
age = re.search('\d+', s)
print(age)  # <re.Match object; span=(5, 7), match='25'> """



s = "I am 25 years old."
age = re.search('\d+', s)
print(age.group())  # 25