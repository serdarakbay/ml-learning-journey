import numpy as np

notlar = np.array([75, 88, 92, 61, 45, 78, 95, 55, 83, 70])
print(np.mean(notlar))
print(np.max(notlar))
print(np.min(notlar))
a=(notlar[notlar>60])
print(a)
print(a.size)
print(notlar/10)
