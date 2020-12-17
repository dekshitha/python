fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    line=line.rstrip()
    wds=line.split()
    if len(wds)<2:
        continue
    if wds[0] != 'From':
        continue
    else:
        words=wds[1]
        counts[words]=counts.get(words,0)+1
bigcount=None
bigword=None
for words,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=words
        bigcount=count
print(bigword,bigcount)    
