import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

ratings = np.array([
    [5, 4, 0, 0],
    [4, 5, 0, 0],
    [0, 0, 5, 4],
    [0, 0, 4, 5]
])

similarity = cosine_similarity(ratings)

user = 0
similar_users = similarity[user].argsort()[::-1][1]

recommendations = np.where(
    ratings[similar_users] > 0
)[0]

for item in recommendations:
    if ratings[user][item] == 0:
        print("Recommended Item:", item + 1)
