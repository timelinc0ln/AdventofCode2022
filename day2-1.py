data = open('rps.txt', 'r').read().split("\n")
temp=[]
for item in data:
    temp.append((item.split(" ")))

 # A = rock = 1 = X
 # B = paper = 2 = Y
 # C = scissor = 3 = Z
myscore = 0
hiscore = 0
for tuple in temp:
    if tuple[0] == 'A' and tuple[1] == 'X':
        myscore += 4
        hiscore += 4
    if tuple[0] == 'A' and tuple[1] == 'Y':
        myscore += 8
        hiscore += 1
    if tuple[0] == 'A' and tuple[1] == 'Z':
        myscore += 3
        hiscore += 7
    if tuple[0] == 'B' and tuple[1] == 'X':
        myscore += 1
        hiscore += 8
    if tuple[0] == 'B' and tuple[1] == 'Y':
        myscore += 5
        hiscore += 5
    if tuple[0] == 'B' and tuple[1] == 'Z':
        myscore += 9
        hiscore += 2
    if tuple[0] == 'C' and tuple[1] == 'X':
        myscore += 7
        hiscore += 3
    if tuple[0] == 'C' and tuple[1] == 'Y':
        myscore += 2
        hiscore += 9
    if tuple[0] == 'C' and tuple[1] == 'Z':
        myscore += 6
        hiscore += 6
print(myscore)
print(hiscore)