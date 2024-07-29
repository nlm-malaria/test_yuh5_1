# write a function that create a 4x4 matrix and print it

def create_matrix():
    matrix = []
    for i in range(4):
        matrix.append([0, 0, 0, 0])
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


matrix = create_matrix()
print_matrix(matrix)

