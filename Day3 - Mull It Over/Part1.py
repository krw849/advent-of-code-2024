import re

VALID_INSTRUCTION_REGEX = "mul\\(([0-9]{1,3}),([0-9]{1,3})\\)"

sum = 0

with open("Day3 - Mull It Over/Input", "r") as file:
    content = file.read().replace("\n", "")

    valid_instructions = re.findall(VALID_INSTRUCTION_REGEX, content)

    for instruction in valid_instructions:
        num1 = int(instruction[0])
        num2 = int(instruction[1])
        sum += num1 * num2

print(sum)
