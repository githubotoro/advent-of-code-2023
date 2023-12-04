import sys
import pprint

infile = open("./day-03/input.txt", "r")
outfile = open("./day-03/1-out.txt", "w")

sys.stdin = infile
sys.stdout = outfile

pp = pprint.PrettyPrinter(depth=float("inf"))


class Solution:
    def __init__(self) -> None:
        pass

    def check(line, idx) -> bool:
        if line[idx].isdigit() == False and line[idx] != ".":
            return True
        else:
            return False

    def getSum(self) -> int:
        sum = 0

        indices = [[-1, -1], [0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1]]
        mat = []

        while True:
            try:
                row = []
                line = input()

                for char in line:
                    row.append(char)

                mat.append(row)

            except EOFError:
                break

        for row in range(len(mat)):
            num = 0
            include = False

            for col in range(len(mat[row])):
                char = mat[row][col]

                if char.isdigit():
                    num = num * 10 + int(char)

                    for idx in indices:
                        newRow = row + idx[0]
                        newCol = col + idx[1]

                        if (
                            include == False
                            and 0 <= newRow < len(mat)
                            and 0 <= newCol < len(mat[row])
                            and mat[newRow][newCol].isdigit() == False
                            and mat[newRow][newCol] != "."
                        ):
                            include = True
                else:
                    if include == True:
                        sum += num

                    num = 0
                    include = False

            if num != 0 and include == True:
                sum += num

        return sum


def main():
    s = Solution()

    sum = s.getSum()
    print(f"Sum of all of the part numbers is {sum}")


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
