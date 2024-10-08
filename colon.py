import re

txt =input()
a=r"[ ,.]"
x = re.sub(a, ":", txt)
print(x)