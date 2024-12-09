import helper


def parse_input_into_lists():
    list1 = []
    list2 = []

    with open("day1/input.txt") as f:
        data = f.read().splitlines()
        for row in data:
            nums = row.split()
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))
    
    return list1, list2


# Get both lists, sort, calculate the distance between each number in the lists
# [1,2,3,4,5] [1,4,6,6,7] => [0,2,3,2,2] => 9
def part1():
    list1, list2 = parse_input_into_lists()
        
    # Sort the lists
    list1.sort()
    list2.sort()
        
    # Calculate the distance between each number in the lists
    distance = 0
    for i in range(len(list1)):
        num1 = list1[i]
        num2 = list2[i]
        distance += abs(num1 - num2)
    
    return distance


# Calculate similarity score by checkign how many times the number 
# in the left list appears in the right lists.
# Then do <num> * <num of times it appears in the right list> and add it to the score
def part2():
    score = 0
    list1, list2 = parse_input_into_lists()

    for num in list1:
        times_in_second_list = list2.count(num)
        score += num * times_in_second_list

    return score


if __name__ == "__main__":
    p1_answer = part1()
    print(f"Part 1: {p1_answer}")

    p2_answer = part2()
    print(f"Part 2: {p2_answer}")