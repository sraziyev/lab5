import re

text = r'[a-z]+_[a-z]+'
txt=input()
match = re.match(text, txt)
if match:
    print(f"'{txt}' matches")
else:
    print(f"'{txt}' doesn't match")
