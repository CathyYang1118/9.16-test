FileBefore = open('students.txt','r')
FileAfter = open('ID.txt','w')

ID = 1
for i in FileBefore.readlines():
    write = str(ID)+' '+i
    FileAfter.write(write)
    ID += 1
FileBefore.close()
FileAfter.close()
