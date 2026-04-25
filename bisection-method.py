def square_root_bisection(number, tolerance=1e-3, maximum=100):
    if number < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )
    elif number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    else:
        low = 0.0
        high = max(1.0, number)

        for _ in range(maximum):
            mid = (low + high) / 2.0
            square = mid**2

            if high - low <= tolerance:
                print(f"The square root of {number} is approximately {mid}")
                return mid
            else:
                if square < number:
                    low = mid
                else:
                    high = mid

        print(f"Failed to converge within {maximum} iterations")
        return None
