from math import floor
def climbStairs(n: int) -> int:
    num: int = 1
    even = True if n % 2 == 0 else False
    if not even:
        i: int = 1
        while i <= floor(n / 2):
            num += n - i
            i += 1
    return num
