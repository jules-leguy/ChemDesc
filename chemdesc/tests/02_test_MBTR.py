from chemdesc import MBTRDesc

s = MBTRDesc(MM_program="rdkit_uff")

desc, success = s.fit_transform(["O=O"])
print(desc)
print(desc.sum())
print(success)