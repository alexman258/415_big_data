fname = "amazon-meta.txt"



def doParse(fileName):
    with open(fileName, encoding = 'ISO-8859-1') as f:
        content = f.readlines()
    #Remove the beginning and trailing white spaces.
    content = [x.strip() for x in content] 

    file = open("amzn.txt","w", encoding='utf8')
    previouslines = ['Id', 'ASIN', 'title', 'group', 'salesrank', 'numsimilar', 'similar', 'categories', 'totalreviews', 'avgrating']
    writeToFile(file, previouslines)
    for line in content:
        
        lines = line.split(':')
        if lines[0] == 'Id':
            previouslines.append(lines[1].strip())
    
        if lines[0] == 'ASIN':
            previouslines.append(lines[1].strip())

        if lines[0] == 'title':
            title = ':'.join(lines[1:]).strip().replace(',', ' ').replace('\n', ' ').strip()
            previouslines.append(title)

        if lines[0] == 'group':
            previouslines.append(lines[1].strip())

        if lines[0] == 'salesrank':
            previouslines.append(lines[1].strip())

        if lines[0] == 'similar':
            similarList = lines[1].strip().split()
            #print(similarList)
            #print(type(similarList))
            if len(similarList) == 1:
                previouslines.append('-1')
                previouslines.append('-1')
            else:
                previouslines.append(similarList[0])
                previouslines.append(' '.join(similarList[1:]))

        if lines[0] == 'categories':
            previouslines.append(lines[1].strip())

        if lines[0] == "reviews" and lines[1].strip() == "total":
            previouslines.append(lines[2].split(' ')[1])
            previouslines.append(lines[4].strip())
            writeToFile(file, previouslines)
            previouslines = []

    file.close()



def writeToFile(file, prevLines):
    if(len(prevLines) == 10):
        for component in prevLines[0:9]:
            file.write(component)
            file.write(',')
        file.write(prevLines[9])
        file.write('\n')

# start
doParse(fname)