test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

my_input = """
"""

total_sum = 0
game_counter = 1

for entry in test_input.split("\n"):
    entry = entry.split(": ")[1].replace(" ", "").split(";")
    max_red = 12
    max_green = 13
    max_blue = 14
    possible = True
    print(entry)
    for game in entry:
        game = game.split(",")
        for balls in game:
            if "red" in balls and int(balls.split("red")[0]) > max_red:
                possible = False
            elif "green" in balls and int(balls.split("green")[0]) > max_green:
                possible = False
            elif "blue" in balls and int(balls.split("blue")[0]) > max_blue:
                possible = False        
    if possible:
        total_sum += game_counter
    game_counter += 1

print(total_sum)


# ++++ PART 2 ++++

total_sum = 0

for entry in my_input.split("\n"):
    entry = entry.split(": ")[1].replace(" ", "").split(";")
    max_red = 0
    max_green = 0
    max_blue = 0
    print(entry)
    for game in entry:
        game = game.split(",")
        for balls in game:
            if "red" in balls and int(balls.split("red")[0]) > max_red:
                max_red = int(balls.split("red")[0])
            elif "green" in balls and int(balls.split("green")[0]) > max_green:
                max_green = int(balls.split("green")[0])
            elif "blue" in balls and int(balls.split("blue")[0]) > max_blue:
                max_blue = int(balls.split("blue")[0])

    total_sum += max_red * max_green * max_blue
    print(max_red, max_green, max_blue)
    game_counter += 1

print(total_sum)