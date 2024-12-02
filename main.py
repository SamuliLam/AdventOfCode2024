left = []
right = []

with open("../adventofcode2024/input.txt") as file:
    for line in file:
        new_list = line.split()
        left.append(new_list[0])
        right.append(new_list[1])

left.sort()
right.sort()

left_integers = []
right_integers = []

for i in left:
    left_integers.append(int(i))

for i in right:
    right_integers.append(int(i))

distance = 0

for i in range(left_integers.__len__()):

    distance += abs(left_integers[i] - right_integers[i])

print(distance)
