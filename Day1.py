START = 50 

counter = 0
counter_2 = 0
current_position = START
with open("Day1.txt", "r", encoding="utf-8") as fo:
    for line in fo:
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])
        distance_to_zero = 100

        if direction == "L":
            if current_position != 0:
                distance_to_zero = current_position
            current_position = (current_position - distance) % 100
        elif direction == "R":
            if current_position != 0:
                distance_to_zero = 100 - current_position
            current_position = (current_position + distance) % 100
        else:
            print("ERROR")
            break
        
        if distance >= distance_to_zero:
            counter_2 += (distance - distance_to_zero) // 100 + 1

        if current_position == 0:
            counter += 1


print(counter , counter_2)
