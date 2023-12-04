with open('./inputs/day01.txt', 'r') as file:
    lines = file.readlines()

words = [line.strip() for line in lines]

total = 0

def first_and_last_digit(word):
    first_digit = None
    last_digit = None
    for char in word:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    return first_digit, last_digit


def concatenate_digits(digit_tuple):
    return int(digit_tuple[0] + digit_tuple[1])


for word in words:
    digits = first_and_last_digit(word)
    line_value = concatenate_digits(digits)
    total += line_value


print(total)