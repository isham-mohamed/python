n = int(input())
l = []
for _ in range(n):
	l.append(list(map(int, input().split())))
boxes = []
for k in l:
	boxes.append(set([(i, j) for i in range(k[0], k[2]) for j in range(k[1], k[3])]))
print(*boxes, sep="\n")
common = []

for i in range(len(boxes) + 1):
	for j in range(i + 1, len(boxes)):
		if len(boxes[i].intersection(boxes[j])) > 0:
			temp = boxes[i].intersection(boxes[j])
			common.append((len(temp), l[i][4] + l[j][4]))
			settemp = [i, j]
			for k in range(len(boxes)):
				if k not in settemp:
					if temp.intersection(boxes[k]) > 0:
						x = temp.intersection(boxes[k])
						if x in common:
							y = common.index(x)
							common[y][1] = common[y][2] + l[k][4]
							common[y][0] += len(temp)
						else:
							common.append(len(x), )
#testing123123
print(common)