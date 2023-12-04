with open('./inputs/day01.txt', 'r') as file:
    lines = file.readlines()

words = [line.strip() for line in lines]


digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
for word in words:
    digits = []
    for i, char in enumerate(word):
        if char.isdigit():
            digits.append(char)
        for j, value in enumerate(digit_words):
            if word[i:].startswith(value):
                digits.append(str(j + 1))
    print(digits)
    total += int(digits[0] + digits[-1])
print(total)