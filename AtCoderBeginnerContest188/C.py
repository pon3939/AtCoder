# -*- coding: utf-8 -*-


from typing import List

"""ABC Tournament
"""


def main() -> None:
    """メイン処理
    """
    # 入力
    n: int = int(input())
    a: List[int] = list(map(int, input().split()))

    firstHalf: List[int] = a[:int(len(a) / 2)]
    secondHalf: List[int] = a[int(len(a) / 2):]
    answersRate: int = min(max(firstHalf), max(secondHalf))
    print(a.index(answersRate) + 1)


if __name__ == '__main__':
    main()
