from scipy.spatial import distance
p1 = (1, 2, 3)
p2 = (4, 5, 6)
d = distance.euclidean(p1, p2)
print("Euclidean distance: ",d)
