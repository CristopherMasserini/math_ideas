import matplotlib.pyplot as plt

num = 4
roundBy = 100

x = range(1, 500)
multiples = [(num * i) % roundBy for i in x]
roundDiff = []
roundDiffSum = []

for mult in multiples:
    if mult < (roundBy/2):
        roundDiff.append(-mult)
    else:
        roundDiff.append(roundBy - mult)


for i, rounded in enumerate(roundDiff):
    if i == 0:
        roundDiffSum.append(rounded)
    else:
        roundSum = roundDiffSum[i-1] + rounded
        roundDiffSum.append(roundSum)

print(x)
print(multiples)
print(roundDiff)
print(roundDiffSum)

# plt.plot(x, multiples)
plt.plot(x, roundDiff)
# plt.plot(x, roundDiffSum)
plt.show()



