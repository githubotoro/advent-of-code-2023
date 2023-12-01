import sys
import pprint

infile = open("./day-01/2-in.txt", "r")
outfile = open("./day-01/2-out.txt", "w")

sys.stdin = infile
sys.stdout = outfile

pp = pprint.PrettyPrinter(depth=float("inf"))


class Solution:
    def __init__(self) -> None:
        self.cache = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        self.letters = {
            "o": [3],
            "t": [3, 5],
            "f": [4, 4],
            "s": [3, 5],
            "e": [5],
            "n": [4],
        }

    def getCalibrationSum(self) -> int:
        calibrations = []

        sum = 0

        while True:
            try:
                calibration = input()
                calibrations.append(calibration)
            except EOFError:
                break

        for calibration in calibrations:
            first = -1
            last = -1

            for idx in range(len(calibration)):
                if calibration[idx].isdigit():
                    first = int(calibration[idx])
                elif self.letters.get(calibration[idx], None) != None:
                    for possibleLength in self.letters.get(calibration[idx], None):
                        if possibleLength + idx <= len(calibration):
                            if (
                                self.cache.get(
                                    calibration[idx : idx + possibleLength], None
                                )
                                != None
                            ):
                                first = self.cache[
                                    calibration[idx : idx + possibleLength]
                                ]

                if first != -1:
                    break

            for idx in range(len(calibration) - 1, -1, -1):
                if calibration[idx].isdigit():
                    last = int(calibration[idx])
                elif self.letters.get(calibration[idx], None) != None:
                    for possibleLength in self.letters.get(calibration[idx], None):
                        if possibleLength + idx <= len(calibration):
                            if (
                                self.cache.get(
                                    calibration[idx : idx + possibleLength], None
                                )
                                != None
                            ):
                                last = self.cache[
                                    calibration[idx : idx + possibleLength]
                                ]

                if last != -1:
                    break

            num = first * 10 + last
            sum += num

        return sum


def main():
    s = Solution()

    calibrationSum = s.getCalibrationSum()
    print(f"Sum of all of the calibration values is {calibrationSum}")


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
