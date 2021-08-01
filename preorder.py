class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None



    def preorder(root):
        if root != None:
            print(root,end = " ")
            preorder(root.left):