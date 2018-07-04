class Node:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_child):
        if self.left_child == None:
            self.left_child = BinaryTree(new_child)
        else:
            t = BinaryTree(new_child)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_child):
        if self.right_child == None:
            self.right_child = BinaryTree(new_child)
        else:
            t = BinaryTree(new_child)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_val(self):
        return self.key

    def set_root_val(self, obj):
        self.key = obj

r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
rb = r.get_left_child()
rb.insert_right('d')
rc = r.get_right_child()
rc.insert_left('e')
rc.insert_right('f')

print(r.key)
print(r.left_child.key)
print(rb.key)
print(rb.right_child.key)
print(r.right_child.key)
