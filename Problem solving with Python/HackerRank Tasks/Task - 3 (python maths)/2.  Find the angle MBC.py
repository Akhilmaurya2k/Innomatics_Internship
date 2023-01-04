import math
AB = int(input())
BC = int(input())
#sep=''
print(round(math.degrees(math.atan(AB/BC))), chr(176), sep='')
