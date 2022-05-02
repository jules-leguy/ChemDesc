import numpy as np

from chemdesc import RandomGaussianVectorDesc, ShinglesVectDesc

desc = RandomGaussianVectorDesc(vect_size=100000)
# desc = ShinglesVectDesc(vect_size=30)

# print("desc : " + str(desc.fit_transform(["C", "C", "CN", "NC", "CF"])))

desc_list = desc.fit_transform(["C", "C", "CN", "NC", "CF"])[0]

l = [np.mean(desc_list[i]) for i in range(len(desc_list))]
print(l)

l = [np.std(desc_list[i]) for i in range(len(desc_list))]
print(l)