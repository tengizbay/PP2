import re
s = input()
if re.fullmatch(r"ab{2,3}", s):
    print("Matched")
else:
    print("Not matched")