# The commented code is mine, not sure why it is failing for few test cases.
# And not sure how the below code works, needs more debugging.
'''
from collections import Counter, OrderedDict
input_string = input()
_counter = Counter(input_string)
most_common_items = _counter.most_common()[:3]
el_dict = OrderedDict()
for el in most_common_items:
    if el[1] not in el_dict.keys():
        el_dict[el[1]] = []
        el_dict[el[1]].append(el[0])
    else:
        el_dict[el[1]].append(el[0])
        el_dict[el[1]] = sorted(el_dict[el[1]])
for k,v in el_dict.items():
    if len(v) > 1:
        for el in v:
            print(el,k)
    else:
        print(*v,k)
'''
from collections import Counter

chars = Counter(input()).items()

for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)