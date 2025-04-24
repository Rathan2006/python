import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.apply(lambda x: x.upper() if pd.notnull(x) else "")
print("Upper case:\n", upper_case)

lower_case = s.apply(lambda x: x.lower() if pd.notnull(x) else "")
print("\nLower case:\n", lower_case)

string_length = s.apply(lambda x: len(x) if pd.notnull(x) else "")
print("\nLength of each string:\n", string_length)
