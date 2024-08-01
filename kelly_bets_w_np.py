import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from time import time

TS = time()
STARTING_MONEY = 100
WIN_PERCENT = 75
NUM_BETS = 100
NUM_ROUNDS = 100
results = [0 for x in range(100)]
# Set a seed so folks can duplicate my results
rng = np.random.default_rng(1701)
for cur_round in range(1, NUM_ROUNDS+1):
    # get wins for this series of bets
    wins = (np.random.randint(0, 100, size=NUM_BETS) < \
        WIN_PERCENT).astype(int)
    wins[wins == 0] = -1
    for bet_percent in range(1,101):
        bp = bet_percent/100
        money = STARTING_MONEY
        for y in range(NUM_BETS):
            money += round(money * wins[y] * bp)
        results[bet_percent - 1] += (money - results[bet_percent - 1]) \
            / cur_round
TF = time()

data = pd.DataFrame(results, columns=['Total Money'])
data.index += 1
sns.set()
g = sns.scatterplot(data=data)
g.set(yscale='symlog') # not log or zeros will not show
plt.show()
print("Took", (TF-TS), "seconds")
