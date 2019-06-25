valid_char=[str(i) for i in range(10)]+['-']
valid_strt=['4','5','6']
def validity(s):
	slen=len(s)
	if slen>19 or slen<16 or s[0] not in valid_strt:
		return 0
	ls = list(s)
	count=0
	item=ls[0]
	for i in range(len(ls)) :
		if ls[i] not in valid_char:
			return 0
		if ls[i]=='-':
			if i not in [9,4,14]:
				return 0
		else:
			if count==4:
				return 0
			else:
				if ls[i]==item:
					count+=1
				else:
					count=1
					item=ls[i]



##Driver code
n=int(input())
l=[]
for _ in range(n):
	l.append(input())
for i in l:
	out=validity(i)
	if out == 0:
		print("Invalid")
	else:
		print("Valid")

