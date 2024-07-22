#dictianory:
user_info = {
    'modal':'2000',
    'color':'black',
    'make_modal':'2007'
}

print(user_info)

# for i,j in user_info.items():
#     print(i, j)

# print("What do you want to insert")
# value_name = input("Enter type of car like sport, city, four-wheel: ")
# user_info.update(
#     {
#         'type': value_name
#     }
# )
# print(user_info)

for i in range(10):
    print("What do you want to insert")
    key_name = input("Enter the key_name you want to add: ")
    value_name = input("Enter the value for above key: ")
    user_info.update(
        {
            key_name : value_name
        }
    )
    print(user_info)

# #To update the dictionary:
# user_info.update({
#     'price':'$20000'
# })

#print(user_info.keys()) #print keys
#print(user_info.values()) #print values
# print(user_info['price'])
# print(len(user_info))

# #To get specific key value:
# modal = user_info.get('modal')
# print(modal)