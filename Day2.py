import re

pattern = re.compile(r"^([0-9]+)\1+$")
with open("Day2.txt", "r") as fo:
    line = fo.readline().strip()
    ranges = line.split(",")
    sum_invalid = 0
    sum_invalid_2 = 0
    for id_range in ranges:
        bounds = id_range.split("-")
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])
        
        
        for id in range(lower_bound, upper_bound + 1):
            id_str = str(id)
            _length = len(id_str)
            if _length % 2 == 0:
                if id_str[:_length // 2] == id_str[_length // 2:]:
                    sum_invalid += id
            matched = pattern.match(id_str)
            if matched is not None:
                sum_invalid_2 += id
    print(sum_invalid, sum_invalid_2)