"""def add(a, b):
    return a + b
print (add(1,2))

# with Lambda
add = lambda x, y : x + y

print ( add(3,4))
"""

my_list = [1,2,3,4,5,6,7]

new_list = list(map(lambda x : x * 2, my_list))

print (new_list)
#combine first and last name to single "full name"
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
full_name("sasd", "shandj")
print(str(full_name))
