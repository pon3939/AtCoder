# -*- coding: utf-8 -*-


from typing import List

"""Orthogonality
"""


def main() -> None:
    """メイン処理
    """
    # 入力
    n: int = int(input())
    a: List[int] = map(int, input().split())
    b: List[int] = map(int, input().split())
    innerProduct: int = 0
    for (ai, bi) in zip(a, b):
        innerProduct += ai * bi

    if (innerProduct == 0):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
