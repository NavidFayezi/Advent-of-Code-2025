import math  # math.dist()
from operator import itemgetter


with open("Day8.txt", "r") as fo:
    points_list = []
    for line in fo:
        line = line.strip()
        coordinates = tuple(map(int, line.split(",")))
        points_list.append(coordinates)

    no_points = len(points_list)
    distances_list = []
    for i in range(no_points):
        for j in range(i + 1, no_points):
            distances_list.append(
                (
                    points_list[i],
                    points_list[j],
                    math.dist(points_list[i], points_list[j]),
                )
            )

    distances_list.sort(key=itemgetter(2))

    sets = []  # no standard DSU implementations in python -_-
    total_connections = len(distances_list)
    part_two = 0
    for i in range(total_connections):
        p1 = distances_list[i][0]
        p2 = distances_list[i][1]
        part_two = p1[0] * p2[0]

        # find the sets to which p1 and p2 belong to
        p1_index = -1
        p2_index = -1
        no_sets = len(sets)
        for c in range(no_sets):
            if p1 in sets[c]:
                p1_index = c
            if p2 in sets[c]:
                p2_index = c

        if p1_index == -1:
            if p2_index != -1:
                sets[p2_index].add(p1)
            else:
                sets.append(set())
                sets[-1].update([p1, p2])

        elif p2_index == -1:
            sets[p1_index].add(p2)

        else:
            if p1_index == p2_index:
                continue
            else:
                sets[p1_index].update(sets[p2_index])
                del sets[p2_index]

        if len(sets) == 1 and (len(sets[0]) == len(points_list)):
            break

    # part one
    # sets.sort(key=len, reverse=True)
    # print(len(sets[0]) * len(sets[1]) * len(sets[2]))
    # for this to work "i" should go upto 1000

    print(part_two)
