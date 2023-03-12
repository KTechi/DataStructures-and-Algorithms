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

    def print_tree(self, print_balance=False):
        if self.root == None:
            print('None')
        else:
            self.__print_balance = print_balance
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
        if self.__print_balance:
            self.__lines[depth] += '[' + str(node.balance) + ']'

        self.__add_to_lines(node.R, depth+1)

class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.L = None
        self.R = None
        self.balance = 0

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
                self.balance -= 1
                return self

            pre_balance = self.L.balance
            self.L = self.L.insert(key)
            if self.L.balance == 0:
                return self
            if pre_balance == 0:
                self.balance -= 1
            if -1 <= self.balance:
                return self
            return self.__rotate_Right()
        else:
            if self.R == None:
                self.R = AVLTreeNode(key)
                self.balance += 1
                return self

            pre_balance = self.R.balance
            self.R = self.R.insert(key)
            if self.R.balance == 0:
                return self
            if pre_balance == 0:
                self.balance += 1
            if self.balance <= +1:
                return self
            return self.__rotate_Left()

    def delete(self, key):
        if key < self.key:
            if self.L == None:
                return self

            pre_balance = self.L.balance
            self.L = self.L.delete(key)
            if self.L == None or abs(pre_balance) == 1 and self.L.balance == 0:
                self.balance += 1
            if abs(self.balance) <= 1:
                return self
            return self.__rotate_Left()
        elif self.key < key:
            if self.R == None:
                return self

            pre_balance = self.R.balance
            self.R = self.R.delete(key)
            if self.R == None or abs(pre_balance) == 1 and self.R.balance == 0:
                self.balance -= 1
            if abs(self.balance) <= 1:
                return self
            return self.__rotate_Right()

        if self.L == None:
            return self.R

        pre_balance = self.L.balance
        self.L, max_node = self.L.__pop_max_node()
        if self.L == None:
            max_node.R = self.R
            max_node.balance = self.balance + 1
            if max_node.balance == +2:
                max_node = max_node.__rotate_Left()
            return max_node

        max_node.L = self.L
        max_node.R = self.R
        max_node.balance = self.balance
        if abs(pre_balance) == 1 and self.L.balance == 0:
            max_node.balance += 1
        if max_node.balance == +2:
            max_node = max_node.__rotate_Left()
        return max_node

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
        if self.R.balance == -1:
            self.R = self.R.__rotate_R()
            retVal = self.__rotate_L()
            x = retVal.L.balance
            y = retVal.R.balance
            z = retVal  .balance
            retVal.L.balance -= 2 + max(0, y) + max(0, z)
            retVal  .balance = max(z, 1 + y + max(0, z)) - max(0, 2 + max(0, y) + max(0, z) - x)
            retVal.R.balance += 1 + max(0, -z)
        else:
            retVal = self.__rotate_L()
            x = retVal.L.balance
            y = retVal.balance
            retVal.L.balance -= 1 + max(0, y)
            retVal.balance   -= 1 + max(0, 1 - x + max(0, y))
        return retVal

    def __rotate_Right(self):
        if self.L.balance == +1:
            self.L = self.L.__rotate_L()
            retVal = self.__rotate_R()
            x = retVal.R.balance
            y = retVal.L.balance
            z = retVal  .balance
            retVal.L.balance -= 1 + max(0, z)
            retVal  .balance = max(-z, 1 - y + max(0, -z)) - max(0, 2 + max(0, -y) + max(0, -z) + x)
            retVal.R.balance += 2 + max(0, -y) + max(0, -z)
        else:
            retVal = self.__rotate_R()
            x = retVal.R.balance
            y = retVal.balance
            retVal.R.balance += 1 + max(0, -y)
            retVal.balance   += 1 + max(0, 1 + x + max(0, -y))
        return retVal

    def __pop_max_node(self):
        if self.R == None:
            return None, self
        if self.R.R == None:
            max_node = self.R
            self.R = self.R.L
            self.balance -= 1
            if self.balance == -2:
                return self.__rotate_Right(), max_node
            return self, max_node

        pre_balance = self.R.balance
        self.R, max_node = self.R.__pop_max_node()
        if abs(pre_balance) == 1 and self.R.balance == 0:
            self.balance -= 1
            if self.balance == -2:
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
