class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class link:
	def __init__(self):
		self.head=node()
	def append(self,data):
		new_node =node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	def length(self):
		cur= self.head
		t=0
		while cur.next!=None:
			cur=cur.next
			t+=1
		return t

	def disp(self):
		e=[]
		cur = self.head
		while cur.next!=None:
			cur=cur.next
			e.append(cur.data)
		print(e)

a=link()
a.disp()
a.append(1)
a.append(2)
a.disp()
print(a.length())