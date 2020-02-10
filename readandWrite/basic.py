myfile =open('readandWrite/test.txt')
myfile.read()
# to read the file
myfile.read()
# we cant call read multiple times on file
#  the cursor goes till the end of the and show the file and show empty
myfile.seek(0) #reset the cursor position
myfile.read()

content = myfile.read()
content
print(content)
myfile.close()

# .readline() is method which help to read the files line by line
newOpen  = open('readandWrite/test.txt','w+') # it will peroform truncation in the original file
newOpen.read()
newOpen.seek(0)
newOpen.read()
newOpen.write('efscdfd')
