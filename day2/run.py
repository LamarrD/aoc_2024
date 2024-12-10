
def get_matrix_from_input():
    matrix = []
    
    with open("day2/input.txt") as f:
        data = f.read().splitlines()
        for row in data:
            # convert to ints
            int_row = [int(num) for num in row.split()]
            matrix.append(int_row)
        
    return matrix


def part_1():
    safe_count = 0
    
    matrix = get_matrix_from_input()
    for row in matrix:  
        safe = True

        # Check if numbers are increasing always or decreasing always
        if sorted(row) != row and sorted(row, reverse=True) != row:
            continue
 
        # Check if numbers are at least 1 apart and at most 3 apart
        for i in range(len(row)-1):
            num1 = row[i]
            num2 = row[i+1]
            
            difference = abs(num1 - num2)
            if difference < 1 or difference > 3:
                safe = False
                break

        if safe:
            safe_count += 1

            
    return safe_count


def part_2_helper(row):
    safe = True

    # Check if numbers are increasing always or decreasing always
    if sorted(row) != row and sorted(row, reverse=True) != row:
        return False

    # Check if numbers are at least 1 apart and at most 3 apart
    for i in range(len(row)-1):
        num1 = row[i]
        num2 = row[i+1]
        
        difference = abs(num1 - num2)
        if difference < 1 or difference > 3:
            return False    

    if safe:
        return True

def part_2():
    safe_count = 0
    potentials = []
    matrix = get_matrix_from_input()
    
    for row in matrix:
        # Determine mostly increasing or decreasing row
        increasings = []
        for i in range(len(row)-1):
            num1 = row[i]
            num2 = row[i+1]
            if num1 < num2:
                increasings.append(True)
        increasing = len(increasings) > len(row) // 2
        
        # Check if numbers are different by at least 1 and at most 3
        safe = True
        for i in range(len(row)-1):
            num1 = row[i]
            num2 = row[i+1]

            difference = abs(num1 - num2)
            if (difference < 1 or difference > 3) or (increasing and num1 > num2) or (not increasing and num1 < num2):
                potential_row1 = row[:i] + row[i+1:]
                potential_row2 = row[:i+1] + row[i+2:]
                potentials.append([potential_row1, potential_row2])
                safe = False
                break
        
        if safe:
            safe_count += 1
            continue
                
    for row1, row2 in potentials:
        if part_2_helper(row1) or part_2_helper(row2):
            safe_count += 1
    
    return safe_count


    

if __name__ == "__main__":
    p1_answer = part_1()
    print(f"Part 1: {p1_answer}")

    p2_answer = part_2()
    print(f"Part 2: {p2_answer}")
