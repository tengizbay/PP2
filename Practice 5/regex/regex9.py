import re
s = input()
print(re.sub(r'(?<!^)(?=[A-Z])', ' ', s))