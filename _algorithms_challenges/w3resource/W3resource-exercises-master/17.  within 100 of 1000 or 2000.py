def near1000(n):
    return ((abs(1000 - n) <= 100 or (abs(2000 - n) <= 100)))
print(near1000(1100))
print(near1000(900))
print(near1000(899))
print(near1000(1101))
print(near1000(1900))
print(near1000(2100))
print(near1000(2101))
print(near1000(1899))