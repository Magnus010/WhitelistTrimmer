import os

filename = "whitelist.txt"

with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]

uniqueContent = set(content)

print ("Length of original list: " + str(len(content)))
print ("Length of updated list: " + str(len(uniqueContent)))

newFilename = "whitelist.txt.new"

with open(newFilename, 'w') as f:
    for item in uniqueContent:
        f.write("%s\n" % item)
