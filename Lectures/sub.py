import re

p = re.sub(r'(blue|white|red)', 'colour', 'blue socks and red shoes')
print(p)    # colour socks and colour shoes