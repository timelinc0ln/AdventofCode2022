data = str(open('datastream.txt', 'r').read())

for i in range(0,len(data)):
    if i > 14:
        a = set(data[i-15:i-1])
        if len(a) == 14:
            print(i-1)
            break

