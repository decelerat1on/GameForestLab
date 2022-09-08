map = """
         ╔══╗
         ║st║
         ╠══╣
         ║в1║
         ╠══╣
         ║в1║
╔══╦══╦══╬══╬══╦══╗   
║в3║в1║в1║в1║зз║зз║
╚══╩══╬══╬══╩══╩══╝
      ║в2║
╔══╦══╬══╬══╗ 
║зз║зз║в1║в2║
╚══╩══╩══╬══╣
         ║12║
╔══╦══╦══╬══╣
║в3║12║в2║в2║
╠══╬══╩══╩══╝
║зз║
╠══╣
║бб║
╚══╝
"""
def move_hero(direction):
    mapclear = ''
    cord = []
    mapsplit = map.split('\n')
    for cell in range(2,len(mapsplit)-1,2):
        mapcell = mapsplit[cell].split('║')
        if 'st' in mapcell:
            cord.append(cell)
        for cell in mapcell:
            if cell != '' or cell != '         ':
                pass
        print(mapcell)
def row(a,b,z,c,x):
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



def create_map(x,y):
    y = y * 2 + 1
    map1 = ''
    for row1 in range(y):
        if row1 == 0:
            map1 += row('╔','═','╦','╗',x)
        elif row1 % 2 == 1:
            map1 += row('║',' ','║','║',x)
        elif row1 - (y - 1) == 0:
            map1 += row('╚','═','╩','╝',x)
        else:
            map1 += row('╠','═','╬','╣',x)
    return map1


print(create_map(4,5))

# mapsplit = map.split('\n')
# print(mapsplit)
# cell = mapsplit[2].split('║')
# print(cell)