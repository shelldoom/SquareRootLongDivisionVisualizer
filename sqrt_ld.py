from helper_func import get_such_num

def sqrt_long_div(num: int, precision:int = 5):
    '''
    Helps visualize the long division process calculation for square root of a number

    Parameters:
    -----
        num (int, float): the number whose square root is to be calculated.
        precision (int): the number which decides the square root's decimal places 

    Returns the square root of a number with the given precision, which is computed using the long division method.
    '''
    
    # Change num to int if it is type(num) == float but num is integer
    # Example - 2.00 is integer but has the type float, so it is converted to int
    num = int(num) if num.is_integer() else num

    integer_part = int(num)
    integer_part_str = str(integer_part)

    # decimal_count is the number of decimal digits after the dot '.'
    # To understand why decimal_part is being rounded
    # Read this -> https://stackoverflow.com/questions/10403434/floating-point-in-python-gives-a-wrong-answer
    if isinstance(num, float):
        decimal_count = len(str(num)[str(num).index(".")+1:])
        decimal_part = num - int(num)
        decimal_part = round(decimal_part, decimal_count + 3)

    # ---- STEP 1: Calculating the integer part of the quotient ---- 

    # Integer part is of even length
    if len(str(integer_part)) % 2 == 0:
        dd = [integer_part_str[i] + integer_part_str[i+1] for i in range(0, len(integer_part_str), 2)]    
    # Integer Part is of odd length
    else:
        dd = [integer_part_str[0]]
        dd += [integer_part_str[i] + integer_part_str[i+1] for i in range(1, len(integer_part_str), 2) if i < len(integer_part_str)]

    dd_i = list(map(int, dd))
    divisor = []
    dividend = []
    quotient = []
    rem = []

    for i in range(len(dd)):
        if i == 0:
            dividend.append(dd_i[0])
            divisor.append(int(dd_i[0]**0.5))
            quotient.append(divisor[-1])
            rem.append(int(dd_i[0]) - int(quotient[-1])**2)
        else:
            dividend.append(int(str(rem[-1]) + dd[i]))
            new_divisor = get_such_num(dividend[-1], quotient[-1] + divisor[-1])
            divisor.append(new_divisor)
            quotient.append(divisor[-1]%10)
            rem.append(dividend[-1] - divisor[-1]*quotient[-1])

    quotient_str = "".join(map(str, quotient))



    # ---- STEP 2: Calculating the decimal part of the quotient ---- 

    quotient_str += "."

    if isinstance(num, float):
        # Getting digits after 0.
        # Example - 0.231412
        # We want 231412
        decimal_part_str = str(decimal_part)[2:]
        num_precision = len(decimal_part_str) 
        if len(decimal_part_str) % 2 == 1:
            decimal_part_str += "0"
        after_dd = [decimal_part_str[i] + decimal_part_str[i+1] for i in range(0, len(decimal_part_str), 2)] + ["00" for _ in range(abs(precision-num_precision))]
    else:
        after_dd = ["00" for _ in range(precision)]

    after_dividend  = []
    after_quotient  = []
    after_divisor   = []
    after_rem       = []

    for i in range(len(after_dd)):
        if i == 0:
            new_dividend = int(str(rem[-1]) + after_dd[0])
            after_dividend.append(new_dividend)
            new_divisor = get_such_num(new_dividend, divisor[-1] + quotient[-1])
            after_divisor.append(new_divisor)
            after_quotient.append(new_divisor%10)
            new_rem = new_dividend - after_divisor[-1]*after_quotient[-1]
            after_rem.append(new_rem) 
        else:
            new_dividend = int(str(after_rem[-1]) + after_dd[i])
            after_dividend.append(new_dividend)
            new_divisor = get_such_num(new_dividend, after_divisor[-1] + after_quotient[-1])
            after_divisor.append(new_divisor)
            after_quotient.append(new_divisor%10)
            new_rem = new_dividend - after_divisor[-1]*after_quotient[-1]
            after_rem.append(new_rem)

    quotient_str += "".join(map(str, after_quotient))

    # print(f"{dividend=}")
    # print(f"{divisor=}")
    # print(f"{quotient=}")
    # print(f"{rem=}")
    # print("After dot")
    # print(f"{after_dividend=}")
    # print(f"{after_divisor=}")
    # print(f"{after_quotient=}")
    # print(f"{after_rem=}")


    # Printing the steps
    assumed_num = "".join(dd) + "." + "".join(after_dd)
    if (num**0.5).is_integer():
        assumed_num = str(int(num))
        quotient_str = str(int(float(quotient_str)))

    top_bar = "-"*(len(quotient_str) + 10) if len(assumed_num) < len(quotient_str) else "-"*(len(assumed_num) + 10) 
    quotient_bar = quotient_str.center(len(top_bar))

    divisor_space = " "
    divisor_space_count = 0
    divisor_space_limit = len(str(after_divisor[-1])) + 3
    print("")
    print(" "*divisor_space_limit + quotient_bar)
    print(" "*divisor_space_limit + top_bar)
    # dividend[0] = num
    dividend[0] = assumed_num

    # Print steps for integer part
    for i in range(len(dividend)):
        print(str(divisor[i]).rjust(divisor_space_limit), end=" |")
        print(divisor_space + str(dividend[i]))
        print(" "*divisor_space_limit + " |" + divisor_space + str(divisor[i]*quotient[i]))
        print(" "*divisor_space_limit + top_bar.replace("-", "_"))
        divisor_space_count+=1
        divisor_space = " "*divisor_space_count

    _bar = "_"*len(top_bar)

    if (num**0.5).is_integer():
        print(" "*divisor_space_limit + " |" + divisor_space + "0")
        return quotient_str

    if len(" "*len(after_quotient)) + len(str(after_dividend[-1])) - len(_bar) > 0:
        _bar += "_"*(len(" "*len(after_quotient)) + len(str(after_dividend[-1])) - len(_bar) + 5)
    

    for i in range(len(after_dividend)):
        print(str(after_dividend[i]).rjust(divisor_space_limit), end=" |")
        print(divisor_space + str(after_dividend[i]))
        print(" "*divisor_space_limit + " |" + divisor_space + str(after_divisor[i]*after_quotient[i]))
        print(" "*divisor_space_limit + _bar)
        divisor_space_count+=1
        divisor_space = " "*divisor_space_count

    print(" "*divisor_space_limit + " |" + divisor_space + str(after_rem[-1]))

    # NOTE: The identation given between | character (pipe) & dividend increases by 1 every step.
    # In other words, a fake indentation is given at every step.

    return quotient_str

if __name__ == "__main__":
    print("--- Square Root of a Number Long Division Visualizer ---")
    num = float(input("Enter the number: "))
    if num < 0:
        print("Doesn't work with negative numbers")
        exit()
    precision = input("Enter the precision (default = 5): ")
    
    
    if precision == '' or precision is None:
        print("\n")
        sqrt_long_div(num)
    else:
        if int(precision) <= 0:
            print("Precision has to be greater than 0.")
            exit()
        print("\n")
        sqrt_long_div(num, precision=int(precision))
    
