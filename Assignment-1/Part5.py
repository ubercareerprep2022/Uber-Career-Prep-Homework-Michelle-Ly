'''
Implement reverseLinkedList() which takes in a linked list and returns a new linked list 
with the same elements in reverse order. For example, if the representation of your 
Linked List is “1, 2, 3, 4”, then reversing it would return “4, 3, 2, 1”.

We have identified three main methodologies for achieving this solution, and we want to 
challenge you to build all three:

Iteratively
    In this context, “iteratively” means “looping through the data set”. Therefore, our solution 
    should have a time complexity of O(n) and a space complexity of O(1).
Using a stack
    Leaning on our knowledge of stacks, can you think of a way to utilize a stack to solve 
    this problem with a time complexity of O(n)?
Recursively
    Read up on recursion, and then apply that knowledge to come up with another version of this algorithm.

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

def printList(temp):
    string = ""
    while(temp):
        string = string + str(temp.data) + " "
        temp = temp.next
    print(string)

# Iteratively
def iterative_reverse(node):
    prev = None
    while node:
        n = node.next
        node.next = prev
        prev = node
        node = n
    return prev

# Stack
def stack_reverse(node):
    stack = []
    if (node == None or node.next == None):
        return node
    while (node):
        stack.append(node)
        node = node.next
    temp = stack.pop()
    head = temp
    for i in range (0, len(stack)):
        temp.next = stack.pop()
        temp = temp.next
    temp.next = None
    return head

# Recursively
def recursive_reverse(node):
    if (node == None or node.next == None):
        return node
    temp = recursive_reverse(node.next)
    node.next.next = node
    node.next = None
    return temp

# Test recursive
list = LinkedList()
for i in range (1, 5):
    list.push(i)
printList(list.head)

temp = recursive_reverse(list.head)
printList(temp)

# Test stack
list1 = LinkedList()
for i in range (1, 5):
    list1.push(i)
printList(list1.head)

temp1 = stack_reverse(list1.head)
printList(temp1)

# Test iterative
list2 = LinkedList()
for i in range (1, 5):
    list2.push(i)
printList(list2.head)

temp2 = iterative_reverse(list2.head)
printList(temp2)







