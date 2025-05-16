"""
Insert your code bellow 

our task is to implement an algorithm that can find the way out of a maze.

The maze representation is like this:

    [
      [1,1,1,1,1],
      [1,0,0,1,1],
      [1,1,0,1,1],
      [1,1,0,0,0],
      [1,1,1,1,1],
    ]

So we have a map like this

    integer 0 represents walls

    integer 1 represents valid cells

    cell (0,0) is the starting point (it is the top left corner)

    the bottom right cell is the destination (so this is what we are looking for)

So the solution should be something like this (S represents the states in the solution set):

    [
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,S,S,S,S],
    ]

Good luck!


"""
def solve_maze(maze): #la funcion maze es la representacion del laberinto
    rows, cols = len(maze), len(maze[0]) #row y cols, los numeros de filas y columnas
    path = [] #aqui se guardan las coordenadas 

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if maze[r][c] == 0 or (r, c) in path:
            return False
        path.append((r, c))
        if (r, c) == (rows - 1, cols - 1):
            return True
        if dfs(r + 1, c) or dfs(r, c + 1) or dfs(r - 1, c) or dfs(r, c - 1):
            return True
        path.pop()
        return False

    dfs(0, 0)

    result = [['-' for _ in range(cols)] for _ in range(rows)]
    for r, c in path:
        result[r][c] = 'S'
    return result


def print_maze(maze):
    for row in maze:
        print(row)
    print()


if __name__ == '__main__':
    mazes = [
        [[1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]],

        [[1, 1, 1, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 1, 1, 1]],

        [[1, 1, 0, 1, 1, 0],
         [0, 1, 0, 1, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 1]],

        [[1, 0, 1, 1, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 1, 1, 1],
         [0, 0, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1]]
    ]

    for i, maze in enumerate(mazes):
        print(f"Laberinto {i + 1}:")
        solution = solve_maze(maze)
        print_maze(solution)

