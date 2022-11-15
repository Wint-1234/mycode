#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

new_list = ["hello", "how", "are", "you", "?"]

#Insert my name to new_list
new_list.insert(1, "Winton")
print(new_list)

#Remove "?"
new_list.remove("?")

#Pop "you" and print it
print(new_list.pop())

