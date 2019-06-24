#Bad Permutations
from itertools import permutations
#n_testcases=int(input())
l=[6,9]
# for _ in range(n_testcases):
#	l.append(int(input()))
factors=[]
for i in l:
	factors.clear()
	factors=[1]
	for j in range (2,i//2+1):
		if i%j==0:
			factors.append(j)
	factors.append(i)
	perm=list(permutations(factors))
	perm1=[]
	for t in perm:
		for ti in range(len(t)):
			ind=factors.index(t[ti])
			if ind+1<len(factors) and ti+1<len(t) and factors[ind+1]==t[ti+1]:
				perm1.append(t)
				break
	for t in perm1:
		perm.remove(t)
	print(len(perm))
