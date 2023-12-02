from collections import defaultdict 
f = open("inputs/dec1.txt", "r").readlines()

# part 1
"""
You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

"""
def parse_line(line: str) -> int:
    first_digit = ""
    last_digit = ""
    seen_first = False
    for ch in line:
        if ch.isdigit():
            if not seen_first:
                first_digit = ch
                seen_first = True
                last_digit = ch
            else:
                last_digit = ch
    
    if not first_digit:
        return 0
    return int(first_digit + last_digit)

def part1(file: list) -> None:
    sum = 0
    for line in file:
        sum += parse_line(line)
    return sum




"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

"""
def parse_line2(line: str) -> str:
    if not line:
        return ""
    
    for idx, ch in enumerate(line):
        if ch.isdigit():
            return ch + parse_line2(line[idx + 1:])
        if ch == "o" and line.find("one") == idx:
            return "1" + parse_line2(line[idx + 2:])
        if ch == "t":
            if line.find("two") == idx:
                return "2" + parse_line2(line[idx + 2:])
            if line.find("three") == idx:
                return "3" + parse_line2(line[idx + 4:])
        if ch == "f":
            if line.find("four") == idx:
                return "4" + parse_line2(line[idx + 3:])
            if line.find("five") == idx:
                return "5" + parse_line2(line[idx + 3:])
        if ch == "s":
            if line.find("six") == idx:
                return "6" + parse_line2(line[idx + 2:])
            if line.find("seven") == idx:
                return "7" + parse_line2(line[idx + 4:])
        if ch == "e" and line.find("eight") == idx:
            return "8" + parse_line2(line[idx + 4:])
        if ch == "n" and line.find("nine") == idx:
            return "9" + parse_line2(line[idx + 3:])
        
    return ""

            


def part2(file: str) -> None:
    sum = 0
    for line in file:
        new_line = parse_line2(line)
        sum += parse_line(new_line)
    return sum
        

part1res = part1(f)
part2res = part2(f)
print(f"Part 1 Result: {part1res}")
print(f"Part 2 result: {part2res}")          
