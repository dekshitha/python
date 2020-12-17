fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
counts=dict()
for line in fh:
    line=line.rstrip()
    wds=line.split()
    if len(wds)<6:
        continue
    if wds[0] != 'From':
        continue
    else:

        count=count+1
        time=(wds[5])
        t=time.split(":")
        hrs=(t[0])
        counts[hrs]=counts.get(hrs,0)+1
lst=list()
for k,v in counts.items():
    newtup=(k,v)
    lst.append(newtup)
lst=sorted(lst)

for k,v in lst:
    print(k,v)
