x = input()

result = list()

for i in range(len(x)):
    if x[i].isupper():
        result.append(x[i].lower())
    else:
        result.append(x[i].upper())
        
print(''.join(result))