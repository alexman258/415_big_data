


"""
Parse the full amazon-meta.txt

Format of Data:
['ASIN', 'title', 'group', 'salesrank', 'numsimilar', 'similar', 'categories', 'totalreviews','avgrating']
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

    file = open("amzn123.txt","w", encoding='utf8')
    previouslines = ['ASIN', 'title', 'group', 'salesrank', 'numsimilar', 'similar', 'categories', 'totalreviews', 'avgrating']
    for line in content:

        lines = line.split(':')
    
        if lines[0] == 'ASIN':
            writeToFile(file, previouslines, 9)
            previouslines = []
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

    file.close()


"""
Parses a the amazon-meta.txt depending on the group.
Inputting "book" will parse all the products with the group label "book"

Content is .readlines() output of the amazon-meta.txt file with
all beginning and trailing white spaces stripped.
"""
def parseGroup(content, groupName):
    file = open(groupName+".txt","w", encoding='utf8')
    previouslines = ['ASIN', 'title', 'salesrank', 'avgrating']
    for line in content:

        lines = line.split(':')
    
        if lines[0] == 'ASIN':
            writeToFile(file, previouslines, 4)
            previouslines = []
            previouslines.append(lines[1].strip())

        elif lines[0] == 'title':
            title = ':'.join(lines[1:]).strip().replace(',', ' ').replace('\n', ' ').strip()
            previouslines.append(title)

        elif lines[0] == 'group':
            #print(lines[1].strip())
            if lines[1].strip() != groupName:
                previouslines = []
                continue

        elif lines[0] == 'salesrank':
            previouslines.append(lines[1].strip())

        elif lines[0] == "reviews" and lines[1].strip() == "total":
            previouslines.append(lines[4].strip())
        else:
            continue

    file.close()

def writeToFile(file, prevLines, expectedLen):
    if(len(prevLines) == expectedLen):
        for component in prevLines[0:(expectedLen-1)]:
            file.write(component)
            file.write(',')
        file.write(prevLines[expectedLen-1])
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
    file = open("similar.txt","w", encoding='utf8')

    asin = ''
    similarAsin = ''
    file.write(asin)
    file.write(',')
    file.write(similarAsin)
    file.write('\n')
    for line in content:
        
        lines = line.split(':')

        if lines[0] == 'ASIN':
            asin = lines[1].strip()

        if lines[0] == 'similar':
            similarList = lines[1].strip().split()
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
groupToParse = "Book"
#parseAll(content)
#parseSimilar(content)
parseGroup(content,groupToParse)

