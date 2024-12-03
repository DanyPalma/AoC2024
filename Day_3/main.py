import re

def part1(filename: str) -> int: 
    pattern = r'\bmul\(\d+,\d+\)\b'
    sum_of_mul = 0
    
    with open(filename) as file:
        for line in file:
            matches = re.findall(pattern, line)
            for match in matches:
                split  = re.search(r'mul\((\d+),(\d+)\)', match)
                if split:
                    numbers = [int(split.group(1)), int(split.group(2))]
                    sum_of_mul += (numbers[0] * numbers[1])
            
        
    return sum_of_mul

print(part1('input.txt'))