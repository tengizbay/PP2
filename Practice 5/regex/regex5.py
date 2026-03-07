import re
s = input()
if re.fullmatch(r"a.*b", s):
    print("Matched")
else:
    print("Not matched")