import sys
import pprint

infile = open("./day-03/input.txt", "r")
outfile = open("./day-03/2-out.txt", "w")

sys.stdin = infile
sys.stdout = outfile

pp = pprint.PrettyPrinter(depth=float("inf"))


class Solution:
    def __init__(self) -> None:
        pass

    def getSum(self) -> int:
        sum = 0

        indices = [[-1, -1], [0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1]]
        mat = []

        cache = {}

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

            candidates = set()

            for col in range(len(mat[row])):
                char = mat[row][col]

                if char.isdigit():
                    num = num * 10 + int(char)

                    for idx in indices:
                        newRow = row + idx[0]
                        newCol = col + idx[1]

                        if (
                            0 <= newRow < len(mat)
                            and 0 <= newCol < len(mat[row])
                            and mat[newRow][newCol] == "*"
                        ):

                            if (newRow, newCol) not in candidates:
                                candidates.add((newRow, newCol))
                else:
                    for candidate in candidates:
                        if cache.get(candidate, None) == None:
                            cache[candidate] = [num]
                        else:
                            currSet = set(cache[candidate])

                            if num not in currSet:
                                cache[candidate].append(num)

                    num = 0
                    candidates = set()

            if num != 0:
                for candidate in candidates:
                    if cache.get(candidate, None) == None:
                        cache[candidate] = [num]
                    else:
                        currSet = set(cache[candidate])

                        if num not in currSet:
                            cache[candidate].append(num)

        for key in cache.keys():
            if len(cache[key]) == 2:
                sum += cache[key][0] * cache[key][1]

        return sum


def main():
    s = Solution()

    sum = s.getSum()
    print(f"Sum of all of the part numbers is {sum}")


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
