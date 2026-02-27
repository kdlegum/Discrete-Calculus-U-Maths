# The Problem

> Come up with a general method to find $\sum_{k=1}^n k^a$. If you can code, try implementing it in python/sympy.

The difficult part is finding a way to generally represent any $k^a$ as a linear combination of falling factorials.

There are a few cool ways to go about this, including using the fact that $H_n$ is the inverse of $\ln$ in the discrete world.

You can also find an algorithm by construction by induction.

Email me at kdlegum [at] gmail [dot] com if you're curious.

Below is what I think is the simplest way I've found so far and my thought process.

# Solution

We want to find coefficients $c_1, c_2, \ldots$ such that

$$k^a = c_1 k^{\underline{a}} + c_2 k^{\underline{a-1}} + c_3 k^{\underline{a-2}} + \cdots + c_a k^{\underline{1}}$$

The only term on the RHS that contributes to the coefficient of $k^a$ is $c_1 k^{\underline{a}}$. Therefore, $c_1 = 1$.

So now we have

$$k^a = k^{\underline{a}} + c_2 k^{\underline{a-1}} + c_3 k^{\underline{a-2}} + \cdots + c_{a-1} k^{\underline{1}}$$

Now we can expand $k^{\underline{a}}$, and then the only term that we can control that contributes to the coefficient of $k^{a-1}$ is $c_2 k^{\underline{a-1}}$. So now we can solve for $c_2$ by matching the coefficients of $k^{a-1}$ on both sides of the equation.

Clearly, we will be able to continue doing this until we've found all of the coefficients $c_n$.

# Notes

Linear systems in this structure where you can solve for each coefficient one by one, matching the terms, is called **triangular**.
The coefficients you've solved for are a famous result from combinatorics, called Stirling numbers of the Second Kind, denoted $S(n, m)$ where $n$ is the normal power of $k$ (i.e., corresponds to $a$) and $m$ is the falling factorial power. Feel free to look it up online!
