data = open('sacks.txt', 'r').read().split("\n")
temp = []
for item in data:
    a,b = item[:len(item)//2], item[len(item)//2:]
    c = set(a)
    d = set(b)
    e = (c & d)
    temp.append(list(e)[0])

total = 0

for letter in temp:
    if letter.islower():
        a = [ord(letter) - 96 for c in letter]
        total += a[0]
        
    if letter.isupper():
        a = [ord(letter) - 64 for c in letter]
        total += a[0] + 26

print(total)