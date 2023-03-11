class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return None if self.root == None else self.root.search(key)

    def insert(self, key):
        if self.root == None:
            self.root = BinarySearchTreeNode(key)
        else:
            self.root.insert(key)

    def delete(self, key):
        if self.root != None:
            self.root = self.root.delete(key)

    def list(self):
        return [] if self.root == None else self.root.list()

    def print_tree(self):
        if self.root == None:
            print('None')
        else:
            self.__lines = []
            self.__add_to_lines(self.root, 0)
            for l in self.__lines:
                print(l)

    def __add_to_lines(self, node, depth):
        if node == None:
            return

        self.__add_to_lines(node.L, depth+1)

        while len(self.__lines) <= depth:
            self.__lines.append('')
        for _ in range(len(self.__lines[depth]), len(max(self.__lines, key=len))):
            self.__lines[depth] += ' '
        self.__lines[depth] += str(node.key)

        self.__add_to_lines(node.R, depth+1)

class BinarySearchTreeNode:
    def __init__(self, key):
        self.key = key
        self.L = None
        self.R = None

    def search(self, key):
        if self.key == key:
            return self

        if key < self.key:
            return None if self.L == None else self.L.search(key)
        else:
            return None if self.R == None else self.R.search(key)

    def insert(self, key):
        if key < self.key:
            if self.L == None:
                self.L = BinarySearchTreeNode(key)
            else:
                self.L.insert(key)
        else:
            if self.R == None:
                self.R = BinarySearchTreeNode(key)
            else:
                self.R.insert(key)

    def delete(self, key):
        if key < self.key and self.L != None:
            self.L = self.L.delete(key)
        elif self.key < key and self.R != None:
            self.R = self.R.delete(key)

        if key != self.key:
            return self
        if self.L == None:
            return self.R

        max_node_parent = self.L.max_node_parent()
        if max_node_parent == None:
            self.L.R = self.R
            return self.L
        max_node = max_node_parent.R
        max_node_parent.R = max_node.L
        max_node.L = self.L
        max_node.R = self.R
        return max_node

    def max_node_parent(self):
        if self.R == None:
            return None
        if self.R.R == None:
            return self
        return self.R.max_node_parent()

    def list(self):
        tmp = []
        if self.L != None:
            tmp += self.L.list()
        tmp.append(self.key)
        if self.R != None:
            tmp += self.R.list()
        return tmp
