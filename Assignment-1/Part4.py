'''
Linked Lists 🔗

Implement a Singly Linked List class with the following methods:

void push(<Node> node) → Adds the node to the end of the list
<Node> pop() → Removes the last node at the end of the linked list, returns that data
void insert(uint index,<Node> node) → Adds a single node containing data to a chosen location in the list. 
    If the index is above the size of the list, do nothing
void remove(uint index) → remove/delete a single node at the index location in the list. 
    If the node doesn't exist at the index, do nothing
<Node> elementAt(uint index) → Returns a pointer to the node at the index location in the list. 
    If the node doesn't exist at the index, return nil/null
uint size() → Returns the length of the list.
void printList() → Returns a string representation of the linked list

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            curr.next = Node(data)
    
    def pop(self, data):
        if (self.head == None):
            return "List is empty"
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            end = curr
            # remove last one
            return end

    def remove(self, index):
        if (index < 0 or index >= self.size()):
            print("Index not in bounds")
            return
        count = 0
        if (index == 0):
            temp = self.head
            self.head = self.head.next
            del(temp)
        else:
            curr = self.head
            while(curr.next and count < index - 1):
                curr = curr.next
                count += 1
            temp = curr.next.next
            del(curr.next)
            curr.next = temp


            del(temp)
        
    def insert(self, data, index):
        if (index < 0 or index >= self.size()):
            print("Index not in bounds")
            return
        count = 0
        new = Node(data)
        if (index == 0):
            new.next = self.head
            self.head = new
        else:
            curr = self.head
            while(curr.next and count < index - 1):
                curr = curr.next
                count += 1
            temp = curr.next
            curr.next = new
            new.next = temp
        
    def size(self):
        count = 1
        if (self.head == None):
            return 0
        else:
            curr = self.head
            while(curr.next):
                count += 1
                curr = curr.next
        return count

    def elementAt(self, index):
        if (index < 0 or index >= self.size()):
            print("Index not in bounds")
            return
        count = 0
        curr = self.head
        while (curr.next and count < index):
            count += 1
            curr = curr.next
        return curr

    def printList(self):
        if (self.head == None):
            return "List is empty"
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

list = LinkedList()

# Not in bounds
list.remove(0)
print("Size of list:", list.size())
list.printList()
print("\n")

list.push(3)
list.push(9)
list.push(8)
list.push(2)
list.push(1)
print("Size of list:", list.size())
list.printList()
print("\n")

list.insert(0, 3)
print("Size of list:", list.size())
list.printList()
print("\n")

list.insert(65, 1)
print("Size of list:", list.size())
list.printList()
print("\n")

# Not in bounds
print(list.elementAt(70))
# In bounds
print((list.elementAt(3)).data)
print("\n")

list.remove(0)
print("Size of list:", list.size())
list.printList()
print("\n")

list.remove(4)
print("Size of list:", list.size())
list.printList()





