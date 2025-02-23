import timeit
from queue import PriorityQueue

test_data = """2333133121414131402"""
test_answer = 2858

data: str = ''
with open('.\\day_9\\data.txt', 'r') as f:
    data = f.read()

def checksum(diskstring: list[int]) -> int:
    result = 0
    for i, ID in enumerate(diskstring):
        if not ID == -1:
            result += i * ID
    return result

def map_to_disk(diskmap: str)-> tuple[list, list]:
    regions = []    

    index = 0
    isFile = True
    result = []
    for i, c in enumerate(diskmap):
        if isFile:
            result += [index] * int(c)
            regions.append((i, index, int(c)))
            index += 1
        else:
            result += [-1] * int(c)
            regions.append((i,-1,int(c))) 
        isFile = not isFile
    return result, regions

def compact(disk: list[int]) -> list[int]:
    start, end = 0, len(disk)
    while start < end:
        # end point on empty space
        if disk[end-1] == -1:
            end -= 1
        # start point on empty space and end on block
        elif disk[start] == -1 and disk[end-1] != -1:
            disk[start], disk[end-1] = disk[end-1], disk[start]
            start += 1
            end -= 1
        # start point on block
        elif disk[start] != -1:
            start += 1
    return disk

def compact2(disk: list[int], free_blocks) -> list[int]:
    
    return [1,2,3,4]
'''
Files are now moved in their entirety
Use a list of blocksets [(start_ix, id_1, len_1), (start_ix+len_1, -1, len), ...]
Potentially storing start index for easier reconstruction
'''
def solve(data: str):
    # Done
    disk, free_blocks = map_to_disk(data)
    print(f'disk: {disk}')
    print(f'free blocks: {free_blocks}')

    # Done
    compacted = compact2(disk, free_blocks)
    # print(compacted)

    return checksum(compacted)

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")