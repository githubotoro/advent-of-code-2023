import sys
import pprint

infile = open("./day-02/2-in.txt", "r")
outfile = open("./day-02/2-out.txt", "w")

sys.stdin = infile
sys.stdout = outfile

pp = pprint.PrettyPrinter(depth=float("inf"))


class Solution:
    def __init__(self) -> None:
        self.map = {
            "r": "red",
            "g": "green",
            "b": "blue",
        }

    def getSum(self) -> int:
        limit = {"red": 12, "green": 13, "blue": 14}
        sum = 0

        while True:
            try:
                line = input()
                words = line.split(" ")

                power = 1

                cache = {}

                for curr in range(len(words)):
                    if words[curr][-1] == ":":
                        gameId = int(words[curr][:-1])
                    elif words[curr].isnumeric():
                        balls = int(words[curr])
                        key = words[curr + 1][0]
                        color = self.map[key]

                        if cache.get(color, None) == None or balls > cache[color]:
                            cache[color] = balls

                for key in cache.keys():
                    power *= cache[key]

                sum += power

            except EOFError:
                break

        return sum


def main():
    s = Solution()

    sum = s.getSum()
    print(f"Sum of the power of sets is {sum}")


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
