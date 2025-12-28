with open("Day7.txt", "r") as fo:
    first_line = fo.readline().strip()
    line_length = len(first_line)
    beams_list = [0 for i in range(line_length)]
    first_beam_index = first_line.index(
        "S"
    )  # assuming the first beam is always on the first line.
    beams_list[first_beam_index] = 1
    fo.seek(0)

    counter = 0
    for line in fo:
        line = line.strip()
        line_length = len(line)

        for i in range(line_length):
            if line[i] == "^" and beams_list[i] >= 1:
                counter += 1
                if i > 0:
                    beams_list[i - 1] += beams_list[i]
                if i < (line_length - 1):
                    beams_list[i + 1] += beams_list[i]
                beams_list[i] = 0
                
    print(counter)  # part one
    print(sum(beams_list))  # part two
