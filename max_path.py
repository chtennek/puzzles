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
    if tree[1] is not None:
        display(tree[1], depth=depth+1)
    print '\t'*depth + 'O'
    if tree[2] is not None:
        display(tree[2], depth=depth+1)

def main():
    display(generate())

if __name__ == '__main__':
    main()
