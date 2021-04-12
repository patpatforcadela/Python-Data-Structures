class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self, root):
        spaces = " " * root.getLevel() * 3
        string = spaces + "|--"
        print(string + root.data)
        if root.children:
            for item in root.children:
                self.printTree(item)

root = Tree("Nilupul")

chinmay = Tree("Chinmay")
vishwa = Tree("Vishwa")
vishwa.addChild(Tree("Dhaval"))
vishwa.addChild(Tree("Abhijit"))
chinmay.addChild(vishwa)
chinmay.addChild(Tree("Aamir"))
gels = Tree("Gels")
gels.addChild(Tree("Peter"))
gels.addChild(Tree("Waqas"))
root.addChild(chinmay)
root.addChild(gels)
root.printTree(root)