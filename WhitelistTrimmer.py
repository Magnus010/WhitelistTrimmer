import os

# Original whitelist
filename = "whitelist.txt"

# Load  file as list
with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Update list to set, to remove duplicates
uniqueContent = set(content)

# Ensure new container has less than old container
print ("Length of original list: " + str(len(content)))
print ("Length of updated list: " + str(len(uniqueContent)))

newFilename = "whitelist.txt.new"

# Create new file, load with set
with open(newFilename, 'w') as f:
    for item in uniqueContent:
        f.write("%s\n" % item)
