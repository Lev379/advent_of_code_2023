with open('./day03/day03.txt', 'r') as file:
    lines = file.readlines()

lines = [list(line.strip("\n")) for line in lines]

def is_symbol(char):
    return not char == "." and not char.isdigit()

def is_valid_index(x, y, max):
    return 0 <= x < max and 0 <= y < max

def check_part_number(matrix, x, y, max):
    directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_index(nx, ny, max) and is_symbol(matrix[nx][ny]):
            return True
    return False

def calculate_part_numbers_sum(matrix):
    
    total_sum = 0
    for i, x in enumerate(matrix):
        part_number = ""
        is_part_number = False
        for j, y in enumerate(x):
            if y.isdigit():
                part_number += y
                if not is_part_number:
                    is_part_number = check_part_number(matrix, i, j, len(matrix))
            else:
                if is_part_number:
                    total_sum += int(part_number)
                part_number = ""
                is_part_number = False
        if is_part_number:
            total_sum += int(part_number)
                
    
    print(total_sum)

calculate_part_numbers_sum(lines)