'''day cung dc xai cho comment hay con goi la docs string'''

# nhay don
''

# nhay kep
""

# chuoi cung dc nam trg 2 cap nay
''' '''
""" """

strThao = 'Nguyen Thanh Thao'
print(strThao)

strLinh = "Dang Le My Linh"
print(strLinh)

# phan biet '' & ""
# a = 'I'm Beginer' => sai vi he thong hieu lam ''
# edit (neu ben trg chuoi co dau '' thi dung "" de tao chuoi hoac nguoc lai)
a = "I'm Beginner"
print(a)

b = 'I"m Beginner 2'
print(b)

# chuoi nhieu dong ('' hay "" nhu nhau)
c = '''Thao sieudeptrai
Thong minh
Tai nang'''
print(c)

# cach khac: dung \n
d = '''Thao sieudeptrai\nThong minh\nTai nang'''
print(d)

# mot so chuoi voi \

# se phat ra 1 tieng beep
print('\a')
# se mat chu 'd'
print('abcd\be')
# xuong dong
print('dong 1\ndong 2')
# tab
print('dong 1\tdong 2')
# fix ' trg chuoi
print('I\'m Beginner')
# hien thi dau \
print('Day la dau \\')

# BAI TAP: trg chuoi vua co dau ' va " thi code lam sao?
bt = 'Tao dc goi la "Thao sieudeptrai" va \'thongthai\''
print(bt)






# CAU HOI CUNG CO
# 1/ Nhung chuoi nao sau day hop le?
# ‘nasdfiuqwnerp’, “234a’adadf”, “””asd34’asdfjoaisdfadf””””, “\”, “””\”””, ‘’
# 2/ Su khac nhau giua 2 bien a va b duoi day la gi?
# >>> a = 69
# >>> b = '69'
# 3/ Chi ra cac Escape Sequence trg nhung gia tri sau day:
# Chuoi 1: '35\53ni34'
# Chuoi 2: '\\n'
# Chuoi 3: “\/\/\/\\/\/”


# TRA LOI
# 1/ 'nasdfiuqwnerp', “234a’adadf”, ''
print("234a'adadf")
print('')
# 2/ a la int, b la str
a, b = 69, '69'
print(type(a))
print(type(b))
# 3/ \5, \, \\
print('35\53ni34')
print('\\n')
print("\/\/\/\\/\/")
