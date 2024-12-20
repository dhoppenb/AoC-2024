import timeit

test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""
test_answer = 11

data: str = ''
with open('.\\day_1\\data.txt', 'r') as f:
    data = f.read()

def read_lists(data: str) -> tuple[list[int], list[int]]:
    list1: list[int] = []
    list2: list[int] = []
    for row in data.splitlines():
        a, b = map(int, row.split())
        list1.append(a)
        list2.append(b)
    list1.sort()
    list2.sort()
    return list1, list2

def solve(data: str):
    (list1, list2) = read_lists(data)
    return sum([abs(a-b) for a, b in zip(list1, list2)])

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")