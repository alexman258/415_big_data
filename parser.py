fname = "amazon-meta.txt"
with open(fname, encoding = 'ISO-8859-1') as f:
    content = f.readlines()
#Remove the beginning and trailing white spaces.
content = [x.strip() for x in content] 

file = open("file.csv","w", encoding='utf8')
previouslines = ['Id', 'ASIN', 'title', 'group', 'salesrank', 'categories', 'totalreviews', 'avgrating']
for line in content:
    lines = line.split(':')
    if lines[0] == 'Id':
        if(len(previouslines) == 8):
            for component in previouslines[0:7]:
                file.write(component)
                file.write(',')
            file.write(previouslines[7])
            file.write('\n')
        previouslines = []
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

   #if lines[0] == 'similar':
   #Add code to add list of similar categories

    if lines[0] == 'categories':
        previouslines.append(lines[1].strip())

    if lines[0] == "reviews" and lines[1].strip() == "total":
        previouslines.append(lines[2].split(' ')[1])
        previouslines.append(lines[4].strip())

file.close()
