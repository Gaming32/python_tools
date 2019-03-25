"Module for creating and handling list matrices (objects in a matrix can also be accessed via matrix[x][y])"

import copy
def create_matrix(width, height, obj=None, deepcopy=False, command=None, **increment):
    """
    Returns a matrix of the specified object for the specifed width and height;
    Every object in the increment increments by one every time an object is created;

    deepcopy
        Whether to deepcopy the object instead of simply copying it
    command
        A function with the argument interface (obj, x, y, **increment) and returns the modified object
    increment
        A set of "name=starting_value" pairs that increment on each loop of the matrix insertion
    """
    matrix = []
    for x in range(width):
        matrix.append([])
        for y in range(height):
            if deepcopy:
                matrix[x].append(copy.deepcopy(obj))
            else:
                matrix[x].append(copy.copy(obj))
            if obj != None:
                matrix[x][y].__dict__.update(increment)
            if command:
                matrix[x][y] = command(matrix[x][y], x, y)
            for key in increment:
                increment[key] += 1
    return matrix

def getmatrixobjs(matrix):
    "Returns a list of tuples of the pattern (obj, x, y)"
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            yield matrix[x][y], x, y

def getmatrixobj(matrix, x, y):
    "Returns the obj at the specifed x and y"
    return matrix[x][y]

if __name__ == "__main__":
    import person
    bob = person.Person('Bob Smith')
    print(dir(bob))
    matrix = create_matrix(21, 13, bob, pay=0)
    import pprint
    for x in matrix:
        for y in x:
            print(y)