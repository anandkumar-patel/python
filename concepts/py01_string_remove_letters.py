import re
# 1st method
p = 'clcoding'
d = p.replace('cl', '')
print(d)

# 2nd method
d = p[2:]
print(d)

# 3rd method
d = p.partition('cl')[2]
print(d)

# 4th method
d = re.sub(r'cl', '', p)
print(d)

# 5th method
d = p.strip('cl')
print(d)
