import re
import numpy as np

def part1(filename: str) -> int: 
    pattern = r'(?<=mul\()\d{1,3},\d{1,3}(?=\))'
    sum_of_mul = 0
    
    matches = re.findall(pattern, open(filename).read())
    # print(matches) 
    
    s = [int(op.split(",")[0]) * int(op.split(",")[1]) for op in matches]
    
    # print(s)
    
    sum_of_mul = sum(s)
    
    return sum_of_mul

print(part1('input.txt'))

def part2(filename: str) -> int: 
    code = open(filename).read()
    insts = {x.span()[-1]: 0 for x in re.finditer(r'don\'t\(\)', code)}
    dos = {x: 1 for x in [0] + [x.span()[-1] for x in re.finditer(r'do\(\)', code)]}
    insts.update(dos)
    
    return sum([np.prod(np.array([int(x) for x in m.group().split(',')])) * insts[max([x for x in insts.keys() if x < m.span()[0]])] for m in re.finditer('(?<=mul\()\d{1,3},\d{1,3}(?=\))', code)])
    
print(part2('input.txt'))