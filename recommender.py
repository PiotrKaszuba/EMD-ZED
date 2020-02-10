import numpy as np
from scipy.stats import pearsonr
from fractions import Fraction
## PRODUCTS vs USERS
M = np.array([
    [4, 4, 4, 1, 1],
    [3, 1, 0, 4, 0],
    [4, 2, 0, 2, 3],
    [0, 2, 3, 0, 1],
    [0, 0, 1, 4, 3],
    [1, 1, 0, 0, 2],
]).astype(np.float64)

user_ind = 0



users = M.T

avgs = np.sum(users, -1) / np.count_nonzero(users, -1)
users = np.where(users == 0, 0, users-np.stack([avgs]*np.shape(users)[1], axis=1))

print("NORMALIZED USERS vs PRODUCTS")
print(users)
user = users[user_ind]
pearsons = []
print("USERS IND, CORRELATION /newline USERS IND, FRACTION CORRELATION FORM")
for i in range(len(M.T)):
    pearsons.append( pearsonr(user, users[i])[0] if i != user_ind else -1)
    print("i: " + str(i) + ", " + str(pearsonr(user, users[i])[0]))
    print("i: " + str(i) + ", " + str( Fraction(pearsonr(user, users[i])[0]).limit_denominator()))




howmanyNeighbours = 2
# FILL MARKS FROM TOP k neighbours
marks = np.array([2,3]).astype(np.float64)

sorted = np.array(list(reversed(np.sort(pearsons)))).astype(np.float64)
#print(sorted)
weights = sorted[:howmanyNeighbours]

ans = np.sum(marks * weights)/np.sum(weights)
print("WEIGHTED SUM OF NEAREST NEIGHBOURS")
print(ans)