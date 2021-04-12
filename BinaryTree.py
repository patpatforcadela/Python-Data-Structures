from collections import deque

class BinarySearchTree:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def addChild(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTree(data)

    def delete(self, value):
        if value < self.data:
            self.left = self.left.delete(value)
        elif value > self.data:
            self.right = self.right.delete(value)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.left is not None:
                return self.right
            elif self.right is not None:
                return self.left
            else:
                min_val = self.right.findMin()
                self.data = min_val
                self.right = self.right.delete(min_val)
            return self

    def search(self, data):
        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def findMin(self):
        temp = self
        while temp.left:
            temp = temp.left
        return temp.data

    def findMax(self):
        temp = self
        while temp.right:
            temp = temp.right
        return temp.data

    def findHeight(self, root):
        if root is None:
            return -1
        left_height = self.findHeight(root.left)
        right_height = self.findHeight(root.right)
        return max(left_height, right_height) + 1

    def calculateSum(self, root):
        if root is None:
            return 0
        total = 0
        total += self.data
        if self.left:
            total += self.left.calculateSum(self.left)
        if self.right:
            total += self.right.calculateSum(self.right)
        return total

    def find(self, value):
        if value < self.data:
            return self.left.find(value)
        elif value > self.data:
            return self.right.find(value)
        else:
            return self

    def invert(self):
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.invert()
        if self.right:
            self.right.invert()

    def find_successor(self, root, value):
        current = self.find(value)
        if current is None:
            return None
        if current.right:
            return current.right.findMin()
        else:
            successor = None
            ancestor = root
            while ancestor != current:
                if current.data < ancestor.data:
                    successor = ancestor.data
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor

    def breadth_first(self, node):
        elements = []
        dq = deque()
        dq.append(node)
        while len(dq) != 0:
            if dq[0].left:
                dq.append(dq[0].left)
            if dq[0].right:
                dq.append(dq[0].right)
            elements.append(dq[0].data)
            dq.popleft()
        return elements

    def inOrder(self):
        elements = []
        if self.left:
            elements += self.left.inOrder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrder()
        return elements

    def preOrder(self, root):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.inOrder()
        if self.right:
            elements += self.right.inOrder()
        return elements

    def postOrder(self, root):
        elements = []
        if self.left:
            elements += self.left.inOrder()
        if self.right:
            elements += self.right.inOrder()
        elements.append(self.data)
        return elements

root = BinarySearchTree(10)
root.addChild(4)
root.addChild(12)
root.addChild(8)
root.addChild(11)
root.addChild(17)