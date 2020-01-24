class node(object):
    def __init__(self,d,n = None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self,n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self,d):
        self.data = d

class LinkedList(object):
    def __init__(self,r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d):
        new_node = node(d, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self,d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()

List = LinkedList()
List.add(1)
List.add(2)
List.add(3)
List.add(4)
List.add(5)
print("size="+str(List.get_size()))
List.remove(3)
print("size="+str(List.get_size()))
print("Remove 8", List.remove(8))
print("size="+str(List.get_size()))
print("Find 8", List.find(8))
