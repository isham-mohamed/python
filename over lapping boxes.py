n=int(input())
l=[]
for _ in range(n):
	l.append(list(map(int,input().split())))
boxes=[]
for k in l:
	boxes.append(set([(i,j) for i in range (k[0],k[2]) for j in range(k[1],k[3])]))
print(*boxes,sep="\n")
common=[]
def findcommon(l,area,val,cb):
	for i in boxes:
		test=i.itersec
		for i boxes
		if i.intersection()


findcommon()
print(common)