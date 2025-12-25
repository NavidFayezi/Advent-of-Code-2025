# I am assuming the row_length is the same for all rows,
# and also the column_length is the same for all columns.
def adjacent(i: int, j: int, row_length: int, column_length: int) -> list:
    adjacency_list = []
    for _i in range(i - 1, i + 2):
        for _j in range(j - 1, j + 2):
            if _j == j and _i == i:
                continue
            else:
                if 0 <= _i <= (row_length - 1) and (
                    0 <= _j <= column_length - 1
                ):
                    adjacency_list.append([_i, _j])
    return adjacency_list


with open("Day4.txt", "r") as fo:
    diagram_array = fo.readlines()  # assuming the file fits in the memory
    row_length = (
        len(diagram_array[0]) - 1
    )  # No need to remove \n, just ignoring it.
    column_length = len(diagram_array)
    accessible_rolls = 0
    flag = True
    while flag:
        flag = False
        for i in range(row_length):
            for j in range(column_length):
                adjacency_list = adjacent(i, j, row_length, column_length)
                rolls = 0
                if diagram_array[i][j] == "@":
                    for index_tuple in adjacency_list:
                        if diagram_array[index_tuple[0]][index_tuple[1]] == "@":
                            rolls += 1
                    if rolls < 4:
                        flag = True
                        accessible_rolls += 1
                        diagram_array[i] = (
                            diagram_array[i][:j]
                            + "."
                            + diagram_array[i][j + 1 :]
                        )
    print(accessible_rolls)
