FileBefore = open('ID.txt','r')
FileAfter = open('Average.txt','w')

for i in FileBefore.readlines():
    j = i.split(' ')
    #print(j)
    MathScore = j[3]
    CSScore = j[4]
    PhyScore = j[5]
    Total = int(MathScore[4:])+int(CSScore[2:])+int(PhyScore[3:-1])
    #print(int(MathScore[4:]),int(CSScore[2:]),int(PhyScore[3:-1]))
    av = str(round(Total/3))+'\n'
    write = i[:-1]+' average:'+av
    FileAfter.write(write)

    
FileBefore.close()
FileAfter.close()
