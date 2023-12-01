import sys
import pprint

infile = open("./day-01/1-in.txt", "r")
outfile = open("./day-01/1-out.txt", "w")

sys.stdin = infile
sys.stdout = outfile

pp = pprint.PrettyPrinter(depth=float("inf"))


class Solution:
    def __init__(self) -> None:
        pass

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
            for idx in range(len(calibration)):
                if calibration[idx].isdigit():
                    first = int(calibration[idx])
                    break

            for idx in range(len(calibration) - 1, -1, -1):
                if calibration[idx].isdigit():
                    last = int(calibration[idx])
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
