import numpy as np
from pprint import  pprint
from scipy.spatial.distance import cosine
M = np.array([
    [1, 0,1,0,1,0,1,0,0],
    [1,0,0,0,1,1,1,1,0],
    [0,0,0,0,1,1,1,0,1],
    [1,1,0,1,1,0,0,0,1]

]).astype(np.float64)

query = [0,0,0,0,0,1,1,0,0]


print("COSINE SIMILARITY TO QUERY TF")
for i in range(len(M)):
    print(1-cosine(query, M[i]))

N = len(M)
n = np.count_nonzero(M, axis=0)
#print(N/n)
idf = np.log(N/n)
#print(idf)

tfidf = M*idf
print("TF IDF MATRIX")
pprint(tfidf)

querytfidf = query * idf
print("QUERY TF IDF")
print(querytfidf)
print("TFIDF SIMILARITY TO QUERY")

for i in range(len(M)):
    print(1-cosine(querytfidf, tfidf[i]))