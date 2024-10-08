import re

def upsplit(txt):
    result = re.findall(r'[A-Z][^A-Z]*', txt)
    return result

inpt = input()
answer = upsplit(inpt)
print(answer)
