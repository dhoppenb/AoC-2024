import timeit
import math

test_data = """125 17"""
test_answer = 55312

data: str = ''
with open('.\\day_11\\data.txt', 'r') as f:
    data = f.read()

def digit_split(i:int) -> tuple[int,int]:
    length: int = int(math.log10(i))+1
    assert length % 2 == 0
    lhs: int = i // 10**(length//2)
    rhs: int = i % 10**(length//2)
    return lhs, rhs

memo = {}

def rule_mem(stone: int, depth: int, maxdepth: int) -> int:
    if memo.__contains__((stone, depth)):
        return memo[(stone, depth)]
    else:
        if depth == maxdepth:
            result = 1
        elif stone == 0:
            result = rule_mem(1, depth+1, maxdepth)
        # even digits
        elif int(math.log10(stone)) % 2 == 1:
            lhs, rhs = digit_split(stone)
            result = rule_mem(lhs, depth+1, maxdepth) + rule_mem(rhs, depth+1, maxdepth)
        else:
            result = rule_mem(stone*2024, depth+1, maxdepth)
            
        memo[(stone, depth)] = result
        return result

# 183620 for d=25 on run input
# 55312 for d=25 on test input
def solve(data: str, depth: int = 75) -> int:
    stones = [int(c) for c in data.split(' ')]

    result = 0
    for stone in stones:
        result += rule_mem(stone, 0, depth)
        
    return result

def test():
    assert solve(test_data, depth=25) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")