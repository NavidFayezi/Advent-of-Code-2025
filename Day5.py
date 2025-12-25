from operator import itemgetter


def unique_fresh_ids(list_ranges: list) -> int:
    list_ranges.sort(key=itemgetter(0, 1))
    unique_ids = 0
    list_length = len(list_ranges)
    max_counted = 0
    for i in range(list_length):
        lower_bound = list_ranges[i][0]
        if max_counted >= list_ranges[i][1]:
            continue

        elif max_counted >= list_ranges[i][0]:
            lower_bound = max_counted + 1

        unique_ids += list_ranges[i][1] - lower_bound + 1
        max_counted = list_ranges[i][1]

    return unique_ids


with open("Day5.txt", "r") as fo:
    reading_ranges = True
    list_ranges = []
    no_fresh_ids = 0
    for line in fo:
        if line == "\n":
            reading_ranges = False
            print(
                "Total number of unique fresh ids is: ",
                unique_fresh_ids(list_ranges),
            )
            continue
        else:
            if reading_ranges == True:
                # reading bounds for ranges
                line = line.strip()
                ranges = line.split("-")
                ranges[0] = int(ranges[0])
                ranges[1] = int(ranges[1])
                list_ranges.append(ranges)
            else:
                # reading ids
                id = int(line.strip())
                fresh = False
                for _range in list_ranges:
                    if _range[0] <= id <= _range[1]:
                        fresh = True
                        no_fresh_ids += 1
                        break

    print("Current fresh ids: ", no_fresh_ids)
