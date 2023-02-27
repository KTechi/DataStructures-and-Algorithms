import itertools as it

L = 8

for tuple_ in it.permutations(range(L)):
    for delete_num in range(L):
        bst = BinarySearchTree()
        for num in tuple_:
            bst.insert(num)
        try:
            if len(bst.list()) != len(tuple_):
                raise Exception('Tree generation error 1')
            for k, v in enumerate(bst.list()):
                if k != v:
                    raise Exception('Tree generation error 2')

            bst.delete(delete_num)

            if len(bst.list()) + 1 != len(tuple_):
                raise Exception('Delete error 1')
            tmp = 0
            for k, v in enumerate(bst.list()):
                if k == delete_num:
                    tmp += 1
                elif k + tmp != v:
                    raise Exception('Delete error 2')
        except Exception as e:
            print('\033[31m' + str(e) + '\033[0m')
            print('tuple', tuple_)
            print('delete', delete_num)
            print(bst.list())
            bst.print_tree()
            print('----------------')
            bst = BinarySearchTree()
            for num in tuple_:
                bst.insert(num)
            bst.print_tree()
            print('--------------------------------')
print('\033[32m' + 'EOF' + '\033[0m')
