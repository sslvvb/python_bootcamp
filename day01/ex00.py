def check(purse: dict[str, int]):
    for key, value in purse.items():
        if not isinstance(key, str) or not isinstance(value, int):
            raise Exception("Wrong type")


def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    check(purse)
    return {"gold_ingots": purse.get("gold_ingots", 0) + 1}


def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    check(purse)
    count: int = 0 if purse.get("gold_ingots", 0) == 0 else purse.get("gold_ingots") - 1
    return {"gold_ingots": count}


def empty(purse: dict[str, int]) -> dict[str, int]:
    check(purse)
    return {}


def split_booty(*dicts: dict[str, int]):
    pass


def main():
    dictionary: dict[str, int] = {"gold_ingots": 4}
    # dictionary: dict[str, int] = {}
    print(dictionary)
    print(dictionary.get("gold_ingots"))

    new_dict = add_ingot(dictionary)
    # new_dict = get_ingot(dictionary)
    # new_dict: dict[str, int] = empty(dictionary)
    print(new_dict)
    print(new_dict.get("gold_ingots"))


if __name__ == "__main__":
    main()
