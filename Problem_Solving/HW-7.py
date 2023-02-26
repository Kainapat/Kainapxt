class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
            return self
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
            return self
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            min_right = self.right
            while min_right.left:
                min_right = min_right.left
            self.data = min_right.data
            self.right = self.right.delete(min_right.data)
            return self        
    
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " is found"
    
    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)
root.PrintTree()
print(root.findval(7))  
print(root.findval(35))  
print("Before deleting 35:")
root.PrintTree()

root = root.delete(35)

print("After deleting 35:")
root.PrintTree()

print("Preorder Traversal:")
root.preorder(root)
print("Inorder Traversal:")
root.inorder(root)
print("Postorder Traversal:")
root.postorder(root)