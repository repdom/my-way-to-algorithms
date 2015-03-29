import operator

data=[]
for l in open('jobs.txt'):
    l = [int(x) for x in l.strip().split(' ')]
    if len(l)>1:
    	l.append(l[0]-l[1])
    data.append(l)

data = data[1:]
data.sort(key=operator.itemgetter(2,0),reverse=True)

res, tmp = 0, 0
for x in data:
    res=res+x[0]*(tmp+x[1])
    tmp=tmp+x[1]
print res