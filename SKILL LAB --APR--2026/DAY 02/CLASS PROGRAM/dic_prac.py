s={1,89,45,78,96,65,45,56}
print(s)
print(type(s))

t=set()
print(t)
print(type(t))

s.add(5)
print(s)
s.update([8,47,23])
print(s)

s.remove(45)
print(s)
s.discard(90)#removing a value if their otherwise it won't show any errorr
print(s)
s.pop()
print(s)

ns=s.copy()
print(ns)

s.clear()
print(s)

del s
print(s)