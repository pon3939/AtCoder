# -*- coding: utf-8 -*-


"""
Abbreviate Fox
"""


def main():
    """
    メイン処理
    """
    n = int(input())
    s = input()

    # TLE
    # currentString = s
    # while True:
    #     prevString = currentString
    #     currentString = currentString.replace("fox", "")
    #     if prevString == currentString:
    #         break
    # print(len(currentString))

    result = n
    temporary = ""
    for char in list(s):
        if char == "f" \
            or (char == "o" and temporary.endswith("f")) \
                or (char == "x" and temporary.endswith("fo")):
            # "fox"が完成する可能性のある文字列をtemporaryに保持する
            temporary += char
        else:
            temporary = ""

        if temporary.endswith("fox"):
            # "fox"が完成したので文字数を3文字分減らし、temporary末尾の"fox"を削除する
            result -= 3
            temporary = temporary[:-3]
    print(result)


if __name__ == '__main__':
    main()
