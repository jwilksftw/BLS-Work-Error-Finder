import re
import glob
import os

os.chdir(r"C:\Users\wilkins_j\Desktop\textdocuments\livetext" )
outToFile = open('C:\Python27\oohlivehandsearch1.txt', mode='w')
outToFile.write('')
outToFile.close()
outToFile = open('C:\Python27\oohlivehandsearch2.txt', mode='w')
outToFile.write('')
outToFile.close()

#THE PROFILES HAVE THE TEXT YOU SEEK    

for file in glob.glob('*.txt'):
    with open(file) as f:
        
        outToFile= open('C:\Python27\oohlivehandsearch1.txt', 'a')
        contents = f.read()

        #median annual pay/median hourly pay, growth adjective, employment number and language, double space
        #patFinder1 = re.compile('\$\d+\,\d+|\$\d+\.\d+')
        #patFinder1 = re.compile('little or no change|decline\s\d+\s+|grow\s\d+\s+percent from 2012 to 2022,.*?occupations')
        #patFinder1 = re.compile('.*? held about .*? jobs in 2012.')
        #patFinder1 = re.compile('\w+  \w+|\d+  \d+')
        patFinder1 = re.compile('  ')

        findPat1 = re.search(patFinder1, contents)
        #print(findPat1.group())
        findPat1 = re.findall(patFinder1, contents)
        #print file
        outToFile.write(file+ '\n')
        outToFile.close()
        count=0
        for i in findPat1:
            
            print(i)
            print file
            outToFile= open('C:\Python27\oohlivehandsearch1.txt', 'a')
            outToFile.write(str(i)+ '\n')
            #outToFile.write(str(count)+'\n')
            outToFile.close()

'''

#THE PROFILES WITH NUMBERS TO BE CHECKED

for file in glob.glob('*.txt'):
    with open(file) as f:
        
        outToFile= open('C:\Python27\oohlivehandsearch1.txt', 'a')
        contents = f.read()

        
        patFinder1 = re.compile('\$\d+\,\d+|\$\d+\.\d+')
        #patFinder1 = re.compile('little or no change|decline\s\d+\s+|grow\s\d+\s+percent from 2012 to 2022,.*?occupations')
        #patFinder1 = re.compile('.*? held about .*? jobs in 2012.')
        #patFinder1 = re.compile('\w+  \w+|\d+  \d+')
        

        findPat1 = re.search(patFinder1, contents)
        #print(findPat1.group())
        findPat1 = re.findall(patFinder1, contents)
        #print file
        outToFile.write(file+ '\n')
        outToFile.close()
        count=0
        for i in findPat1:
            if count<1:
                count+=1
                print file + ' '+ str(i)
                #print(i)
            
                outToFile= open('C:\Python27\oohlivehandsearch1.txt', 'a')
                outToFile.write(str(i)+ '\n')
                #outToFile.write(str(count)+'\n')
                outToFile.close()
'''
'''            
            
#THE PROFILES ARE MISSING THE TEXT YOU SEEK     

for file in glob.glob('*.txt'):
    with open(file) as f:
        
        outToFile= open('C:\Python27\oohlivehandsearch1.txt', 'a')
        contents = f.read()

        #patFinder1 = re.compile('The median annual wage for .*? was .*? in May 2012.|The median hourly wage for .*? was .*? in May 2012.')
        #patFinder1 = re.compile('Employment of .*? is projected to grow .*? percent from 2012 to 2022')
        patFinder1 = re.compile('typically do the following:')
        #patFinder1 = re.compile('.*? held about .*? jobs in 2012.')
        #patFinder1 = re.compile('The median wage is the wage at which half the workers in an occupation earned more than that amount and half earned less.')
        #patFinder1 = re.compile('The lowest 10 percent earned less than .*?, and the top 10 percent earned more than .*?0.')


        findPat1 = re.search(patFinder1, contents)
        #print(findPat1.group())
        findPat1 = re.findall(patFinder1, contents)
        #print file
        outToFile.write(file)
        outToFile.close()
        count=0
        for i in findPat1:
            #count+=1
            #print(i)
            
            outToFile= open('C:\Python27\oohlivehandsearch1.txt', 'a')
            outToFile.write(str(i)+ '\n')
            #outToFile.write(str(count)+'\n')
            outToFile.close()        


f = open('C:\Python27\oohlivehandsearch1.txt')

strToSearch = ""

for line in f:
    strToSearch += line
    
patFinder1 = re.compile('\d+F.txtHand')

findPat1 = re.search(patFinder1, strToSearch)
#print(findPat1.group())
findPat1 = re.findall(patFinder1, strToSearch)
outToFile = open('C:\Python27\oohlivehandsearch2.txt', mode='w')        
outToFile.write(str(findPat1))
outToFile.close()

f = open('C:\Python27\oohlivehandsearch2.txt')
strToSearch = ""

for line in f:
    print line
    strToSearch += line
'''
