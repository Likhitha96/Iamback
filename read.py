from sklearn.neighbors import NearestNeighbors
import csv
import numpy as np

data = []
fileread = open('test.csv', 'rU')
readcsv = csv.reader(fileread, delimiter=',')
L = list(readcsv)
L=L[1:]
L=[i[1:] for i in L]
L = np.array(L)
L = np.transpose(L)
print L
nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(L)
distances, indices = nbrs.kneighbors(L)
print indices
