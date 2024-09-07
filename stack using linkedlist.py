class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class stack:
    def _init_(self):
        self.head=None
        self.tail=None
    def push(self,data):
        if(self.head==None):
            self.head=node(data)
        else:
            newnode=node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        self.head=self.head.next
    def peek(self):
        print(self.head.data)
    def display(self):
        temp=self.head
        while(temp!=None):
             print(temp.data,id(temp.next))
             temp=temp.next
obj=stack()
n=int(input())
for i in range(n):
    m=int(input())
    obj.push(m)
obj.display()
obj.pop()
obj.display()
obj.peek()
obj.display()
