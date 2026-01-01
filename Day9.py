with open("Day9.txt", "r") as fo:
    tiles_list = []
    for line in fo:
        red_tile = tuple(map(int, line.strip().split(",")))
        tiles_list.append(red_tile)

    no_tiles = len(tiles_list)
    max_area = 0
    for i in range(no_tiles):
        for j in range(i + 1, no_tiles):
            y_i = tiles_list[i][1]
            x_i = tiles_list[i][0]
            y_j = tiles_list[j][1]
            x_j = tiles_list[j][0]
            temp_area = (abs(y_i - y_j) + 1) * (abs(x_i - x_j) + 1)

            rule_out = False
            for k in range(no_tiles):
                p1 = tiles_list[k]
                p2 = tiles_list[(k + 1) % no_tiles]
                max_x = max(x_i, x_j)
                max_y = max(y_i, y_j)
                min_x = min(x_i, x_j)
                min_y = min(y_i, y_j)

                min_x2 = min(p1[0], p2[0])
                max_x2 = max(p1[0], p2[0])
                min_y2 = min(p1[1], p2[1])
                max_y2 = max(p1[1], p2[1])

                if (
                    min_x < max_x2
                    and max_x > min_x2
                    and min_y2 < max_y
                    and max_y2 > min_y
                ):
                    rule_out = True

            if temp_area > max_area and rule_out == False:
                max_area = temp_area
    print(max_area)
