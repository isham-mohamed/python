#Bad Permutations
from itertools import permutations
#n_testcases=int(input())
l=[9]
#for _ in range(n_testcases):
#	l.append(int(input()))
factors=[]
for i in l:
	factors.clear()
	factors=[0,1]
	for j in range (2,i//2):
		if i%j==0:
			factors.append(j)
	perm=list(permutations(factors))
	print(factors)
	print(perm)
