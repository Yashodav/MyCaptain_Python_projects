str = "mississippi"

dict = {}

for i in str:
    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1

    myKeys = list(dict.keys())
    myKeys.sort(reverse = True)
    sorted_dict = {i: dict[i] for i in myKeys}

print (sorted_dict)