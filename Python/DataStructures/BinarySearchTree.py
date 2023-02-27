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
        if self.root == None:
            return False
        if self.root.key == key:
            if self.root.L == None:
                self.root = self.root.R
                return True
            max_node_parent = self.root.L.max_node_parent()
            if max_node_parent == None:
                self.root.L.R = self.root.R
                self.root = self.root.L
                return True
            max_node = max_node_parent.R
            max_node_parent.R = max_node.L
            max_node.L = self.root.L
            max_node.R = self.root.R
            self.root = max_node
            return True
        return self.root.delete(key)

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
        if key < self.key:
            if self.L == None:
                return False
            if self.L.key != key:
                return self.L.delete(key)
            del_node = self.L
            if del_node.L == None:
                self.L = del_node.R
                return True
        else:
            if self.R == None:
                return False
            if self.R.key != key:
                return self.R.delete(key)
            del_node = self.R
            if del_node.L == None:
                self.R = del_node.R
                return True

        max_node_parent = del_node.L.max_node_parent()
        if max_node_parent == None:
            del_node.L.R = del_node.R
            if key < self.key:
                self.L = del_node.L
            else:
                self.R = del_node.L
            return True

        max_node = max_node_parent.R
        max_node_parent.R = max_node.L
        max_node.L = del_node.L
        max_node.R = del_node.R
        if key < self.key:
            self.L = max_node
        else:
            self.R = max_node
        return True

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
