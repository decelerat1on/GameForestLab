def move_hero(map, dir, x, y):
    map = map.split('\n')
    event = None
    if dir == 's':
        if map[y + 2][x] != 'x':
            map[y] = map[y].replace('H', ' ')
            y += 2
            event, row = list(map[y])[x], list(map[y])
            row[x] = "H"
            map[y] = ''.join(row)
    elif dir == 'w':
        if map[y - 2][x] != 'x':
            map[y] = map[y].replace('H', ' ')
            y -= 2
            event, row = list(map[y])[x], list(map[y])
            row[x] = "H"
            map[y] = ''.join(row)
    elif dir == 'a':
        if map[y][x - 2] != 'x':
            map[y] = map[y].replace('H', ' ')
            x -= 2
            event, row = list(map[y])[x], list(map[y])
            row[x] = "H"
            map[y] = ''.join(row)
    elif dir == 'd':
        if map[y][x + 2] != 'x':
            map[y] = map[y].replace('H', ' ')
            x += 2
            event, row = list(map[y])[x], list(map[y])
            row[x] = "H"
            map[y] = ''.join(row)
    return '\n'.join(map), x, y, event


def findhero(map):  # ищем героя на карте
    map = map.split('\n')
    for splitmap in map:
        if 'H' in splitmap:
            y = map.index(splitmap)
            split1 = list(splitmap)
            x = split1.index('H')
            return (x, y)

map = '''
╔═╦═╦═╦═╦═╗
║x║x║x║x║x║
╠═╬═╬═╬═╬═╣
║x║x║2║x║x║
╠═╬═╬═╬═╬═╣
║x║3║H║2║x║
╠═╬═╬═╬═╬═╣
║x║x║4║x║x║
╠═╬═╬═╬═╬═╣
║x║x║x║x║x║
╚═╩═╩═╩═╩═╝
'''

x, y = findhero(map)
print(x, y, map)

while True:
    dir = input("Направление: ").lower()
    map, x, y, event = move_hero(map, dir, x, y)
    print(map)
