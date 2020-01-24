class Stack():
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def get_stack(self):
        return self.items
    
s = Stack()
print(s.is_empty())
s.push("A")
s.push("B")
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.is_empty())
