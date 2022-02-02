from chemdesc import ShinglesVectDesc

s = ShinglesVectDesc(external_desc_id_dict={"C": 0})

s = ShinglesVectDesc(external_desc_id_dict="dict.json")

print(s.fit_transform(["CNF"]))