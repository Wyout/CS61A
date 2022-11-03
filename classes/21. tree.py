# Trees
from operator import is_, le


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch) #检测分支是不是树
    return [label] + list(branches) #返回的是一个list，注意这里的list用的是（）

def label(tree):
    return tree[0] #list的第一个元素就是根

def branches(tree):
    return tree[1:]

def is_tree(tree):
    #判断是不是树，通过判断树的类型是不是list或者该list是否有内容
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):#再判断每个根是不是树
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]#注意这里是一个list！！！
    else:
        return sum([leaves(b) for b in branches(tree)], [])
        #为什么这里后面有一个【】，详见ob

def increment_leaves(t):#每个子节点的大小加一
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):#每个节点大小一
    return tree(label(t)+1, [increment(b) for b in branches(t)])

def print_tree(t, indent = 0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)


numbers = tree(3, [tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])

def print_sum(t, so_far):
    so_far = so_far + label(t)
    if(is_leaf(t)):
        print(so_far)
    else:
        for b in branches(t):
            print_sum(b, so_far)