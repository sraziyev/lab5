"""import re

txt=input()
camel = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), txt)
print(camel)

сработал для одного _
"""

import re

def snaketocamel(txt):
    camel = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), txt)
    return camel[0].lower() + camel[1:]

inpt=input()
answer=snaketocamel(inpt)
print(answer)

