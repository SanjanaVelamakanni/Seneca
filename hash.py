int_val = 4
str_val = 'python'
flt_val = 24.56

# Printing the hash values.
print("The integer hash value is : " + str(hash(int_val)))
print("The string hash value is : " + str(hash(str_val)))
print("The float hash value is : " + str(hash(flt_val)))

#hashing on tuples and lists
tuple_val = (1, 2, 3, 4, 5)
list_val = [1, 2, 3, 4, 5]

# Printing the hash values.
print("The tuple hash value is : " + str(hash(tuple_val)))

#raises error as lists are mutable
print("The list hash value is : " + str(hash(list_val)))