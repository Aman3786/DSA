class node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class linkedlist:
	def __init__(self):
		self.head = None

	#add node at first location
	def insert_at_beginning(self, data):
		self.head = node(data, self.head)

	#add node at last location
	def insert_at_end(self, data):
		if not self.head:
			self.insert_at_beginning(data)
			return

		temp = self.head
		while temp.next:
			temp = temp.next

		temp.next = node(data)

	#add node at any location
	def insert_at_index(self, index, data):
		if not self.head or index==0:
			self.insert_at_beginning(data)
			return

		if index < 0 :
			if -(index) <= self.get_length()+1:	
				index = self.get_length()-(-(index)) + 1 
			else:
				self.insert_at_beginning(data)
				return

		if index>=1 and index<=self.get_length():
			temp = self.head
			counter = 0
			while temp:
				if counter == index-1:
					Node = node(data, temp.next)
					temp.next = Node
					return
				counter+=1
				temp = temp.next

		else:
			self.insert_at_end(data)

	def get_length(self):
		counter = 0
		temp = self.head
		while temp:
			counter+=1
			temp = temp.next
		print("Total length of linkedlist is, ", counter)
		return counter

	#remove node at first location
	def remove_first(self):
		if self.head:
			self.head = self.head.next
		else:
			print("no node in ll")
			return

	#remove node at last location
	def remove_last(self):
		if not self.head:
			print("no node in ll")
			return

		elif self.get_length()>1:
			temp = self.head
			while temp.next.next:
				temp = temp.next
			temp.next = None
			return

		elif self.get_length()==1:
			self.head = None

	#remove node at any location
	def remove_at_index(self, index):
		if not self.head:
			print("no node in ll to remove")
			return

		else:
			if index == 0:
				self.remove_first()
				return

			elif index>=1 and index<self.get_length():
				temp = self.head
				counter = 0
				while temp.next.next: 
					counter+=1
					if index == counter:
						break
					temp = temp.next
				temp.next = temp.next.next


	#display linkedlist in order
	def display(self):
		if not self.head:
			print("Empty linkedlist")

		temp = self.head
		while temp:
			print(temp.data,"-> ", end="")
			temp = temp.next

li = linkedlist()
li.insert_at_beginning(3)
li.insert_at_end(13)
li.insert_at_end(30)
li.insert_at_index(-2,32)
li.display()
li.remove_at_index(1)
print()
li.display()
