# The Problem

> Come up with a general method to find $\sum_{k=1}^n k^a$. If you can code, try implementing it in python/sympy.

The difficult part is finding a way to generally represent any $k^a$ as a linear combination of falling factorials.

There are a few cool ways to go about this, including using the discrete Taylor series expansion called the Newton series expansion. This can even get you a closed form! I've written out that derivation [here](Closed_form.md) because it took me too long not to.

(If you want to try this: Use the fact that $\Delta^m k^{\underline{m}} = m!$ and $\Delta^m k^r = 0 \text{ when } r < m$ and that $0^{\underline{0}} = 1$. Then use $\Delta^m f(k) = \sum_{j=0}^m (-1)^{m-j}\binom{m}{j}f(k+j)$ for the final push.) 

You can also find an algorithm by inductive construction.

Email me at kdlegum [at] gmail [dot] com if you're curious.

Below is what I think is the simplest way I've found so far and my thought process.

# Solution

We want to find coefficients $c_1, c_2, \ldots$ such that

$$k^a = c_1 k^{\underline{a}} + c_2 k^{\underline{a-1}} + c_3 k^{\underline{a-2}} + \cdots + c_a k^{\underline{1}}$$

The only term on the RHS that contributes to the coefficient of $k^a$ is $c_1 k^{\underline{a}}$. Therefore, $c_1 = 1$.

So now we have

$$k^a = k^{\underline{a}} + c_2 k^{\underline{a-1}} + c_3 k^{\underline{a-2}} + \cdots + c_{a-1} k^{\underline{1}}$$

Now we can expand $k^{\underline{a}}$, and then the only term that we can control that contributes to the coefficient of $k^{a-1}$ is $c_2 k^{\underline{a-1}}$. So now we can solve for $c_2$ by matching the coefficients of $k^{a-1}$ on both sides of the equation.

Clearly, we will be able to continue doing this until we've found all of the coefficients $c_a$.

# Notes

A linear system with this structure — where you can solve for each coefficient one at a time by matching terms — is called **triangular**.

The coefficients you've solved for are a famous result from combinatorics, called Stirling numbers of the Second Kind, denoted $S(n, m)$ where $n$ is the normal power of $k$ (i.e., corresponds to $a$) and $m$ is the falling factorial power. Feel free to look it up online!

The closed form solution to the original problem is called Faulhaber's formula or sometimes Bernoulli's formula, which is usually presented as:

$$\sum_{k=1}^{n} k^p = \frac{1}{p+1} \sum_{j=0}^{p} \binom{p+1}{j} B_j \, n^{p+1-j}$$

where $B_j$ are the Bernoulli numbers (with the convention $B_1 = +\tfrac{1}{2}$).

You can also write it directly in terms of falling factorials (closer to the approach in this solution):

$$\sum_{k=1}^{n} k^a = \sum_{m=0}^{a} \left( \frac{1}{(m+1)m!} \sum_{j=0}^{m} (-1)^{m-j} \binom{m}{j} j^a \right) (n+1)^{\underline{m+1}}$$

There are a lot of crazy looking solutions on https://en.wikipedia.org/wiki/Faulhaber%27s_formula.
