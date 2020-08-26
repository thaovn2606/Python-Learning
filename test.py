
# so nguyen (int): so ko co dau "."
# so thuc (float): tap hop so nguyen & phan so (co dau "."), chi in xap xi 10 so sau dau "."


a = 4
b = 1.123456789101112131415
c = "5"


print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

# cach ko bi gioi han 10 so

# lay toan bo noi dung cua decimal
from decimal import*

# lay toi da 30 chu so phan nguyen va phan thap phan decimal
getcontext().prec = 30

f = float(3)/float(8)
d = Decimal(100)/Decimal(3)

print(f)
print(d)

# https://stackoverflow.com/questions/3387655/safest-way-to-convert-float-to-integer-in-python














