# Use the file name mbox-short.txt as the file name
tot=0.0
count=0.0
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('cant open file:',fh)
    quit()
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find(':')
    str=float(line[pos+1:])
    tot=tot+str
    count=count+1
print("Average spam confidence:",tot/count)
