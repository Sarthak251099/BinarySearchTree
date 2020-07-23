class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root==None:
            self.root = Node(value)
            print(f"Value {value} added to root")
            return
        else:
            self.insert2(value,self.root)

    def insert2(self,value,curr_node):
        if value<curr_node.data:
            if curr_node.left ==None:
                curr_node.left = Node(value)
                print(f"Value {value} added to tree")
            else:
                self.insert2(value,curr_node.left)
        else:
            if curr_node.right == None:
                curr_node.right = Node(value)
                print(f"Value {value} added to tree")
            else:
                self.insert2(value,curr_node.right)
    
    def printInorder(self):
        if self.root == None:
            print("This tree has no Nodes to print")
        else:
            self.printInorder2(self.root)
    
    def printInorder2(self,curr_node):
        if curr_node!=None:
            self.printInorder2(curr_node.left)
            print(curr_node.data, end = " ")
            self.printInorder2(curr_node.right)
    
    def printPostorder(self):
        if self.root == None:
            print("This tree has no Nodes to print")
        else:
            self.printPostorder2(self.root)
    
    def printPostorder2(self,curr_node):
        if curr_node!=None:
            self.printPostorder2(curr_node.left)
            self.printPostorder2(curr_node.right)    
            print(curr_node.data, end = " ")
    
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:   return 0
    
    def _height(self,cur_node,cur_height):
        if cur_node==None:
            return cur_height
        left_height = self._height(cur_node.left,cur_height+1)
        right_height = self._height(cur_node.right,cur_height+1)
        return max(left_height,right_height)

        
    
tree = BinarySearchTree()
tree.insert(10)
tree.insert(20)
tree.insert(3)
tree.insert(16)
tree.insert(22)
print(tree.height())
tree.printInorder()
print()
tree.printPostorder()

           