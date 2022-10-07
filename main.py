from dataclasses import dataclass
from enum import Enum
import json
from typing import Optional, Union


@dataclass
class Coodinate:
    x: int
    y: int

class Gender(Enum):
    Male = 1
    Female = 2
    Other = None

def try_to_deserialize_objects() -> None:
    try:
        print(json.dumps(Coodinate(10, 20)))
    except Exception as e:
        print("オブジェクトをそのままjson.dumpsに渡してもデシリアライズ不可 > ", e)
    print(f"__dict__を利用してオブジェクトを辞書形式に変換するとデシリアライズできる > {json.dumps(Coodinate(10, 20).__dict__)}")

def try_to_deserialize_lists() -> None:
    target_list: Optional[list[int]] = None
    target_json = json.dumps({"target_list": target_list})
    print(f"listデシリアライズ（Noneを渡した場合） >  {target_json}")
    target_list = [1, 2, 3, 4, 5]
    target_json = json.dumps({"target_list": target_list})
    print(f"listデシリアライズ >  {target_json}")

def try_to_deserialize_enum() -> None:
    try:
        target_json = json.dumps({"MyGender": Gender.Male})
        print(f"{target_json}")
    except Exception as e:
        print(f"enumそのままではデシリアライズ不可", e)

    target_json = json.dumps({"MyGender": Gender.Male.value})
    print(f"valueを取ることでデシリアライズできる > {target_json}")

    gender_list = [Gender.Male, Gender.Female, Gender.Other]
    gender_value_list = [g.value for g in gender_list]
    target_list_json = json.dumps({"Genders": gender_value_list})
    print(f"enumのリスト > {target_list_json}")

    try_to_deserialize_from_union_args(Gender.Male)
    try_to_deserialize_from_union_args(Gender.Other)
    try_to_deserialize_from_union_args([Gender.Male])
    try_to_deserialize_from_union_args([Gender.Other])

def try_to_deserialize_from_union_args(gender: Union[Gender, list[Gender]]) -> None:
    if isinstance(gender, Gender):
        target_json = json.dumps({"gender": gender.value})
        print(f"Union型からデシリアライズ > {target_json}")
    elif isinstance(gender, list):
        gender_value_list = [g.value for g in gender]
        target_json = json.dumps({"gender": gender_value_list})
        print(f"Union型からデシリアライズ > {target_json}")


def main() -> None:
    try_to_deserialize_objects()
    try_to_deserialize_lists()
    try_to_deserialize_enum()

if __name__ == "__main__":
    main()