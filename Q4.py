FileBefore = open('ID.txt','r')
FileAfter = open('Q4.txt','w')

for i in FileBefore.readlines():
    j = i.split(' ')
    if j[1] == 'Daniel':
        Math = j[3]
        MathScore = round(int(Math[4:])*1.1 )         
        write = str(i[0:12])+' Math'+str(MathScore)+str(i[19:])
    else:
        write = i
    FileAfter.write(write)

    
FileBefore.close()
FileAfter.close()
