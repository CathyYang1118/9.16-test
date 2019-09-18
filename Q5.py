FileBefore = open('Q4.txt','r')
FileAfter = open('new-gradebook.txt','w')

imf = []
lowest = 100
name = ''

for i in FileBefore.readlines():
    i = i.strip('\n')
    j = i.split(' ')
    phy = j[-1]
    PhyScore = phy[3:]
    imf.append(i)
    if int(PhyScore) <= lowest:
        lowest = int(PhyScore)
        name = j[1]
#print(lowest,name,imf)

for t in imf:
    s = t.split(' ')
    if s[1] != name:
        #print(s[1])
        FileAfter.write(t)
        FileAfter.write('\n')

FileBefore.close()
FileAfter.close()
