# საშინაო დავალება 4
# სავალდებულო


#1
# ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია
# საკუთარი სახელის, გვარის და ასაკის შესახებ. თითოეული
# მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში.
# შემდეგ კი სამივე სია დაამატე საერთო ცალრიელ სიას
# სახელად consumer_info. Input_ის მეშვეობით მომხმარებლის
# ინდექსის შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს
# არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21
#


# consumer_info = []
#
# for i in range(3):
#     name = str(input("შეიყვანეთ სახელი: "))
#     lastname = str(input("შეიყვანეთ გვარი: "))
#     age = int(input("შეიყვანეთ ასაკი: "))
#
#     person_info = [name, lastname, age]
#     consumer_info.append(person_info)
#
# print(consumer_info)
#
# result = int(input("მოძებნეთ მომხმარებელი ინდექსის მიხედვით (1-3) : "))
# if 1 <= result <= 3:
#     print("სახელი:", consumer_info[result - 1][0])
#     print("გვარი:", consumer_info[result - 1][1])
#     print("ასაკი:", consumer_info[result - 1][2])
# else:
#     print("თქვენ შეიყვანეთ არასწორი მონაცემი")





# 2
# შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული
# ცნობილი მსახიობების შესახებ ინფორმაცია. მომხმარებელს
# შემოჰყავს მსახიობის სახელი ან გვარი. თუ სიაში მოიძებნა
# მსახიობი, დაბეჭდe მის შესახებ არსებული ინფორმაცია
# რეზუმის სახით.


# sia = [
#        ["Anya Taylor-Joy", "28", "Beth Harmon"],
#        ["Zendaya", "27", "Ruby Bennett “Rue”"],
#        ["Rosamund Pike", "45", "Amy Dune"],
#        ["Scarlett Johansson", "40", "Black Widow"],
#        ["Cate Blanchett", "55", "Elizabeth"],
#        ["Sarah Paulson", "49", "Lana Winters"]
# ]
#
# name = str(input("შეიყვანეთ მსახიობის სახელი და გვარი: "))
# found = False
#
# for actor in sia:
#        if name in actor[0].lower():
#               print("\nმსახიობი მოიძებნა სიაში.")
#               print("სახელი და გვარი:", actor[0])
#               print("ასაკი:", actor[1])
#               print("ცნობილი როლი:", actor[2])
#               found = True
#               break
#
# if not found == True:
#        print("მსახიობი სიაში არ მოიძებნა.")



# 3
# შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს
# ასევე სიას, თუმცა უნიკალური ელემენტებით
# (გამოიყენე set მონაცემთა ტიპი).
# def unique_list():
# ...
# return ...


# def unique_list(set_input):
#     first_set = set(set_input.split())
#     return first_set
#
# x = input("შეიყვანეთ ელემენტები: ")
#
# result = unique_list(x)
# print("სია უნიკალური ელემენტებით:", result)




# 4
# შექმენი ფუნქცია რომელიც მიიღებს ორ set
# ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ
# კი გადააქცევს tuple ტიპის მონაცემად და
# დააბრუნებს შედეგს.
# def set_to_tuple():
# ...
# return ...
#

# def set_to_tuple(set1, set2):
#     set_combined = set1.union(set2)
#     print("set: ", set_combined)
#     tuple_combined = tuple(set_combined)
#     print("tuple: ", tuple_combined)
#
#     return tuple_combined
#
#
# x_input = input("Enter elements for set x : ")
# x = set(x_input.split())
#
# y_input = input("Enter elements for set y : ")
# y = set(y_input.split())
#
# print(x)
# print(y)
#
# set_to_tuple(x, y)




# 5
# დაწერე პროგრამა, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.


# while True:
#     key = input("enter key value: ")
#     item = input("enter item value: ")
#     dict = {key : item}
#
#
#     if key == "" and item == "":
#         print("Dictionary is empty")
#         break
#
#     else:
#         print(dict)
#         print("Dictionary is not empty")
#         break



# 6
# დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს ოდენობა.
# მაგალითად პროგრამას გადავეცით სტრიქონი: 'w3schools'
# უნდა დააბრუნოს ლექსიკონი:
#
# {'w': 1, '3': 1, ‘s': 2, ‘c': 1, ‘h': 1, 'o': 2, ‘l': 1}
#

# def string_to_dict(string):
#     dict = {}
#     for i in string:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return dict
#
# print(string_to_dict(input("შეიყვანეთ მონაცემი: ")))



