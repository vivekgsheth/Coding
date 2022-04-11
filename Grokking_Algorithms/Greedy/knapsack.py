from collections import OrderedDict

w = [30,20,15]
v = [3000,2000,1500]

item_dict = {}
for i in range(len(v)):
    item_dict[v[i]] = w[i]

print(item_dict)
final_list = []

capacity = 35
total_weight = 0
total_value = 0

sorted_dict = OrderedDict(sorted(item_dict.items(), key=lambda t: t[0], reverse=True))


for val,wt in sorted_dict.items():
    if wt+total_weight < capacity:
        print(val,wt,total_weight)
        total_weight += wt
        total_value += val
        final_list.append(val)
    else:
        continue
    
print(final_list)
