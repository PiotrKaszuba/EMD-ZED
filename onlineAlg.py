import numpy as np
#bid, ctr, budget, spent
M = np.array([
    [1, 0.1, 1000, 100],
    [2, 0.08, 2000, 1000],
    [3, 0.04, 1000, 500]
]).astype(np.float64)


print("BALANCE")
for i in range(len(M)):
    print(M[i,2] - M[i,3])

print("GENERALIZED BALANCE")
for i in range(len(M)):
    val = M[i,0] * (1- np.e ** ( -(1  - (M[i,3]/M[i,2])  )  )  )
    print(val)

print("RO!")
for i in range(len(M)):
    val = M[i,0] * M[i,1]
    print(val)
