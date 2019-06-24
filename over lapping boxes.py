from operator import itemgetter
n = int(input())
l = []
for _ in range(n):
	l.append(list(map(int, input().split())))
boxes = []
for k in l:
	boxes.append(set([(i, j) for i in range(k[0], k[2]) for j in range(k[1], k[3])]))
#print(*boxes, sep="\n")
common = []

def findcommon(temp,val,chckd):
	if len(chckd)==len(boxes):
		common.append((len(temp),val))
	for i in range(len(boxes)):
		if i not in chckd:
			chckd.append(i)
			for j in chckd:
				temp1=boxes[j].intersection(boxes[i])
				if temp==temp:
					findcommon(temp,val+l[i][4],chckd)
				elif len(temp1)>=0:
					findcommon(temp1,val+[i][4],chckd)






#recursion
for i in range(len(boxes)):
	for j in range(i+1,len(boxes)):
		temp=boxes[i].intersection(boxes[j])
		if(len(temp)>0):
			chkd=[i,j]
			#common.append()
			findcommon(temp,l[i][4]+l[j][4],chkd)

print(max(common,key=itemgetter(1))[0])