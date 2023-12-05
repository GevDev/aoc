test_input = """two1nine"""

my_input = """
"""

import re

total_sum = 0

for entry in my_input.split("\n"):
    numbers = re.sub(r'[A-Za-z]', "", entry)
    total_sum += int(numbers[0]+numbers[len(numbers)-1])

print(f"Part 1 sum: {total_sum}")



### PART 2 ###

test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteene"""

valid_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
valid_words = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4", 
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}



total_sum = 0

for entry in my_input.split("\n"):

    entry = entry.replace("zerone", "zeroone")
    entry = entry.replace("twone", "twoone")
    entry = entry.replace("eightwo", "eighttwo")
    entry = entry.replace("eighthree", "eightthree")
    entry = entry.replace("oneight", "oneeight")
    entry = entry.replace("threeight", "threeeight")
    entry = entry.replace("fiveight", "fiveeight")
    entry = entry.replace("nineight", "nineeight")
    entry = entry.replace("sevenine", "sevennine")

    for word in valid_words:
        if word in entry:
            entry = entry.replace(word, valid_words[word]+"e")
    numbers = re.sub(r'[A-Za-z]', "", entry)
    print(numbers)
    print(int(numbers[0]+numbers[len(numbers)-1]))
    print("++++++++++++")
    total_sum += int(numbers[0]+numbers[len(numbers)-1])
    
print(f"Part 2 sum: {total_sum}")