import timeit

test_data = """125 17"""
test_answer = 55312

data: str = ''
with open('.\\day_11\\data.txt', 'r') as f:
    data = f.read()

def rule(stone: str) -> list[str]:
    if stone == '0':
        return ['1']
    elif len(str(stone)) % 2 ==0:
        first = stone[:len(stone)//2]
        second = stone[len(stone)//2:]
        second_strip = str(int(second))
        return [first, second_strip]
    else:
        return [str(int(stone)*2024)]


def solve(data: str):
    stones = data.split(' ')

    for _ in range(0,25):
        new_stones = []
        for stone in stones:
            new_stones.extend(rule(stone))
        stones = new_stones
        # print(stones)

    return len(stones)

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")