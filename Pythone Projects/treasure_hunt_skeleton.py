d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', '2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', '#': ' '}
d2 = {'C': 'W', '3': 'W', 'F': 'W', '0': 'T', '2': 'T', '4': 'T', 'B': '.', '+': '.', ';': '.', 'Q': '^', '7': '^', '8': '^', 'D': 'E', '1': 'E', 'Z': 'E', '(': 'M', ')': 'M', '9': 'M', '*': ':', '|': ':', '#': ':', 'X': ' ', 'P': ' ', '!': ' '}
        
def decode_map(mapfile,ddict,outfile):
    # open thfile
    with open(mapfile, 'r') as maps:
        # open a new file
        with open(outfile, 'w') as decode_maps:
            # identify the key and its value
            for line in maps:
                decode_line = line.rstrip('\n')
                for char in decode_line:
                    if char in ddict.keys():
                        # write the values in the outfile
                        decode_maps.write(ddict[char])
                    else:
                        decode_maps.write(char)
                decode_maps.write('\n')
    pass
                    
                    
def find_treasure(mapfile):
    # open mapfile
    with open(mapfile, 'r') as treasure:
        # find number of rows
        # find the coordinate of "T"
        treasure_lst = []
        for line in treasure:
            treasure_line = line.rsplit('\n')
            treasure_lst.append(treasure_line)
            
        row = len(treasure_lst)
        column = len(treasure_lst[0])

        for r in range(row):
            for c in range(column):
                if 'TTT' in treasure_lst[r][c]:
                    return (r,c)
        #
        # in                      'T'
        #                       'T"T"T'
        #                         'T'
        # return the coordinate of "T"

print("Map 1")
decode_map('encoded_map.txt',d1,'decoded_map.txt')
print(find_treasure('decoded_map.txt'))

# Uncomment the following for your test cases

print("Map 2")
decode_map('encoded_map2.txt',d1,'decoded_map2.txt')
print(find_treasure('decoded_map2.txt'))

print("Map 3")
decode_map('encoded_map3.txt',d1,'decoded_map3.txt')
print(find_treasure('decoded_map3.txt'))

print("Map 5")
decode_map('encoded_map5.txt',d1,'decoded_map5.txt')
print(find_treasure('decoded_map5.txt'))

print("Map 1 B")
decode_map('encoded_mapB.txt',d2,'decoded_mapB.txt')
print(find_treasure('decoded_mapB.txt'))

