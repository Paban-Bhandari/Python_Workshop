#This is how we define set
set_item = {"Apple","Mango","Orange","Cherry","Watermelon","Apple"}
print(set_item)

status = 1
if status:
    print("True Value")
else:
    print("False Value")

print(type(set_item))

set_variable = set(("Apple","Mango","Orange","Watermelon"))
print(set_variable)
set_variable.remove("Apple")
print(set_variable)
set_variable.add("Cherry")
print(set_variable)
set_variable.pop()
print(set_variable)
copy_variable = set_variable.copy()
print(copy_variable)