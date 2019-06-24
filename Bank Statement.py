interest=input()
n=int(input())
l=[]
for _ in range (n-2):
    l.append(input().split())
for i in l:
    i[0]=int(i[0])
    i[1]=int(i[1])
    i[3]=int(i[3])
ifrd=float(input())
sum1=0
for i in l:
    sum1+=float(i[3])*(0.08/365)
pinerest=ifrd-sum1
i=1
while(i==int(l[i-1][0])):
    i+=1
i=i-3
result=[]
if(l[i+2][2]=='debit'):
    u=l[i + 2][3]+l[i + 2][1]
    pu = float(u) * (.08 / 365)
else:
    u = l[i + 2][3]-l[i + 2][1]
    pu = float(u) * (.08 / 365)
py=pinerest-pu
y=float(py)/(0.08/365)
if(u>y):
    result.append([i+4,int(u-y),'credit',u])
else:
    result.append([i+4,int(y-u),'debit',u])
if(l[i+1][3]<y):
    result.append([i + 3, round(y-l[i+1][3]), 'credit',round(y)])
else:
    result.append([i + 3,(l[i+1][3]-y), 'debit', round(y)])
result.reverse()
print(*result,sep='\n')






