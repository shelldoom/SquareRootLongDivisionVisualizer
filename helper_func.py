from typing import Union


def get_such_num(dividend: int, initial_digits: int) -> int:
    """
    Example 1: \n
    dividend = 100 \n
    initial_digits = 2 \n
    A number 2x is found such that 2x * x <= 100 \n
    where 0 <= x <= 9 \n
    We need to find x\n
    For x = 1, 21 * 1 = 21 < = 100 ✔ \n
    For x = 2, 22 * 2 = 44 <= 100 ✔ \n
    For x = 3, 23 * 3 = 66 <= 100 ✔ \n
    For x = 4, 24 * 4 = 96 <= 100 ✔ \n
    For x = 5, 25 * 5 = 125 > 100 ✘ This is greater than 100  \n
    We pick x = 4 as the answer since 24 * 4 is closest to 100.
    The returned number here is 24. \n

    Example 2: \n
    dividend = 6400 \n
    inital_digits = 88 \n
    A number 88x is found such that 88x * x <= 6400 \n
    where 0 <= x <= 9 \n
    We need to find x\n
    For x = 1, 881 * 1 = 881  <= 6400 ✔ \n
    For x = 2, 882 * 2 = 1764 <= 6400 ✔ \n
    For x = 3, 883 * 3 = 2649 <= 6400 ✔ \n
    For x = 4, 884 * 4 = 3536 <= 6400 ✔ \n
    For x = 5, 885 * 5 = 4425 <= 6400 ✔ \n
    For x = 6, 886 * 6 = 5316 <= 6400 ✔ \n
    For x = 7, 887 * 7 = 6209 <= 6400 ✔ \n
    For x = 8, 888 * 8 = 7104 > 6400  ✘ This is greater than 6400.  \n
    We pick x = 7 as the answer since 887 * 7 is closest to 6209.
    The returned number here is 887.
    """
    distance = dividend + 1
    final_divisor = int(str(initial_digits) + "9")

    for i in range(0, 10):
        cur_divisor = int(str(initial_digits) + str(i))
        cur_distance = dividend - cur_divisor * i
        if cur_distance < 0:
            break
        if cur_distance == 0:
            return cur_divisor
        if cur_distance < distance:
            distance = cur_distance
            final_divisor = cur_divisor
    return final_divisor


def is_perfect_square(num: Union[int, float]) -> bool:
    if (num ** 0.5).is_integer():
        return True
    else:
        return False