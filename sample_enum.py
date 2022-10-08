from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BlUE = 3


def main() -> None:
    print(f"列挙型メンバー > {Color.RED}")
    print(f"列挙型メンバー > {repr(Color.RED)}")
    print(f"列挙型メンバーのデータ型(typeで判定) > {type(Color.RED)}")
    print(f"列挙型メンバーのデータ型(isinstanceで判定) > {isinstance(Color.RED, Color)}")
    print(f"列挙型メンバーのnameプロパティ > {Color.RED.name}")
    print(f"列挙型メンバーのvalueプロパティ > {Color.RED.value}")
    for c in Color:
        print(f"定義順でのイテレーション > {c}")


if __name__ == "__main__":
    main()