import random

def generate(parent=None, p=.8, max_depth=5):
    if max_depth == 0 or random.random() > p:
        return None
    else:
        node = [parent, None, None]
        node[1] = generate(parent, p, max_depth - 1)
        node[2] = generate(parent, p, max_depth - 1)
        return node

def display(tree, depth=0):
    if tree is None:
        print 0
        return
    if tree[1] is not None:
        display(tree[1], depth=depth+1)
    print '\t'*depth + (str(tree[3]) if len(tree) == 4 else 'O')
    if tree[2] is not None:
        display(tree[2], depth=depth+1)
    return tree

def depth(tree):
    if tree is None:
        return
    elif tree[1] == tree[2] == None:
        tree += [0]
    else: 
        depth(tree[1])
        depth(tree[2])
        left_depth = tree[1][3] if tree[1] else 0
        right_depth = tree[2][3] if tree[2] else 0
        tree += [max(left_depth, right_depth) + 1]
    return tree

def max_depth(tree):
    return 0 if tree is None else tree[3] + 1

def max_path(tree):
    if tree is None:
        return 0
    return max(max_path(tree[1]), max_path(tree[2]), max_depth(tree[1]) + max_depth(tree[2]))

def main():
    tree = depth(generate())
    display(tree)
    print max_path(tree)


if __name__ == '__main__':
    main()
