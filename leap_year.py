import sys

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

if __name__ == "__main__":
    y = int(sys.argv[1])
    if is_leap_year(y):
        print(f"{y} is a leap year")
    else:
        print(f"{y} is not a leap year")