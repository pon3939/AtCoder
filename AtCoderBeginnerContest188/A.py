# -*- coding: utf-8 -*-


"""Three-Point Shot
"""


def main() -> None:
    """メイン処理
    """
    # 入力
    x: int
    y: int
    x, y = map(int, input().split())
    if (min(x, y) + 3 > max(x, y)):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
