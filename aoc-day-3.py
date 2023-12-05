import string

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
...$.*.*20"""

my_input = """
"""

from collections import defaultdict 

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
total_sum = 0
engine_map = []

part2_adjencency_map = defaultdict(lambda: [])

for entry in test_input.split("\n"):
# for entry in test_input.split("\n"):
    engine_map.append(list(entry))

def is_adjacent(col_start, row_start, col_end, row_end, my_map, number):
    found = False
    # Check top left of col_start, row_start-1
    if row_start > 0 and col_start > 0:
        if my_map[row_start-1][col_start-1] in string.punctuation and my_map[row_start-1][col_start-1] != ".":
            if (my_map[row_start-1][col_start-1] == "*"):
                part2_adjencency_map[(row_start-1,col_start-1)].append(number)
            print("Top left")
            found = True

    # Check directly above col_start, row_start-1 to col_end, row_start-1
    if row_start > 0:
        for col in range(col_start, col_end):
            if my_map[row_start-1][col] in string.punctuation and my_map[row_start-1][col] != ".":
                if (my_map[row_start-1][col] == "*"):
                    part2_adjencency_map[(row_start-1,col)].append(number)
                print("Top")
                found = True

    # Check top right of col_start, row_start
    if row_start > 0 and col_end < len(my_map[row_start-1])-1:
        if (my_map[row_start-1][col_end] in string.punctuation) and my_map[row_start-1][col_end] != ".":
            if (my_map[row_start-1][col_end] == "*"):
                part2_adjencency_map[(row_start-1,col_end)].append(number)
            print("Top right")
            found = True
    
    # Check bottom left of col_start, row_start+1
    if row_end < len(my_map)-1 and col_start > 0:
        if my_map[row_end+1][col_start-1] in string.punctuation and my_map[row_end+1][col_start-1] != ".":
            if (my_map[row_end+1][col_start-1] == "*"):
                part2_adjencency_map[(row_end+1,col_start-1)].append(number)
            print("Bottom left")
            found = True

    # Check directly below col_start, row_end+1 to col_end, row_end+1
    if row_end < len(my_map)-1:
        for col in range(col_start, col_end):
            if my_map[row_end+1][col] in string.punctuation and my_map[row_end+1][col] != ".":
                if (my_map[row_end+1][col] == "*"):
                    part2_adjencency_map[(row_end+1,col)].append(number)
                print("Bottom")
                found = True

    # Check bottom right of col_end, row_end+1
    if row_end < len(my_map)-1 and col_end < len(my_map[row_end+1])-1:
        if my_map[row_end+1][col_end] in string.punctuation and my_map[row_end+1][col_end] != ".":
            if (my_map[row_end+1][col_end] == "*"):
                part2_adjencency_map[(row_end+1,col_end)].append(number)
            print("Bottom right")
            found = True

    # Check directly left of col_start
    if col_start > 0:
        if my_map[row][col_start-1] in string.punctuation and my_map[row][col_start-1] != ".":
            if (my_map[row][col_start-1] == "*"):
                part2_adjencency_map[(row,col_start-1)].append(number)
            print("Left")
            found = True

    # Check directly right of col_end
    if col_end < len(my_map[row])-1:
        if my_map[row][col_end] in string.punctuation and my_map[row][col_end] != ".":
            if (my_map[row][col_end] == "*"):
                part2_adjencency_map[(row,col_end)].append(number)
            print("Right")
            found = True

    if not found:
        print("No adjacent found")
    return found

for row in range(len(engine_map)):
    col_start = -1
    col_end = -1
    row_start = -1
    row_end = -1
    number = ""
    for col in range(len(engine_map[row])):
        if engine_map[row][col] in numbers:
            if col_start == -1:
                col_start = col
                row_start = row
            number += engine_map[row][col]
        elif engine_map[row][col] not in numbers:
            if col_start != -1 or number != "":
                col_end = col
                row_end = row
                print(number)
                if is_adjacent(col_start, row_start, col_end, row_end, engine_map, number):
                    total_sum += int(number)
                col_start = -1
                col_end = -1
                row_start = -1
                row_end = -1
                number = ""
        if col == len(engine_map[row])-1 and number != "":
            col_end = col
            row_end = row
            print(number)
            if is_adjacent(col_start, row_start, col_end, row_end, engine_map, number):
                total_sum += int(number)
            col_start = -1
            col_end = -1
            row_start = -1
            row_end = -1
            number = ""

    print("+++++++")

print(total_sum)

# +++++ PART 2 +++++

total_sum = 0

for entry in part2_adjencency_map:
    if len(part2_adjencency_map[entry]) == 2:
        print(entry, part2_adjencency_map[entry])
        total_sum += int(part2_adjencency_map[entry][0])*int(part2_adjencency_map[entry][1])

print(total_sum)