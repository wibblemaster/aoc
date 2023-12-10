#!/usr/bin/env python

def extract_digits(s):
    leftmost_digit = None
    rightmost_digit = None
    for i in s:
        if i.isdigit():
            if leftmost_digit is None:
                leftmost_digit = i
            rightmost_digit = i
    if leftmost_digit is None or rightmost_digit is None:
        return None
    return leftmost_digit + rightmost_digit


def replace_text_with_digits(s):
    element = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    impl = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
             "six": "6", "seven": "7", "eight": "8", "nine": "9" }

    changes = False

    while True:
        min_locn = len(s) + 1
        replacement = ""
        for i in element:
            locn = s.find(i)
            if locn != -1 and locn < min_locn:
                replacement = i
                min_locn = locn
                changes = True
        if not changes:
            break
        else:#
            s = s.replace(replacement, impl[replacement], 1)
            changes = False
        max_locn = 0
        replacement = ""
        for i in element:
            locn = s.find(i, max_locn)
            if locn != -1 and locn > max_locn:
                replacement = i
                max_locn = locn
                changes = True
        if not changes:
            break
        else:
            items = s.split(replacement)
            
            s = s.replace(replacement, impl[replacement])

            break
    return s

# Example usage
s = "eighttwothree"
print(replace_text_with_digits(s))  # Output: 1 2 3 4 5 6 7 8 9

# Example usage
s = "a7a"
print(extract_digits(s))  # Output: 77

print(extract_digits("abd1234cde3456sdd"))  # Output: 77

with open('input.txt','r') as f:
    lines = [line.strip() for line in f.readlines()]

print(lines)
print("---")
t = [replace_text_with_digits(x) for x in lines]

for i in range(len(lines)):
    print(f"{lines[i]} - {t[i]}")

sum = 0
for line in lines:
    details = extract_digits(line)
    # print(f"{sum}: {line} - {replace_text_with_digits(line)} - {details}")
    sum += int(details)

old = sum

# Example usage
sum = 0
for line in lines:
    details = extract_digits(replace_text_with_digits(line))
    print(f"{sum}: {line} - {replace_text_with_digits(line)} - {details}")
    sum += int(details)

print(f"{old},{sum}")

print(extract_digits(replace_text_with_digits("twofivesevenfivesixonenine5seven")))
