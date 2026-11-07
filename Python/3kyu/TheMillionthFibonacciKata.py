


"""

Fast Doubling Formula:-------


*for even-numbers:
--------------------+--------------------
$$
F_{2n} = F_n(2F_{n+1}-F_n)
$$
--------------------+--------------------

*for odd-numbers: 
--------------------+--------------------
$$
F_{2n+1} = (F_n)^2+(F_{n+1})^2 
$$
--------------------+--------------------
example:

$$
\begin{aligned}
&5\ is\ an\ 'odd'\ number:\ then\\
&\boxed{F_{2n+1} = (F_n)^2+(F_{n+1})^2}\ ,where\ n=5 \\
&n=5 = 2*2+1 \\
&F_5 = F_2^2 + F_3^2 \\
& and\ we\ know\ that\ :\boxed{F_2 = 1},\ \boxed{F_3 = 2} \\
&F_5 = 1^2 + 2^2 \\
&    = 1+4 \\
&\boxed{F_5=5}
\end{aligned}
$$


"""


def fast_doubling(n: int):
    F = [0, 1] # value's container
    if n in F: return n



    if n >= 0:
        for i in range(2, n+1):
            F.append(F[i - 1] + F[i - 2])
        return F[-1]

    
    

    return F[-1]*(-1)


while True:
    inp = input("::>")
    # print(f"+{inp}= ",fast_doubling( int(inp) ))
    print(f"{inp}= ",fast_doubling( int(inp) ))