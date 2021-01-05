# -*- coding: utf-8 -*-

"""
Welcome to AtCoder
"""


def main():
    """
    メイン処理
    """
    inputString = [input().split() for i in range(3)]
    a = int(inputString[0][0])
    b = int(inputString[1][0])
    c = int(inputString[1][1])
    s = inputString[2][0]
    print(f"{a + b + c} {s}")


if __name__ == '__main__':
    main()
