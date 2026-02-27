from sympy import symbols, expand, Poly, factor

"""x^(n) represents the falling factorial while x^{n} or x^n represents a normal power."""

def falling_factorial(x, m):
    """Computes x^(m)"""
    result = 1
    for i in range(m):
        result *= (x - i)
    return result


def power_to_falling_factorials_coeffs(a):
    """
    Find coefficients c[n] such that:
        k^a = sum_{n=1}^{a} c[n] * k^{(n)}

    Uses the triangular method from the README: at each step, the leading term
    of the remainder uniquely determines the next coefficient c[n].
    """
    k = symbols('k')
    remainder = k**a
    coeffs = {}

    for falling_exponent in range(a, 0, -1):
        # Match the next highest degree exponent
        c = Poly(expand(remainder), k).nth(falling_exponent)
        coeffs[falling_exponent] = c

        #Subtract the contribution from the entire falling factorial we just matched.
        remainder = expand(remainder - c * falling_factorial(k, falling_exponent))

    return coeffs


def sum_falling_factorial(n, m):
    """
    Computes the sum from 1 to n of k^(m) using the antidifference.
    Since the antidiffernece of k^(m) is k^(m+1) / (m+1) The sum is given by 
    sum_{k=1}^{n} k^(m) = (n+1)^(m+1) / (m+1) - 1^(m+1) / (m+1)
                        = (n+1)^(m+1) / (m+1)
    Note that 1^(n) = 0 for n > 1.
    """
    return falling_factorial(n + 1, m + 1) / (m + 1)


def sum_power(a):
    """
    Return a symbolic closed form for sum_{k=1}^{n} k^a.
    """
    n = symbols('n')
    coeffs = power_to_falling_factorials_coeffs(a)
    result = sum(
        coeffs[m] * sum_falling_factorial(n, m)
        for m in range(1, a + 1)
    )
    return factor(result)


if __name__ == '__main__':
    for a in range(1, 7):
        print(f"sum_{{k=1}}^{{n}} k^{a} = {sum_power(a)}")
