s = input()
components = s.split('_')
print(components[0] + ''.join(x.title() for x in components[1:]))