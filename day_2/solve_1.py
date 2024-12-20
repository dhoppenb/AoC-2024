import timeit
import functools

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
test_answer = 2

data: str = ''
with open('.\\day_2\\data.txt', 'r') as f:
    data = f.read()

def checkReport(list: list[int]) -> bool:
    difflist = [list[i] - list[i+1] for i in range(len(list)-1)]
    mono_decr = functools.reduce(lambda x, y: x and y, [1 <= x <= 3 for x in difflist])
    mono_incrc = functools.reduce(lambda x, y: x and y, [-3 <= x <= -1 for x in difflist])
    return mono_decr or mono_incrc

def solve(data: str):
    reports: list[list[int]] = []
    for line in data.splitlines():
        reports.append([int(x) for x in line.split()])
    
    return sum([checkReport(report) for report in reports])

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")