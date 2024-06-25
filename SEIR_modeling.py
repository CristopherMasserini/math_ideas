"""
Modeling the SEIR model for infections disease

S'=−𝛽𝐼𝑁𝑆
E'=𝛽𝐼𝑁𝑆−𝜎𝐸
I'=𝜎𝐸−𝛾𝐼
R'=𝛾𝐼

Moves to (when s=S/N, e=E/N, ...)

s'=−𝛽is
e'=𝛽is−𝜎e
i'=𝜎e−𝛾i
r'=𝛾i
"""


def s_step(s_0, i_0, beta):
    # s_i=−𝛽is
    step = -beta * i_0 * s_0
    return step


def e_step(e_0, s_0, i_0, beta, sigma):
    # e_i=𝛽is−𝜎e
    step = (beta * i_0 * s_0) - (sigma * e_0)
    return step


def i_step(i_0, e_0, sigma, gamma):
    # i_i=𝜎e−𝛾i
    step = (sigma * e_0) - (gamma * i_0)
    return step


def r_step(i_0, gamma):
    # r_i=𝛾i
    step = gamma * i_0
    return step


def step_all(iterations):
    # Init conditions
    s_0 = 0.99
    e_0 = 0.01
    i_0 = 0
    r_0 = 0

    beta = 1
    sigma = 1
    gamma = 0.1

    for _ in range(0, iterations):
        s_n = s_0 + s_step(s_0, i_0, beta)
        e_n = e_0 + e_step(e_0, s_0, i_0, beta, sigma)
        i_n = i_0 + i_step(i_0, e_0, sigma, gamma)
        r_n = r_0 + r_step(i_0, gamma)

        print(s_n, e_n, i_n, r_n)

        s_0, e_0, i_0, r_0 = s_n, e_n, i_n, r_n

    
    # return s_0, e_0, i_0, r_0

step_all(10)
