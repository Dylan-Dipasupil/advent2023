f = open("inputs/dec1.txt", "r").read()

# part 1
"""
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?
"""
def part1(text: str) -> None:
    floor = 0
    for ch in text:
        if ch == "(":
            floor += 1
        else:
            floor -= 1
    return floor

"""
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

"""

def part2(text: str) -> None:
    floor = 0
    for i in range(len(text)):
        if text[i] == "(":
            floor += 1
        else:
            floor -= 1
            
        if floor == -1:
            return i + 1


endFloor = part1(f)
basementPosition = part2(f)
print(f"Part 1 End Floor: {endFloor}")
print(f"Part 2 Basement Position: {basementPosition}")          
          
