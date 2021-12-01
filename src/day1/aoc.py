import yaml

def part_one():
    with open('aoc1.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    count = 0
    for i, j in zip(data, data[1:]):
        if i < j:
            count += 1
    print(count)

def part_two():
    with open('aoc1.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    count = 0
    cache = list()
    for i, j, z in zip(data, data[1:], data[2:]):
        sum = i + j + z
        cache.append(sum)
    for i, j in zip(cache, cache[1:]):
        if i < j:
            count += 1
    print(count)

if __name__ == '__main__':
    part_one()
    part_two()