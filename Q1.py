import random
#print(random.randint(90,100))

FileGrade = open('students.txt','w')

EnglishName = 'Daniel','Julian','Lisa','Shirley','Nico','Tim','James','Andy','Cathy','Brian','Harry','Jack'
ChineseName = 'Chu','Ye','Xu','Zeng','Jiang','Xing','Liu','Zhang','Yang','Shan','Fang','Jin'
MathTotal = 0
CSTotal = 0
PhyTotal = 0

for i in range(11):
    Math = random.randint(85,100)
    CS = random.randint(93,100)
    Phy = random.randint(83,100)
    MathTotal += Math
    CSTotal += CS
    PhyTotal += Phy
    write = EnglishName[i]+' '+ChineseName[i]+' Math'+str(Math)+' CS'+str(CS)+' Phy'+str(Phy) + '\n'
    FileGrade.write(write)

write = EnglishName[11]+' '+ChineseName[11]+' Math'+str(90*12-MathTotal)+' CS'+str(95*12-CSTotal)+' Phy'+str(88*12-PhyTotal)
FileGrade.write(write)

FileGrade.close()
