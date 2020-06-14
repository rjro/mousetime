class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value
    
    def __str__(self):
        return str(self.value)

a= Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.prev = a
b.next = c
c.prev = b

node = c

while node.prev is not None:
    print(node)
    node = node.prev

print("----")

print(node)
print(node.next)
print(node.next.next)