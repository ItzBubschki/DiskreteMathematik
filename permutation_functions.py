from abc import abstractproperty


def cycle_to_tupel(cycles):
    size = len([item for sublist in cycles for item in sublist])
    tupel = [0]*size
    for cycle in cycles:
        if len(cycle) > 1:
            for i in range(len(cycle)):
                next = (i+1)%len(cycle)
                tupel[cycle[i]-1] = cycle[next]
        else:
            tupel[cycle[0]-1] = cycle[0]
    return tupel

def tupel_to_cycle(tupel):
    new_tupel = tupel.copy()
    cycles = []
    for i in range(len(tupel)):
        if i == new_tupel[i]-1:
            cycles.append([i+1])
        elif new_tupel[i] != -1:
            cycle = []
            cycle.append(i+1)
            curr = tupel[i]
            while curr != i+1:
                cycle.append(curr)
                new_tupel[curr-1] = -1
                curr = tupel[curr-1]
            cycles.append(cycle)
    return cycles

def permutation_matrix(tupel):
    matrix = []
    for i in range(len(tupel)):
        matrix.append([0]*len(tupel))
    for i in range(len(tupel)):
        matrix[i][tupel[i]-1] = 1
    return matrix

def fixpoints(tupel):
    fixpoints = []
    for i in range(len(tupel)):
        if i == tupel[i]-1:
            fixpoints.append(i+1)
    return fixpoints

cycles = [[1,2,5], [3], [4]]
tupel = cycle_to_tupel(cycles)
print(tupel)
print(tupel_to_cycle(tupel))
matrix = permutation_matrix(tupel)

print('\n'.join([''.join([f"{'{'}:{len(matrix)}{'}'}".format(item) for item in row])
      for row in matrix]))

print(fixpoints(tupel))