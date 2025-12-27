import math
with open("Day6.txt", "r") as fo:
    number_of_operands = len(fo.readline().split())
    list_of_all = [[] for i in range(number_of_operands)]
    fo.seek(0)
    second_part_list = []
    for line in fo:
        second_part_list.append(line)
        _list = line.split()
        for i in range(number_of_operands):
            if _list[i] != "*" and _list[i] != "+":
                list_of_all[i].append(int(_list[i]))
            else:
                list_of_all[i].append(_list[i])

    # part one of the question
    total = 0
    for _list in list_of_all:
        if _list[-1] == "*":
            total += math.prod(_list[:-1])
        elif _list[-1] == "+":
            total += sum(_list[:-1])
        else:
            print("Unsupported")        
    print(total)

    # the second part of the question
    rows = len(second_part_list) -1 # ignoring the operator row
    columns = len(second_part_list[0]) - 1 # assuming all columns have the
                                           # same length and ignore trailing \n
    
    # create the list of weird numbers
    list_of_numbers = ["" for i in range(columns)]
    for i in range(rows):
        for j in range(columns):
            if second_part_list[i][j] != " ":
                list_of_numbers[j] += second_part_list[i][j]

    operators = second_part_list[-1].split()
    temp = []
    operator_counter = 0
    total = 0
    list_of_numbers.append("")  # fixes the last iteration in the next loop
    for char_string in list_of_numbers:
        if char_string == "":
            if operators[operator_counter] == "+":
                total += sum(temp)
            elif operators[operator_counter] == "*":
                total += math.prod(temp)
            else:
                print("Unsupported.")
            
            temp = []
            operator_counter += 1

        else:
            temp.append(int(char_string))
    

    print(total)


