import re
s = input()
if re.fullmatch(r"ab*", s):
    print("Matched")
else:
    print("Not matched")