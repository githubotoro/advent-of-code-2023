import sys
import pprint

infile = open("./day-02/1-in.txt", "r")
outfile = open("./day-02/1-out.txt", "w")

sys.stdin = infile
sys.stdout = outfile

pp = pprint.PrettyPrinter(depth=float("inf"))


class Solution:
    def __init__(self) -> None:
        self.colors = set(["red", "green", "blue"])

    def getSum(self) -> int:
        limit = {"red": 12, "green": 13, "blue": 14}
        sum = 0

        while True:
            try:
                line = input()
                words = line.split(" ")

                cache = {}
                valid = True

                for curr in range(len(words)):
                    if words[curr][-1] == ":":
                        gameId = int(words[curr][:-1])
                    elif words[curr][-1] == ",":
                        color = words[curr][:-1]
                        cache[color] = int(words[curr - 1])
                    elif words[curr][-1] == ";":
                        color = words[curr][:-1]
                        cache[color] = int(words[curr - 1])

                        for color in self.colors:
                            if (
                                cache.get(color, None) != None
                                and cache[color] > limit[color]
                            ):
                                valid = False
                                cache = {}
                                break

                        if valid == True:
                            cache = {}
                    elif curr == len(words) - 1:
                        color = words[curr][:-1]
                        cache[color] = int(words[curr - 1])

                        for color in self.colors:
                            if (
                                cache.get(color, None) != None
                                and cache[color] > limit[color]
                            ):
                                valid = False
                                cache = {}
                                break

                        if valid == True:
                            cache = {}

                if valid == True:
                    sum += gameId

            except EOFError:
                break

        return sum


def main():
    s = Solution()

    sum = s.getSum()
    print(f"Sum of the IDs of games is {sum}")


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
