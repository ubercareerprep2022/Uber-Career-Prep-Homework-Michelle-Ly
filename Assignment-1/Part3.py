'''
Stacks 🥞🍓🍁

Implement the Stack class from scratch (do not use your 
language's standard stack or queue library/package methods). In this challenge, 
your Stack will only accept Integer values. Implement the following methods:

push() → Pushes an integer on top of the stack
pop() → Removes what is on the top of the stack, and returns that value to the caller
top() → Looks at the top value, and returns it. Does not manipulate the stack
isEmpty() → Returns True or False if the stack is Empty or not, respectively
size() → Returns an integer value with the count of elements in the stack

Note: Assumes all inputs are valid as integers

'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        if len(self.stack) <= 0:
            return True
        return False

    def size(self):
        if self.isEmpty():
            return 0
        return len(self.stack)

    def top(self):
        if self.isEmpty():
            return "Stack is empty, no top"
        return self.stack[-1]

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty, cannot pop from stack"
        value = self.stack[-1]
        del(self.stack[-1])
        return value


# Try top and size of empty stack
myStack = Stack()
print ("Top of stack:", myStack.top())
print ("Size of stack:", myStack.size())
print("\n")

myStack.push(42)
print ("Top of stack:", myStack.top())
print ("Size of stack:", myStack.size())
popped_value = myStack.pop()
print ("Popped value:", popped_value)
print ("Size of stack:", myStack.size())
print("\n")

# Try popping from empty stack
popped_value = myStack.pop()
print ("Popped value:", popped_value)
print("\n")

# Testing with more values
myStack.push(1)
myStack.push(20)
myStack.push(38)
myStack.push(41)
myStack.push(59)
print ("Top of stack:", myStack.top())
print ("Size of stack:", myStack.size())
# Pop 5
popped_value = myStack.pop()
print ("Popped value:", popped_value)
# Pop 4
popped_value = myStack.pop()
print ("Popped value:", popped_value)
print ("Top of stack:", myStack.top())
print ("Size of stack:", myStack.size())
myStack.push(78)
print ("Top of stack:", myStack.top())
print ("Size of stack:", myStack.size())
print("\n")

'''
Queues 🧇🫐🍁

Implement a Queue class from scratch that handles integers, with the following methods: 
enqueue() → adds an item to the queue
dequeue() → removes an item from the queue
rear() → returns the item at the end of the queue
front() → returns the item at the front of the queue
size() → returns the size of the queue
isEmpty() → returns whether or not the queue is empty

Note: Assumes all inputs are valid as integers
'''

class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        if len(self.queue) <= 0:
            return True
        return False

    def size(self):
        if self.isEmpty():
            return 0
        return len(self.queue)

    def front(self):
        if self.isEmpty():
            return "Queue is empty, no front"
        return self.queue[0]

    def rear(self):
        if self.isEmpty():
            return "Queue is empty, no rear"
        return self.queue[-1]

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty, cannot dequeue from queue"
        value = self.queue[0]
        del(self.queue[0])
        return value


# Try top and size of empty queue
myQueue = Queue()
print ("Front of queue:", myQueue.front())
print ("Rear of queue:", myQueue.rear())
print ("Size of queue:", myQueue.size())
print("\n")

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print ("Size of queue:", myQueue.size())
print ("Front of queue:", myQueue.front())
print ("Rear of queue:", myQueue.rear())
print("\n")

dequeued_value= myQueue.dequeue()
print ("Dequeued value:", dequeued_value)
print ("Size of queue:", myQueue.size())
print ("Front of queue:", myQueue.front())
print ("Rear of queue:", myQueue.rear())
print("\n")

dequeued_value= myQueue.dequeue()
print ("Dequeued value:", dequeued_value)
print ("Size of queue:", myQueue.size())
print ("Front of queue:", myQueue.front())
print ("Rear of queue:", myQueue.rear())
print("\n")

dequeued_value= myQueue.dequeue()
print ("Dequeued value:", dequeued_value)
print ("Size of queue:", myQueue.size())
print ("Front of queue:", myQueue.front())
print ("Rear of queue:", myQueue.rear())
print("\n")

# Try to dequeue from empty queue
dequeued_value= myQueue.dequeue()
print ("Dequeued value:", dequeued_value)
print ("Size of queue:", myQueue.size())
print("\n")
