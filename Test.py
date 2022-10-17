# -*- coding: utf-8 -*-
# map = """
#          ╔══╗
#          ║st║
#          ╠══╣
#          ║в1║
#          ╠══╣
#          ║в1║
# ╔══╦══╦══╬══╬══╦══╗
# ║в3║в1║в1║в1║зз║зз║
# ╚══╩══╬══╬══╩══╩══╝
#       ║в2║
# ╔══╦══╬══╬══╗
# ║зз║зз║в1║в2║
# ╚══╩══╩══╬══╣
#          ║12║
# ╔══╦══╦══╬══╣
# ║в3║12║в2║в2║
# ╠══╬══╩══╩══╝
# ║зз║
# ╠══╣
# ║бб║
# ╚══╝
# """

def row(a, b, z, c, x):  # создание строки карты
    map1 = ''
    for col in range((x * 2) + 1):
        if col == 0:
            map1 += a
        elif col % 2 == 1:
            map1 += b
        elif col - (x * 2) == 0:
            map1 += c
        else:
            map1 += z
    return map1 + '\n'


def create_map(x, y):  # создание карты
    y = y * 2 + 1
    map1 = ''
    for row1 in range(y):
        if row1 == 0:
            map1 += row('╔', '═', '╦', '╗', x)
        elif row1 % 2 == 1:
            map1 += row('║', 'x', '║', '║', x)
        elif row1 - (y - 1) == 0:
            map1 += row('╚', '═', '╩', '╝', x)
        else:
            map1 += row('╠', '═', '╬', '╣', x)
    return map1


print(create_map(8, 12))

# maptest = '''
# ╔═╦═╦═╦═╦═╦═╦═╦═╗
# ║x║x║x║x║x║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║x║x║x║H║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║x║x║x║1║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║x║x║x║1║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║3║1║1║1║з║з║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║x║x║2║x║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║з║з║1║2║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║x║x║x║2║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║3║2║2║2║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║з║x║x║x║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║б║x║x║x║x║x║x║
# ╠═╬═╬═╬═╬═╬═╬═╬═╣
# ║x║x║x║x║x║x║x║x║
# ╚═╩═╩═╩═╩═╩═╩═╩═╝
# '''


def findhero(map):  # ищем героя на карте
    map = map.split('\n')
    for splitmap in map:
        if 'H' in splitmap:
            y = map.index(splitmap)
            split1 = list(splitmap)
            x = split1.index('H')
            return (x, y)


def movehero(map, x, y, dir):  # движения героя
    map = map.split('\n')
    event = ''
    if dir == 'S':
        if map[y+2][x] != 'x':
            map[y] = map[y].replace('H',' ')
            y += 2
            event = map[y][x]
            row = list(map[y])
            row[x] = 'H'
            map[y] = ''.join(row)


    elif dir == 'W':
        if map[y - 2][x] != 'x':
            map[y] = map[y].replace('H', ' ')
            y -= 2
            event = map[y][x]
            row = list(map[y])
            row[x] = 'H'
            map[y] = ''.join(row)


    elif dir == 'A':
        if map[y][x - 2] != 'x':
            map[y] = map[y].replace('H', ' ')
            x -= 2
            event = map[y][x]
            row = list(map[y])
            row[x] = 'H'
            map[y] = ''.join(row)


    elif dir == 'D':
        if map[y][x + 2] != 'x':
            map[y] = map[y].replace('H', ' ')
            x += 2
            event = map[y][x]
            row = list(map[y])
            row[x] = 'H'
            map[y] = ''.join(row)

    temp = ''
    for element in map:
        if element == '╚═╩═╩═╩═╩═╩═╩═╩═╝':
            temp += element
        else:
            temp += element + '\n'
    return temp,x,y,event



# взять строку в которой находится герой
# превратить строку в список
# заменить героя на пустоту
# поставить героя в нужное место
# сохранить изменения в карте





print(maptest)
x, y = findhero(maptest)
while True:
    wheremove = input('Введите движение: ').upper()
    maptest,x,y,event = movehero(maptest, x, y, wheremove)
    print(maptest)

