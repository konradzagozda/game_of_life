import copy

# n <- ilość kolumn
# m <- ilość wierszy

n = 20
m = 12
#filepath = '...'


# # input:
# with open(filepath) as f:
#     generation1 = [list(x[:-1]) if x[-1] == '\n' else list(x) for x in f.readlines()]


input = """....................
....................
....................
....................
.......X.XX.........
.......XXX..........
........X...........
....................
....................
....................
....................
...................."""

generation1 = [x for x in input.split('\n')]
print(generation1)

def check(c):
    return True if c == 'X' else False


def find_next_gen(generation):
    generation2 = [['.' for x in range(n)] for x in range(m)]
    # generation2 = generation1[:]
    # generation2 = generation1.copy()

    for i, row in enumerate(generation1):
        for j, element in enumerate(row):

            # checking alive_neighbours:
            alive_neighbours = 0

            # same row:
            alive_neighbours += check(generation1[i][j - 1] if j != 0 else generation1[i][-1])
            alive_neighbours += check(generation1[i][j + 1] if j != n - 1 else generation1[i][0])

            # row above:
            if i == 0:
                row_num_above = -1
            else:
                row_num_above = i - 1
            alive_neighbours += check(generation1[row_num_above][j - 1] if j != 0 else generation1[row_num_above][-1])
            alive_neighbours += check(generation1[row_num_above][j])
            alive_neighbours += check(generation1[row_num_above][j + 1] if j != n - 1 else generation1[row_num_above][0])

            # row beneath:
            if i == m - 1:
                row_num_beneath = 0
            else:
                row_num_beneath = i + 1
            alive_neighbours += check(generation1[row_num_beneath][j - 1] if j != 0 else generation1[row_num_beneath][-1])
            alive_neighbours += check(generation1[row_num_beneath][j])
            alive_neighbours += check(generation1[row_num_beneath][j + 1] if j != n - 1 else generation1[row_num_beneath][0])

            # create new generation:
            if generation1[i][j] == 'X' and 3 >= alive_neighbours >= 2 or generation1[i][j] == '.' and alive_neighbours == 3:
                generation2[i][j] = 'X'
            else:
                generation2[i][j] = '.'
    return generation2


def count_alive(generation):
    alives = 0
    for x in generation:
        for y in x:
            if y == 'X':
                alives += 1
    return alives


generations = []
generations.append((copy.deepcopy(generation1)))

# zmienna z pokoleniami od 1 do 101
for x in range(100):
    next_gen = find_next_gen(generation1)
    generation1 = next_gen
    generations.append(copy.deepcopy(generation1))

# 51 generation
for i, x in enumerate(generations):
    if i == 0:
        continue
    elif generations[i] == generations[i-1]:
        print(i)

print(count_alive(generations[50]))

for x in generations[50]:
    print(''.join(x))

