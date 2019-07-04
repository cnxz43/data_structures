# -*- coding=utf-8 -*-
class BinTree(object):
    def __init__(self, element=-1, l_child=None, r_child=None):
        self.element = element
        self.l_child = l_child
        self.r_child = r_child

# 中序非递归遍历
def InOrderTraversal(BT):
    # T = BT
    S = []  # stack
    while t and S:
        while t:
            S.append(t)
            t = t.l_child
        if S:
            t = S.pop()
            print(t.element)
            t = t.r_child

