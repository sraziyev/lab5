import re

txt=input()
match = re.match('abbb', txt)
if match:
    print(f"'{txt}' matches")
else:
    print(f"'{txt}' doesn't match")
