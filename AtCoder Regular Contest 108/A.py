# -*- coding: utf-8 -*-


"""
Sum and Product
"""


import math


def main():
    """
    メイン処理
    """
    # nm = p より min(n, m) <= √p
    # x = min(n, m) とする
    # nm = p に x を代入して x(s-x) = p
    # x = min(n, m) <= √p なので 1 <= x <= √pの範囲で全探索
    s, p = map(int, input().split())
    for x in range(1, math.floor(math.sqrt(p)) + 1):
        if x * (s - x) == p:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
