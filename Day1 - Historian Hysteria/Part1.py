list1 = []
list2 = []

with open("Day1 - Historian Hysteria/Input", "r") as file:
    for line in file:
        id1, id2 = line.split()
        list1.append(int(id1))
        list2.append(int(id2))

list1.sort()
list2.sort()

distances = []
for i in range(0, len(list1)):
    id1 = list1[i]
    id2 = list2[i]
    distances.append(abs(id1-id2))

print(sum(distances))
