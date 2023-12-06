import re

str_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_first_digit_of_line(line, reverse=False):
    # try to match the line with digit dictionary from start,
    # or until we find the first digit number, and return it
    text = line[::-1] if reverse else line
    digit_match = re.search(r'\d', text)
    digit_value = digit_match.group(0) if digit_match else None
    digit_index = text.find(digit_value) if digit_value else len(text)
    for (key, value) in str_to_digit.items():
        rl_key = key[::-1] if reverse else key
        text_digit_index = text.find(rl_key)
        if text_digit_index != -1 and text_digit_index < digit_index:
            digit_index = text_digit_index
            digit_value = value

    return int(digit_value)


f = open("data.txt", "r")
i = 0
sum_first_digits = 0
sum_last_digits = 0
for line in f:
    i += 1
    first_digit = get_first_digit_of_line(line)
    sum_first_digits += first_digit
    last_digit = get_first_digit_of_line(line, reverse=True)
    sum_last_digits += last_digit
    print(f"Line {i}: {first_digit} - {last_digit}")

print(f"Sum of first digits: {sum_first_digits}")
print(f"Sum of last digits: {sum_last_digits}")
