# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Invalid file name')
    quit()   
for words in fh:
    words=words.rstrip()
    str=words.upper()
    print(str)
