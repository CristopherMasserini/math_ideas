import matplotlib.pyplot as plt

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
    step = beta * i_0 * s_0 - sigma * e_0
    return step


def i_step(i_0, e_0, sigma, gamma):
    # i_i=𝜎e−𝛾i
    step = sigma * e_0 - gamma * i_0
    return step


def i_step_SIR(i_0, s_0, beta, gamma):
    # i_i=𝜎e−𝛾i
    step = beta * i_0 * s_0 - gamma * i_0
    return step


def r_step(i_0, gamma):
    # r_i=𝛾i
    step = gamma * i_0
    return step


def step_all_SEIR(iterations):
    # Init conditions
    s_0 = 0.99
    e_0 = 0.01
    i_0 = 0
    r_0 = 0

    beta = 1
    sigma = 0.9
    gamma = 0.1

    s_all = [s_0]
    e_all = [e_0]
    i_all = [i_0]
    r_all = [r_0]

    for _ in range(0, iterations):
        s_n = s_0 + s_step(s_0, i_0, beta)
        e_n = e_0 + e_step(e_0, s_n, i_0, beta, sigma)
        i_n = i_0 + i_step(i_0, e_n, sigma, gamma)
        r_n = r_0 + r_step(i_n, gamma)

        s_all.append(s_n)
        e_all.append(e_n)
        i_all.append(i_n)
        r_all.append(r_n)

        s_0, e_0, i_0, r_0 = s_n, e_n, i_n, r_n

    return s_all, e_all, i_all, r_all


def step_all_SIR(iterations):
    # Init conditions
    s_0 = 0.99
    i_0 = 0.01
    r_0 = 0

    beta = 1
    gamma = 0.1

    s_all = [s_0]
    i_all = [i_0]
    r_all = [r_0]

    for _ in range(0, iterations):
        s_n = s_0 + s_step(s_0, i_0, beta)
        i_n = i_0 + i_step_SIR(i_0, s_0, beta, gamma)
        r_n = r_0 + r_step(i_n, gamma)

        s_all.append(s_n)
        i_all.append(i_n)
        r_all.append(r_n)

        print(s_n+i_n+r_n)
        s_0, i_0, r_0 = s_n, i_n, r_n

    return s_all, i_all, r_all


def plot_SEIR(iterations):
    t = list(range(0, iterations+1))
    s_all, e_all, i_all, r_all = step_all_SEIR(iterations)

    plt.plot(t, s_all, label="Susceptible")
    plt.plot(t, e_all, label="Exposed")
    plt.plot(t, i_all, label="Infected")
    plt.plot(t, r_all, label="Recovered")
    plt.legend()
    plt.show()


def plot_SIR(iterations):
    t = list(range(0, iterations+1))
    s_all, i_all, r_all = step_all_SIR(iterations)

    plt.plot(t, s_all, label="Susceptible")
    plt.plot(t, i_all, label="Infected")
    plt.plot(t, r_all, label="Recovered")
    plt.legend()
    plt.show()

plot_SIR(100)
