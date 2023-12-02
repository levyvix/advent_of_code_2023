import re
import string

# remove letters from text


def remove_letters(s):
    digits = re.compile(r"\d").findall(s)
    digits = digits[0], digits[-1]
    return int(''.join(digits))


if __name__ == "__main__":
    with open("data\\001.txt", "r") as f:
        data = f.readlines()
        data = list(map(lambda x: x.strip(), data))

    print(data[:10])
    numbers = list(map(remove_letters, data))

    print(numbers[:10])

    print(sum(numbers))
