# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

def is_safe(levels):
    increasing = all(
        1 <= b - a <= 3
        for a, b in zip(levels, levels[1:])
    )

    decreasing = all(
        1 <= a - b <= 3
        for a, b in zip(levels, levels[1:])
    )

    return increasing or decreasing


safe_count = 0
unsafe_count = 0
with open("Day2 - Red-Nosed Reports/input", "r") as file:
    for line in file:
        levels = list(map(int, line.split()))

        if is_safe(levels):
            print("Safe")
            safe_count += 1
        else:
            print("Unsafe")
            unsafe_count += 1

print(safe_count)
