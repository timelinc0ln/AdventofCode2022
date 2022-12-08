data = open('clean.txt', 'r').read().split("\n")
count = 0
for item in data:
    a, b = item.split(',')
    c, d = a.split('-')
    e, f = b.split('-')
    s1 = set(range(int(c), int(d)+1))
    s2 = set(range(int(e), int(f)+1))
    if s1.issubset(s2) or s2.issubset(s1):
        count += 1

print(count)