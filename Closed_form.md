# Closed form derivation

To find the closed form we start by assuming

$$k^a = \sum_{r=0}^a c_r\, k^{\underline{r}}$$

Now we apply the forward difference $\Delta$ exactly $m$ times to both sides, analogous to differentiating a Taylor series to isolate a single coefficient:

$$\Delta^m k^a = \sum_{r=0}^a c_r\, \Delta^m (k^{\underline{r}})$$

Whenever $r < m$, we have $\Delta^m (k^{\underline{r}}) = 0$, so we can raise the lower limit of the sum:

$$\Delta^m k^a = \sum_{r=m}^a c_r\, \Delta^m (k^{\underline{r}})$$

Now we plug in $k = 0$. This is useful because $0^{\underline{0}} = 1$ but $0^{\underline{r}} = 0$ for all $r > 0$.

Expanding $\Delta^m (k^{\underline{r}})$ gives

$$r(r-1)\cdots(r-m+1)\, k^{\underline{r-m}}$$

Since we are evaluating at $k = 0$, the only surviving term on the right-hand side is the one where $r - m = 0$, i.e., $r = m$. At $r = m$ we have $\Delta^m k^{\underline{m}} = m!$, so

$$\left.\Delta^m (k^a)\right|_{k=0} = c_m\, m!$$

This gives us a formula for each coefficient $c_m$:

$$c_m = \frac{\left.\Delta^m (k^a)\right|_{k=0}}{m!}$$

All that remains is a closed formula for $\left.\Delta^m (k^a)\right|_{k=0}$. We use the identity

$$\Delta^m f(k) = \sum_{j=0}^m (-1)^{m-j}\binom{m}{j}f(k+j)$$

Plugging in $f(k) = k^a$ and evaluating at $k = 0$:

$$\left.\Delta^m (k^a)\right|_{k=0} = \sum_{j=0}^m (-1)^{m-j} \binom{m}{j}\, j^a$$

Substituting this into the formula for $c_m$:

$$c_m = \frac{1}{m!}\sum_{j=0}^{m}(-1)^{m-j}\binom{m}{j}\, j^a$$

Substituting back into our original assumption gives the closed form:

$$k^a = \sum_{m=0}^a c_m\, k^{\underline{m}}$$

From here it is straightforward to derive Faulhaber's formula. Swapping the order of summation:

$$\sum_{k=1}^n k^a = \sum_{m=0}^a c_m \sum_{k=1}^n k^{\underline{m}}$$

Since the antidifference of $k^{\underline{m}}$ is $\dfrac{k^{\underline{m+1}}}{m+1}$, we have

$$\sum_{k=1}^{n} k^{\underline{m}} = \frac{(n+1)^{\underline{m+1}}}{m+1} - \frac{1^{\underline{m+1}}}{m+1} = \frac{(n+1)^{\underline{m+1}}}{m+1}$$

where the last equality uses $1^{\underline{r}} = 0$ for $r > 1$. Substituting in gives the final result:

$$\sum_{k=1}^n k^a = \sum_{m=0}^a c_m\, \frac{(n+1)^{\underline{m+1}}}{m+1}$$

where $c_m = \dfrac{1}{m!}\displaystyle\sum_{j=0}^{m}(-1)^{m-j}\binom{m}{j}\, j^a$.
