class AVLTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return None if self.root == None else self.root.search(key)

    def insert(self, key):
        self.root = AVLTreeNode(key) if self.root == None else self.root.insert(key)

    def delete(self, key):
        if self.root != None:
            self.root = self.root.delete(key)

    def list(self):
        return [] if self.root == None else self.root.list()

    def print_tree(self, print_height=False):
        if self.root == None:
            print('None')
        else:
            self.__print_height = print_height
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
        self.__lines[depth] +=  str(node.key)
        if self.__print_height:
            self.__lines[depth] += '[' + str(node.height) + ']'

        self.__add_to_lines(node.R, depth+1)

class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.L = None
        self.R = None
        self.height = 1

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
                self.L = AVLTreeNode(key)
                self.height = 2
                return self
            pre_height = self.L.height
            self.L = self.L.insert(key)
            if pre_height == self.L.height:
                return self
            self.height = self.__calc_height()
            if self.R == None or self.R.height - self.L.height <= -2:
                return self.__rotate_Right()
            return self
        else:
            if self.R == None:
                self.R = AVLTreeNode(key)
                self.height = 2
                return self
            pre_height = self.R.height
            self.R = self.R.insert(key)
            if pre_height == self.R.height:
                return self
            self.height = self.__calc_height()
            if self.L == None or +2 <= self.R.height - self.L.height:
                return self.__rotate_Left()
            return self

    def delete(self, key):
        if key < self.key:
            if self.L == None:
                return self
            self.L = self.L.delete(key)
            self.height = self.__calc_height()
            return self if self.__calc_balance() <= +1 else self.__rotate_Left()
        elif self.key < key:
            if self.R == None:
                return self
            self.R = self.R.delete(key)
            self.height = self.__calc_height()
            return self if -1 <= self.__calc_balance() else self.__rotate_Right()

        if self.L == None:
            return self.R
        self.L, max_node = self.L.__pop_max_node()
        if self.L != None:
            max_node.L = self.L
        max_node.R = self.R
        max_node.height = max_node.__calc_height()
        return max_node if max_node.__calc_balance() <= +1 else max_node.__rotate_Left()

    def __calc_height(self):
        L_height = 0 if self.L == None else self.L.height
        R_height = 0 if self.R == None else self.R.height
        return 1 + max(L_height, R_height)
    
    def __calc_balance(self):
        L_height = 0 if self.L == None else self.L.height
        R_height = 0 if self.R == None else self.R.height
        return R_height - L_height

    def __rotate_L(self):
        nodeR = self.R
        self.R = nodeR.L
        nodeR.L = self
        return nodeR

    def __rotate_R(self):
        nodeL = self.L
        self.L = nodeL.R
        nodeL.R = self
        return nodeL

    def __rotate_Left(self):
        if self.R.__calc_balance() <= -1:
            self.R = self.R.__rotate_R()
            retVal = self.__rotate_L()
            retVal.L.height = retVal.L.__calc_height()
            retVal.R.height = retVal.R.__calc_height()
            retVal  .height = retVal  .__calc_height()
        else:
            retVal = self.__rotate_L()
            retVal.L.height = retVal.L.__calc_height()
            retVal  .height = retVal  .__calc_height()
        return retVal

    def __rotate_Right(self):
        if +1 <= self.L.__calc_balance():
            self.L = self.L.__rotate_L()
            retVal = self.__rotate_R()
            retVal.L.height = retVal.L.__calc_height()
            retVal.R.height = retVal.R.__calc_height()
            retVal  .height = retVal  .__calc_height()
        else:
            retVal = self.__rotate_R()
            retVal.R.height = retVal.R.__calc_height()
            retVal  .height = retVal  .__calc_height()
        return retVal

    def __pop_max_node(self):
        if self.R == None:
            return None, self
        if self.R.R == None:
            max_node = self.R
            self.R = self.R.L
            self.height = self.__calc_height()
            if self.__calc_balance() == -2:
                return self.__rotate_Right(), max_node
            return self, max_node

        self.R, max_node = self.R.__pop_max_node()
        self.height = self.__calc_height()
        if self.__calc_balance() == -2:
            return self.__rotate_Right(), max_node
        return self, max_node

    def list(self):
        tmp = []
        if self.L != None:
            tmp += self.L.list()
        tmp.append(self.key)
        if self.R != None:
            tmp += self.R.list()
        return tmp
