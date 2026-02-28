# Discrete Calculus: Challenges & Extended Solutions

Welcome! This repository contains the detailed solutions to the challenges posed in my article *Discrete Calculus: The Power of Finite Differences*.

---

## Challenge 1: Summation by Parts

**The Problem:** 
> Show that $\Delta(u_n v_n) = v_{n+1}\Delta u_n + u_n \Delta v_n$. Use this to derive the "Summation by Parts" formula: $\sum u_n \Delta v_n = u_n v_n - \sum v_{n+1} \Delta u_n$.

### Part 1: The Discrete Product Rule
In continuous calculus, the product rule is $(uv)' = u'v + uv'$. Let's see what happens when we apply the forward difference operator $\Delta$ to a product of two sequences, $u_n$ and $v_n$.

By definition:

$$
\Delta(u_n v_n) = u_{n+1}v_{n+1} - u_n v_n
$$

To make this look like the difference operator, we need to add and subtract $u_n v_{n+1}$ in the middle of the expression.

$$
\Delta(u_n v_n) = u_{n+1}v_{n+1} - u_n v_{n+1} + u_n v_{n+1} - u_n v_n
$$

Now, factorise:

$$
\Delta(u_n v_n) = v_{n+1}(u_{n+1} - u_n) + u_n(v_{n+1} - v_n)
$$

Recognising the definitions of $\Delta u_n$ and $\Delta v_n$, we get:

$$
\Delta(u_n v_n) = v_{n+1}\Delta u_n + u_n \Delta v_n
$$


### Part 2: Deriving Summation by Parts
To derive the summation by parts formula, we take the antidifference of both sides of the result above (using $\sum \Delta f(n) = f(n)$):

$$
u_n v_n = \sum v_{n+1}\Delta u_n + \sum u_n \Delta v_n
$$

Rearranging to isolate $\sum u_n \Delta v_n$ gives us our final formula:

$$
\sum u_n \Delta v_n = u_n v_n - \sum v_{n+1} \Delta u_n
$$

---

## Challenge 2: The Discrete $xe^x$

**The Problem:** 
> Use Summation by Parts to find a closed form for $\sum_{k=1}^n k 2^k$.

In continuous calculus, integrating $\int x e^x \ dx$ requires Integration by Parts. Here, we evaluate the discrete analogue using Summation by Parts.

Let's choose u and v:
* Let $u_k = k \implies \Delta u_k = 1$
* Let $\Delta v_k = 2^k \implies v_k = 2^k$ (Using the fact that $\Delta 2^k = 2^k$)

Notice that our formula requires $v_{k+1}$. If $v_k = 2^k$, then $v_{k+1} = 2^{k+1}$.

Now, plug these into the Summation by Parts formula from Challenge 1:

$$
\sum_{k=1}^n k 2^k = [k 2^k]_{1}^{n+1} - \sum_{k=1}^n (2^{k+1})(1)
$$

First, evaluate the limits block:

$$
[k 2^k]_{1}^{n+1} = (n+1)2^{n+1} - (1)2^1 = (n+1)2^{n+1} - 2
$$

Next, evaluate the remaining sum. We can pull out a factor of $2$:

$$
\sum_{k=1}^n 2^{k+1} = 2 \sum_{k=1}^n 2^k
$$

This is a standard geometric series: $2^1 + 2^2 + \dots + 2^n = 2^{n+1} - 2$.
So, our sum evaluates to $2(2^{n+1} - 2) = 2^{n+2} - 4$.

Finally, put it all together:

$$
\sum_{k=1}^n k 2^k = \left( (n+1)2^{n+1} - 2 \right) - \left( 2^{n+2} - 4 \right)
$$

$$
= (n+1)2^{n+1} - 2^{n+2} + 2
$$

To tidy this up, we can write $2^{n+2}$ as $2 \cdot 2^{n+1}$ and factor:

$$
= 2^{n+1}(n + 1 - 2) + 2
$$

$$
= (n-1)2^{n+1} + 2
$$

---

## Challenge 3: Generalizing Polynomial Sums

**The Problem:** 
> Come up with a general method to find $\sum_{k=1}^n k^a$. If you can code, try implementing it in python/sympy.

The difficult part is finding a way to generally represent any $k^a$ as a linear combination of falling factorials.

There are a few cool ways to go about this, including using the discrete Taylor series expansion called the Newton series expansion. This can even get you a closed form! I've written out that derivation [here](Closed_form.md) because it took me too long not to.

(If you want to try this: Use the fact that $\Delta^m k^{\underline{m}} = m!$ and $\Delta^m k^r = 0 \text{ when } r < m$ and that $0^{\underline{0}} = 1$. Then use $\Delta^m f(k) = \sum_{j=0}^m (-1)^{m-j}\binom{m}{j}f(k+j)$ for the final push.) 

You can also find an algorithm by inductive construction. Email me at `kdlegum [at] gmail [dot] com` if you're curious.

Below is what I think is the simplest way I've found so far and my thought process.

### Solution

We want to find coefficients $c_1, c_2, \ldots$ such that:

$$
k^a = c_1 k^{\underline{a}} + c_2 k^{\underline{a-1}} + c_3 k^{\underline{a-2}} + \cdots + c_a k^{\underline{1}}
$$

The only term on the RHS that contributes to the coefficient of $k^a$ is $c_1 k^{\underline{a}}$. Therefore, $c_1 = 1$.

So now we have:

$$
k^a = k^{\underline{a}} + c_2 k^{\underline{a-1}} + c_3 k^{\underline{a-2}} + \cdots + c_{a-1} k^{\underline{1}}
$$

Now we can expand $k^{\underline{a}}$, and then the only term that we can control that contributes to the coefficient of $k^{a-1}$ is $c_2 k^{\underline{a-1}}$. So now we can solve for $c_2$ by matching the coefficients of $k^{a-1}$ on both sides of the equation.

Clearly, we will be able to continue doing this until we've found all of the coefficients $c_a$.

An implementation of this in python is in this repo.

### Notes

A linear system with this structure — where you can solve for each coefficient one at a time by matching terms — is called **triangular**.

The coefficients you've solved for are a famous result from combinatorics, called Stirling numbers of the Second Kind, denoted $S(n, m)$ where $n$ is the normal power of $k$ (i.e., corresponds to $a$) and $m$ is the falling factorial power. Feel free to look it up online!

The closed form solution to the original problem is called **Faulhaber's formula** or sometimes Bernoulli's formula, which is usually presented as:

$$
\sum_{k=1}^{n} k^p = \frac{1}{p+1} \sum_{j=0}^{p} \binom{p+1}{j} B_j \, n^{p+1-j}
$$

where $B_j$ are the Bernoulli numbers (with the convention $B_1 = +\frac{1}{2}$).

There are also a lot of crazy looking solutions on the [Faulhaber's formula Wikipedia page](https://en.wikipedia.org/wiki/Faulhaber%27s_formula).
