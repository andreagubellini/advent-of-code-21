import yaml

def part1():
    depth = 0
    horizontal_pos = 0
    with open("aoc2.yml", 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            for i in data:
                i = i.split()
                if i[0] == 'forward':
                    horizontal_pos += int(i[1])
                elif i[0] == 'up':
                    depth -= int(i[1])
                else:
                    depth += int(i[1])
                 
            print(int(horizontal_pos) * int(depth)) 
        except yaml.YAMLError as exc:
            print(exc)

def part2():
    depth = 0
    horizontal_pos = 0
    aim = 0
    with open("aoc2.yml", 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            for i in data:
                i = i.split()
                if i[0] == 'forward':
                    horizontal_pos += int(i[1])
                    depth += aim*int(i[1])
                elif i[0] == 'up':
                    aim -= int(i[1])
                else:
                    aim += int(i[1])
            print(int(horizontal_pos) * int(depth)) 
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == '__main__':
    part1()  
    part2()