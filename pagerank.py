import numpy as np
from fractions import Fraction



M = np.array([
    [0, 1/2, 0, 0,  0],
    [1/2, 0, 0,  0,    0],
    [1/2,  1/2,    0, 0, 0],
    [0,   0, 1/2,   0, 1],
    [0,   0, 1/2, 1,   0],
]).astype(np.float64)

# init (only page rank) , topic specific intis itself!!
v = np.array([1,1,1,1,1]).astype(np.float64)


def pagerank():
    it1 = M@v
    print("ITERATION 1")
    print(it1)
    toPrint=[ Fraction(i).limit_denominator()  for i in it1]
    print("ITERATION 1, fraction form")
    print(toPrint)


def topicSpecific(tax, topicIndices):
    # tax_income = np.zeros_like(v).astype(np.float64)
    # inc_val = tax * np.sum(v) / len(topicIndices)
    # tax_income[topicIndices] = inc_val
    # it1 = (1-tax) * (M@v) + tax_income

    vt = np.zeros_like(v).astype(np.float64)
    vt[topicIndices] = tax/len(topicIndices)
    tax_income = np.array(vt)
    it1 = (1-tax) * (M@vt) + tax_income
    it2 = (1-tax) * (M@it1) + tax_income
    print("ITERATION 1")
    print(it1)
    toPrint = [Fraction(i).limit_denominator() for i in it1]
    print("ITERATION 1, fraction form")
    print(toPrint)
    print("ITERATION 2")
    print(it2)
    toPrint = [Fraction(i).limit_denominator() for i in it2]
    print("ITERATION 2, fraction form")
    print(toPrint)

#pagerank()
topicSpecific(tax = 0.2, topicIndices=[0,1])



# M = np.array([
#     [0, 1/2, 1, 1/5,  0,    0],
#     [0,   0, 0, 1/5,  0,    0],
#     [0, 1/2, 0, 1/5, 1/3,   0],
#     [0,  0, 0,    0, 1/3, 1/2],
#     [0,   0, 0, 1/5,   0, 1/2],
#     [0,   0, 0, 1/5, 1/3,   0],
# ]).astype(np.float64)




