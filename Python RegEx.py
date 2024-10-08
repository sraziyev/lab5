#What will be the printed result?
import re
txt = 'The rain in Spain'
x = re.findall('[a-c]', txt)
print(x)
#['a', 'a']

#What will be the printed result?
import re
txt = 'The rain in Spain'
x = re.search('a', txt)
print(x.start())
#5

#What will be the printed result?
import re
txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x.start())
#3

'''
When using the re module to find a match, a match will return a Match object, but what is the return value when there is no match?
'''
#None