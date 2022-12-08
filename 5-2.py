data = open('crane.txt', 'r').read().split("\n")
       
s1, s2, s3, s4, s5, s6, s7, s8, s9 = ['C','Z','N','B','M','W','Q','V'], ['H','Z','R','W','C','B'], ['F','Q','R','J'], ['Z','S','W','H','F','N','M','T'], ['G','F','W','L','N','Q','P'], ['L','P','W'], ['V','B','D','R','G','C','Q','J'], ['Z','Q','N','B','W'], ['H','L','F','C','G','T','J']
piles = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
#s1, s2, s3 = ['Z','N'],['M','C','D'],['P']
#piles = [''.join(s1), ''.join(s2), ''.join(s3)]
for inst in data:
    inst1=inst.split()
    number, pile1, pile2 = int(inst1[1]), int(inst1[-3]), int(inst1[-1])
    piles[pile2-1] += piles[pile1-1][-number:]
    piles[pile1-1] = piles[pile1-1][0:-number]

answer = ""
for i in range(0,len(piles)):
   answer+=str(piles[i][-1])
print(answer)