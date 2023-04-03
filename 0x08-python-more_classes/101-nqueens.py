import sys

def n_queens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def backtrack(row, columns, diagonals, anti_diagonals):
        if row == n:
            # Found a solution
            solution = []
            for i in range(n):
                row_string = ""
                for j in range(n):
                    if columns[i] == j:
                        row_string += "Q"
                    else:
                        row_string += "."
                solution.append(row_string)
            print("\n".join(solution))
            return

        for col in range(n):
            diagonal = row - col
            anti_diagonal = row + col
            if columns[col] or diagonals[diagonal] or anti_diagonals[anti_diagonal]:
                # Column or diagonal already taken
                continue

            # Mark column and diagonals
            columns[col] = True
            diagonals[diagonal] = True
            anti_diagonals[anti_diagonal] = True

            # Try next row
            backtrack(row+1, columns, diagonals, anti_diagonals)

            # Unmark column and diagonals
            columns[col] = False
            diagonals[diagonal] = False
            anti_diagonals[anti_diagonal] = False

    # Start backtrack
    columns = [False] * n
    diagonals = [False] * (2*n - 1)
    anti_diagonals = [False] * (2*n - 1)
    backtrack(0, columns, diagonals, anti_diagonals)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    n_queens(n)

