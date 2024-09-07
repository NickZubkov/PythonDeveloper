my_dict = {"Nick" : 1987, "Alex" : 1995, "Elena" : 1990}
print(my_dict)
print(my_dict["Nick"])
print(my_dict.get("Ben"))
my_dict.update({"Ben" : 2000,
                "Mike" : 2005})
print(my_dict.pop("Nick"))
print(my_dict)

my_set = {1, 1, 1, 2, 3, 3, 4, True, True, False, "Nick", "Nick", "Ben"}
print(my_set)
my_set.add("Elena")
my_set.add(5.5)
print(my_set)
my_set.remove(5.5)
print(my_set)