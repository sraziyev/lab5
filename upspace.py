import re

def spaces(txt):
    result = re.sub(r'([A-Z])', r' \1', txt)
    return result

inpt = input()
answer = spaces(inpt)
print(answer)
