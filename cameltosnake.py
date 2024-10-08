import re

def cameltosnake(txt):
    result = re.sub(r'([A-Z])', r'_\1', txt).lower()
    return result

# Example usage
inpt = input()
answer = cameltosnake(inpt)
print(answer)
