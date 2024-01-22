# Looping Over globals
# What happens if you run this code? RuntimeError: dictionary changed size during iteration.
#
# for name in globals():
#     print(name)

# What happens if you run this code instead? Show the key of global().
#
# name = None
# for name in globals():
#     print(name)
# Why are the two different? the first code attempt to modify the dictionary while iteration, the second code the variable 'name' is defined at first and is reassigned each iteration
