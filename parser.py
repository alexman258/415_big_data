fname = "amazon-meta.txt"
with open(fname, encoding = 'utf8') as f:
    content = f.readlines()
#Remove the beginning and trailing white spaces.
content = [x.strip() for x in content] 

# Write extracted information to testfile.txt in a format of ',' demilited files.
# The columns are Id, title, group, categories, totalreviews, avgrating.
# The code stores all extracted information about a product into previoulines,
# and write the content into file only when all information are available. Hence,
# if review information for a product is not available, the product won't appear
# in the final file.
file = open("file.txt","w", encoding='utf8')
previouslines = ['Id', 'title', 'group', 'categories', 'totalreviews', 'avgrating']
for line in content:
    lines = line.split(':')
    if lines[0] == "Id":
        if (len(previouslines) == 6):
            for component in previouslines[0:5]:
                file.write(component)
                file.write(',')
            file.write(previouslines[5])
            file.write("\n")
        previouslines = []
        previouslines.append(lines[1].strip())
        
    if lines[0] == "title":
        title = ':'.join(lines[1:]).strip().replace(',', ' ').replace('\n', ' ').strip()
        previouslines.append(title)
       
    if lines[0] == "group":
        previouslines.append(lines[1].strip())

    if lines[0] == "categories":
        previouslines.append(lines[1].strip())
    
    if lines[0] == "reviews" and lines[1].strip() == "total":
        previouslines.append(lines[2].split(' ')[1])
        previouslines.append(lines[4].strip())
file.close()