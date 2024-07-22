## string operation

# ####################################
# string_name = "This is string it's"
# print(string_name)
# print(len(string_name))
# #####################################

# ##################
# p = 'Hello world'
# print(p[0])
# for i in p:
#     print(i)
###################

# ############################################
# email = input('Enter your email: ')
# if '@' not in email:
#     print("Email not valid.")
# else:
#     print("Email validated sucessfully.")
# ############################################

# #######################################
# example= "Favourite fruit is mango"
# if 'mango' in example:
#     print("yes, mango is favourite")

# #slicing
# print(example[2:8])  
# print(example[-5:-1])
# print(example[:10])
# print(example[2:])
# #######################################

# #######################################################
# #Modifying the string
# sentence = "The World is Beautiful so lets be HAPPY"

# #To make all elements inside string into lowercase:
# print(sentence.lower())

# #To make all elements inside string into uppercase:
# print(sentence.upper())
# #######################################################

# #######################################################################
# #removing whitespace from the string
# #whitespace means unwwanted space in the sentence
# new_sentence = "         Texas college of Management and IT"
# print(new_sentence.strip())
# #to replace anything character and a word from a string we use replace
# print(new_sentence.replace('college','school'))
# print(new_sentence.strip().replace('college','school'))#both
# print(len(new_sentence))
# ########################################################$###############

# #######################################################################
# #spliting the string:
# split_name = "Paban!Bhandari"
# print(split_name.split('!'))
# print(type(split_name.split('!')))
# #string concatination(joining the string)
# first_name = "Paban"
# last_name = "Bhandari"
# concate_name = first_name +' '+ last_name
# print(concate_name)
# print(first_name+" "+last_name)
# #######################################################################

# #############################################################################
# #sum
# def sum(a,b):
#     sum = a + b
#     return sum
# sum_amt = sum(10, 20)
# print(sum_amt)
# #there is 2 way to format string and variables:
# print("The sum of 10 and 20 is", sum_amt)
# print("The sum of 10 and 20 is " + str(sum_amt))
# print(f"The sum of 10 and 20 is {sum_amt}")
# print(f"{sum_amt} is the total sum")
# #difference
# def min(a,b):
#     min = a - b
#     return min
# difference = min(90, 20)
# print("The difference between 90 and 20 is", difference)

# print(f"{4*10} is the multiple value of 4 and 10.")
# #############################################################################

########################################################################
print("laxmi Parsad Devkota wrote \"Muna Madan\"")
########################################################################