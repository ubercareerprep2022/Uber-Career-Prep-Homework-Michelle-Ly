'''
[Trees - Ex1] Exercise: Printing a tree
Implement a method called print() to print the values of the data in all the TreeNodes in a Tree above. 
For example, running print() on the Tree above should produce one of the three values below:

1 7 17 6 3
7 1 6 17 3
7 6 3 17 1 

(Hint - think recursively!)
'''

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


root = Node(1)
root.left = Node(7)
root.right = Node(17)
root.right.left = Node(6)
root.right.right = Node(3)

def print_tree(root):
    if root.left:
        print_tree(root.left)
    print(root.data),
    if root.right:
        print_tree(root.right)
    
    
def print_tree2(root):
    if (root == None):
        return
    print_tree2(root.left)
    print(root.data)
    print_tree2(root.right)
    

print_tree(root)
print("**********")
print_tree2(root)
    