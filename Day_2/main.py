def is_safe_sequence(nums):
    is_increasing = all(nums[i+1] - nums[i] >= 1 and nums[i+1] - nums[i] <= 3 for i in range(len(nums)-1))
    is_decreasing = all(nums[i] - nums[i+1] >= 1 and nums[i] - nums[i+1] <= 3 for i in range(len(nums)-1))
    return is_increasing or is_decreasing

def part1(filename: str) -> int:
    safe_levels = 0
    
    with open(filename) as file:
        for line in file:
            nums = [int(x) for x in line.strip().split()]
            
            if is_safe_sequence(nums):
                safe_levels += 1
                continue
    
    return safe_levels

print(part1('input.txt'))

def part2(filename: str) -> int:
    safe_levels = 0
    
    with open(filename) as file:
        for line in file:
            nums = [int(x) for x in line.strip().split()]
            
            if is_safe_sequence(nums):
                safe_levels += 1
                continue
            
            for i in range(len(nums)):
                modified_nums = nums[:i] + nums[i+1:]
                if is_safe_sequence(modified_nums):
                    safe_levels += 1
                    break
    
    return safe_levels

print(part2('input.txt'))