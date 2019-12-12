


"""
Parse the full amazon-meta.txt

Format of Data:
['Id', 'ASIN', 'title', 'group', 'salesrank', 'numsimilar', 'similar', 'categories', 'totalreviews','avgrating']
Id          -   Starts at 1 and increments
ASIN        -   Amazon Identification number
title       -   The name of the item
group       -   Which group the item belongs to. (eg, book, musicm etc)
numsimilar  -   The number of items that are similar to it.
similar     -   The ASIN's of the items similar to it. Delimited by a space.
                This is mainly to be used when populating the graph of the network.
categories  -   Currently stores the number of categories. Not all the different categories associated with that item.
totalreviews-   Number of reviews an item has.
avgrating   -   The average rating of that item.

Saves the data into CSV format.
"""
def parseAll(content):        

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
            writeToFile(file, previouslines, 10)
            previouslines = []

    file.close()




def writeToFile(file, prevLines, expectedLen):
    if(len(prevLines) == expectedLen):
        for component in prevLines[0:9]:
            file.write(component)
            file.write(',')
        file.write(prevLines[9])
        file.write('\n')

def openAndStrip(fileName):
    print('Opening file')
    with open(fileName, encoding = 'ISO-8859-1') as f:
        content = f.readlines()
    #Remove the beginning and trailing white spaces.
    print('cleaning file contents')
    content = [x.strip() for x in content] 
    return content



"""
The purpose of this function is to flatten out the data for similar items.
Outputs data in the following format: [SourceASIN, SimilarASIN]

SourceASIN  -   The ASIN of the current item.
SimilarASIN -   The ASIN of the file similar to it.

Example:
ASIN: 123
Number of similar items: 3
Similar Items: zyx abc asdf

The output would look like this:
SourceASIN | SimilarASIN
123        | xyz
123        | abc
123        | asdf
"""
def parseSimilar(content):
    file = open("testSimilar.txt","w", encoding='utf8')
    previouslines = ['ASIN', 'similar']
    #writeToFile(file, previouslines, 2)
    asin = ''
    similarAsin = ''
    for line in content:
        
        

        lines = line.split(':')

        if lines[0] == 'ASIN':
            asin = lines[1].strip()

        if lines[0] == 'similar':
            similarList = lines[1].strip().split()
            #print(similarList)
            #print(type(similarList))
            if len(similarList) == 1:
                continue
            else:
                for item in similarList[1:]:
                    similarAsin = item
                    file.write(asin)
                    file.write(',')
                    file.write(similarAsin)
                    file.write('\n')
    file.close()
        
# start

fname = "amazon-meta.txt"
content = openAndStrip(fname)

#parseAll(content)
parseSimilar(content)