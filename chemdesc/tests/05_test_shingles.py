from chemdesc import ShinglesVectDesc

d = ShinglesVectDesc(vect_size=2, count=True)
print("desc : " + str(d.fit_transform(["C", "C", "CN", "NC", "CF"])))
