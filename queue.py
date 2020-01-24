class Stack:
	def __init__(self):
		self.Max = 6
		self.arr = [None]*self.Max
		self.front = 0
		self.rear = -1
		self.items = 0
	
	def peek(self):
		print('Element at front', self.arr[self.front])

	def isEmpty(self):
		return self.items == 0
	
	def isFull(self):
		return self.items == self.Max

	def size(self):
		return self.items

	def insert(self, data):
		if not (self.items == self.Max):
			if(self.rear == self.Max-1):
				self.rear = -1
		self.rear+=1		
		self.arr[self.rear] = data
		self.items+=1

	def remove(self):
		data = self.arr[self.front]
		self.front+=1
		if self.front == self.Max:
			self.front = 0
		self.items-=1
		print("%d removed" %(data)) 

		
stack = Stack()
stack.peek()
stack.insert(10)
stack.insert(20)
stack.insert(30)
stack.insert(40)
stack.insert(50)
stack.insert(60)
if stack.isFull():
	print("Queue Full")
stack.peek()
stack.remove()
stack.remove()
stack.remove()
stack.insert(60)
stack.peek()
