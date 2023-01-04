f = open('python.txt', 'r')


for line in f:
    list_data = line.split()
    print(list_data[0], list_data[1], end='\t')

    print('sum', int(list_data[0]) + int(list_data[1]))
