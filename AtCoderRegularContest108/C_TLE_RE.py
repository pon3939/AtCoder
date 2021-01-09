# -*- coding: utf-8 -*-

from typing import List

"""
Keep Graph Connected
"""


class Node:
    """
    頂点クラス
    """
    # 親
    Parent: 'Node'

    # 子
    Children: List['Node']

    # ラベル
    Label: int

    # 親につながる辺のラベル
    ParentEdgeLabel: int

    def __init__(self):
        self.Parent = None
        self.Children = []
        self.Label = 0
        self.ParentEdgeLabel = 0


def main() -> None:
    """メイン処理
    """
    # 入力
    global N
    m: int
    N, m = map(int, input().split())
    nodes: List[Node] = InitNodes(N)
    for _ in range(m):
        u: int
        v: int
        c: int
        u, v, c = map(int, input().split())
        # めんどくさいからインデックスは0スタートにする
        UniteTree(nodes[u - 1], nodes[v - 1], c - 1)

    StickLabel(FindRoot(nodes[0]))
    for node in nodes:
        # 0スタートにしてるから+1
        print(node.Label + 1)


def StickLabel(root: Node) -> None:
    """rootを根とする部分木にラベルを貼る

    Args:
        node (node): 根
    """
    if root == FindRoot(root):
        # 根のラベルは何でもいい
        root.Label = 0
    elif root.Parent.Label == root.ParentEdgeLabel:
        # 親のラベルと辺のラベルが等しい場合
        root.Label = 1 if root.ParentEdgeLabel == 0 else 0
    else:
        # 親のラベルと辺のラベルが異なる場合
        root.Label = root.ParentEdgeLabel

    for child in root.Children:
        StickLabel(child)


def InitNodes(nodeCount: int) -> List[Node]:
    """頂点がnodeCount個の木を初期化する

    Args:
        nodeCount (int): 頂点の数
    """
    return list(map(lambda x: Node(), range(nodeCount)))


def FindRoot(node: Node) -> Node:
    """根を取得

    Args:
        node (Node): 根を探す頂点

    Returns:
        Node: 根
    """
    if (node.Parent is None):
        return node

    return FindRoot(node.Parent)


def IsSameTree(nodeA: Node, nodeB: Node) -> bool:
    """頂点Aと頂点Bが同じ木であればTrueを返す

    Args:
        nodeA (Node): 頂点A
        nodeB (Node): 頂点B

    Returns:
        bool: 同じ木であるか
    """
    return FindRoot(nodeA) == FindRoot(nodeB)


def UniteTree(parent: Node, child: Node, label: int) -> None:
    """2つの頂点を結合する

    Args:
        parent (Node): 親になる頂点
        child (Node): 子になる頂点
        label (int): 辺のラベル
    """

    if (IsSameTree(parent, child)):
        # 同じ木なので何もしない
        return

    ChangeParent(parent, child, label)


def ChangeParent(parent: Node, child: Node, label: int) -> None:
    """2つの頂点の親子関係を変更する

    Args:
        parent (Node): 親になる頂点
        child (Node): 子になる頂点
        label (int): 辺のラベル
    """
    if (child.Parent is not None):
        # 親が存在する場合は親を再帰的に付け替える
        child.Parent.Children.remove(child)
        ChangeParent(child, child.Parent, child.ParentEdgeLabel)

    parent.Children.append(child)
    child.Parent = parent
    child.ParentEdgeLabel = label


if __name__ == '__main__':
    main()
