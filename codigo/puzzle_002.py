import re


def get_digits(s: str) -> int:
    """Remove letter from a string, and return the first and last digits

    Args:
        s (str): string to be parsed

    Returns:
        int: first and last digits

    Examples:
    >>> get_digits("two2three3four4five5six6seven7eight8nine9")
    29
    """

    mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    p = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", s)
    result = []
    for digit in p:
        try:
            result.append(int(digit))
        except Exception:
            result.append(mapping[digit])

    return int("".join([str(result[0]), str(result[-1])]))


if __name__ == "__main__":
    with open("data\\002.txt", "r") as f:
        data = f.readlines()
        data = list(map(lambda x: x.strip(), data))

    numbers = list(map(get_digits, data))

    print(sum(numbers))
