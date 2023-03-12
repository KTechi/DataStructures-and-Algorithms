import itertools as it
import random as rd

def debug_tree(self):
    L_height = 0 if self.L == None else self.L.debug_tree()
    R_height = 0 if self.R == None else self.R.debug_tree()
    if 2 <= abs(L_height - R_height):
        raise Exception(f'[Height Error] key: {self.key}, L: {L_height}, R: {R_height}')
    if R_height - L_height != self.balance:
        raise Exception(f'[Balance Error] key: {self.key}, Bal: {self.balance}, L {L_height}, R {R_height}')
    return max(L_height, R_height) + 1

L = 9 # 全通り　生成
AVLTreeNode.debug_tree = debug_tree
for tuple_ in it.permutations(range(L)):
    try:
        avl = AVLTree()
        for num in tuple_:
            avl.insert(num)
            avl.root.debug_tree()
        if len(avl.list()) != len(tuple_):
            raise Exception('Tree generation error 1')
        for k, v in enumerate(avl.list()):
            if k != v:
                raise Exception('Tree generation error 2')
    except Exception as e:
        print('\033[31m' + str(e) + '\033[0m')
        print('tuple', tuple_)
        print(avl.list())
        avl.print_tree(print_balance=True)
        print('----------------')
        avl = AVLTree()
        for num in tuple_:
            avl.insert(num)
        avl.print_tree(print_balance=True)
        print('--------------------------------')
print('\033[32m' + 'EOF' + '\033[0m')

L = 8 # 全通り　生成　削除
AVLTreeNode.debug_tree = debug_tree
for tuple_ in it.permutations(range(L)):
    for delete_num in range(L):
        avl = AVLTree()
        for num in tuple_:
            avl.insert(num)
        try:
            if len(avl.list()) != len(tuple_):
                raise Exception('Tree generation error 1')
            for k, v in enumerate(avl.list()):
                if k != v:
                    raise Exception('Tree generation error 2')

            avl.root.debug_tree()
            avl.delete(delete_num)
            avl.root.debug_tree()

            if len(avl.list()) + 1 != len(tuple_):
                raise Exception('Delete error 1')
            tmp = 0
            for k, v in enumerate(avl.list()):
                if k == delete_num:
                    tmp += 1
                elif k + tmp != v:
                    raise Exception('Delete error 2')
        except Exception as e:
            print('\033[31m' + str(e) + '\033[0m')
            print('tuple', tuple_)
            print('delete', delete_num)
            print(avl.list())
            avl.print_tree(print_balance=True)
            print('----------------')
            avl = AVLTree()
            for num in tuple_:
                avl.insert(num)
            avl.print_tree(print_balance=True)
            print('--------------------------------')
print('\033[32m' + 'EOF' + '\033[0m')

L = 50 # 大きい木　生成　削除　 100000 回試行
AVLTreeNode.debug_tree = debug_tree
for _ in range(100000):
    tuple_ = [i for i in range(L)]
    for i in range(L):
        r = rd.randint(0, L-1)
        tuple_[i], tuple_[r] = tuple_[r], tuple_[i]
    avl = AVLTree()
    for num in tuple_:
        avl.insert(num)
    try:
        if len(avl.list()) != len(tuple_):
            raise Exception('Tree generation error 1')
        for k, v in enumerate(avl.list()):
            if k != v:
                raise Exception('Tree generation error 2')

        avl.root.debug_tree()
        delete_num = rd.randint(0, L-1)
        avl.delete(delete_num)
        avl.root.debug_tree()

        if len(avl.list()) + 1 != len(tuple_):
            raise Exception('Delete error 1')
        tmp = 0
        for k, v in enumerate(avl.list()):
            if k == delete_num:
                tmp += 1
            elif k + tmp != v:
                raise Exception('Delete error 2')
    except Exception as e:
        print('\033[31m' + str(e) + '\033[0m')
        print('tuple', tuple_)
        print('delete', delete_num)
        print(avl.list())
        avl.print_tree(print_balance=True)
        print('----------------')
        avl = AVLTree()
        for num in tuple_:
            avl.insert(num)
        avl.print_tree(print_balance=True)
        print('--------------------------------')
print('\033[32m' + 'EOF' + '\033[0m')
