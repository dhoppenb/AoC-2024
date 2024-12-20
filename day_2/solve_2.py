import timeit

from solve_1 import checkReport

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
test_answer = 4

data: str = ''
with open('.\\day_2\\data.txt', 'r') as f:
    data = f.read()

def checkReportDropOne(list: list[int]):
    valid = False
    for i in range(0, len(list)):
        drop_one_report = list[:i] + list[i+1:]
        valid = valid or checkReport(drop_one_report)
    return valid

def solve(data: str):
    reports: list[list[int]] = []
    for line in data.splitlines():
        reports.append([int(x) for x in line.split()])
    return sum([checkReportDropOne(report) for report in reports])

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")