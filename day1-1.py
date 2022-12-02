data = open('calories.csv', 'r').read().split("\n\n")
temp =[]
for elf in data:
    temp1=elf.split("\n")
    temp.append(sum([int(x) for x in temp1]))
print("Part 1:", max(temp))
temp.sort()
print("Part 2:", temp[-1] + temp[-2] + temp[-3])
