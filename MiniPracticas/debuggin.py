############DEBUGGING#####################

# Describe Problem
# def my_function(): 
#   for i in range(1, 21): #Range solo agarra hasta uno menos que el parametro final
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 5) #Inclute BOTH END POINTS, ambos parametros 
# print(dice_imgs[dice_num])


# # Fix the Errors #cuiado con la sintaxis y tener encueta Fstrins e identacion 
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print (word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])