classes = [(11,12), (9,10), (9.5,10.5), (10,11), (10.5,11.5)]
final_list = []
last_time = 0
classes = sorted(classes, key=lambda t: t[1])

for class_time in classes:
    if last_time <= class_time[0]:
        final_list.append(class_time)
        last_time = class_time[1]

print(final_list)