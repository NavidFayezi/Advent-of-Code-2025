DIGITS = 12
with open("Day3.txt", "r") as fo:
    joltage_sum = 0
    for line in fo:
        line = line.strip()
        line_length = len(line)
        beginning_index = 0
        line_joltage = ""
        for j in range(DIGITS - 1, -1, -1):
            max_char_index = beginning_index
            for i in range(beginning_index, line_length - j):
                if int(line[max_char_index]) < int(line[i]):
                    max_char_index = i
            line_joltage += line[max_char_index]
            beginning_index = max_char_index + 1
        joltage_sum += int(line_joltage)
    print(joltage_sum)
