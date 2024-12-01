def day1(filename='input.txt'):
    left_list = [] 
    right_list = [] 
    total_distance = 0
    with open(filename) as file:
        for line in file:
            left, right = line.strip().split()
            right_list.append(int(right))
            left_list.append(int(left))

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])

    return total_distance

print(day1())

def day2(filename='input.txt'):
    left_list = []
    right_list = []
    similarity_score = 0
    with open(filename) as file:
        for line in file:
            left, right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))
            
    
    for number in left_list:
        similarity_score += number * right_list.count(number)
    
    return similarity_score

print(day2())