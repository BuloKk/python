w = 'bulok'
a = 1
s = 2.3
b = bytes(123)
f = [1, 2.3, 'cat', w]
g = ('qqq', 45, s, f)
h = {'qqqq', 'fff', 'eee', 'www', 'www'}
j = frozenset({'zzz', 'dddd', 'ggg', 'bbb'})
k={'mck' : 495, 'spb' : 812, 'rzn' : 912}

print(w, '=', type(w), '\n',
      s, '=', type(s), '\n',
      f, '=', type(f), '\n',
      g, '=', type(g), '\n',
      h, '=', type(h), '\n',
      j, '=', type(j), '\n',
      k, '=', type(k), '\n')
# print(a, '=', type(a))
# print(s, '=', type(s))
# print(f, '=', type(f))
# print(g, '=', type(g))
# print(h, '=', type(h))
# print(j, '=', type(j))
# print(k, '=', type(k))
z = 'cat'
print(w, z)
print(w, a)
print(w +' '+ str(a))

