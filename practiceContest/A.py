# -*- coding: utf-8 -*-

"""
Welcome to AtCoder
"""


def main():
    """
    メイン処理
    """
    # 1行目
    a = int(input())
    # 2行目
    b, c = map(int, input().split())
    # 3行目
    s = input()
    print(f"{a + b + c} {s}")


if __name__ == '__main__':
    main()
