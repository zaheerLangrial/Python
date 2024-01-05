
# Re-naming a Module
# import Mudel1 
import Mudel1 as mx
import platform
from Mudel1 import mul


# print(Mudel1.sum(11, 11))


# print (Mudel1.greeting('Zaheer'))


# print(Mudel1.person1)


print(mx.sum(11, 11))


print (mx.greeting('Zaheer'))


print(mx.person1)

print(mul(33 , 3))


#           Built-in Modules

# x = platform.system()
x = dir(platform)
# print(x)