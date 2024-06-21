
# collectiondır sıralanabilir fakat değiştirilemez
# tuple uyg daha performanslı hale getirir sadece listeyi göstermek için kullanılır 


_list = [1,2,3]
_tuple = (1,"iki",True)
_tuple2 = (3,"dört",True)

print(type(_list))
print(type(_tuple))

print(_list[1])
print(_tuple[1])

print(len(_list))
print(len(_tuple))

_list[0]=5
# _tuple[0]=5 hatalı değiştirilemez

_list.append(3)
# _tuple.append(5)

print(_tuple.count('iki'))

print(_tuple + _tuple2)

_t = tuple([3,4,5])

print(type(_t))
print(_t)

print(_list)
print(_tuple)

# listeyi  tuple çevirebiliriz kodun daha güvenli olması için