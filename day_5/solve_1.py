import timeit
import pprint

test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
test_answer = 143

data: str = ''
with open('.\\day_5\\data.txt', 'r') as f:
    data = f.read()

def middle_val(l: list[str]) -> int:
    middle_ix = len(l) // 2
    return int(l[middle_ix])

def valid_item_list(item_str: str, adj_list: dict) -> bool:
    rev_list = item_str.split(',')[::-1]
    for i, item in enumerate(rev_list):
        for j in range(i+1, len(rev_list)):
            if item in adj_list and adj_list[item].count(rev_list[j]) > 0:
                return False
    return True

def solve(data: str):
    split = data.split('\n\n')
    orderings = split[0].splitlines()
    itemlists = split[1].splitlines()

    adj_list = {}
    for ordering in orderings:
        a, b = ordering.split('|')
        if a not in adj_list:
            adj_list[a] = []
        adj_list[a].append(b)
    
    return sum([middle_val(itemlist.split(',')) for itemlist in itemlists if valid_item_list(itemlist, adj_list)])

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")