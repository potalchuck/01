my_dict={"Daniel":2003,"Irina":1982, 'Masha': 2002}
print(my_dict)
print(my_dict.get("Irina"))
print(my_dict.get("Kamila"))
my_dict.update({"Sasha":2006,"Alex":1993})
a=my_dict.pop("Masha")
print(my_dict)
print(a)
my_set={1,2,3,4,"Oleg",True,1,2,3,4,}
print(my_set)
my_set.update({5,6})
print(my_set)
print(my_set.discard("Oleg"))
print(my_set)