list1 = []
list2 = []

with open("Day1 - Historian Hysteria/Input", "r") as file:
    for line in file:
        id1, id2 = line.split()
        list1.append(int(id1))
        list2.append(int(id2))

list2_counts = {}
for num in list2:
    list2_counts[num] = list2_counts.get(num, 0) + 1

similarityScore = 0
for num in list1:
    similarityScore += num * list2_counts.get(num, 0)

print(similarityScore)
