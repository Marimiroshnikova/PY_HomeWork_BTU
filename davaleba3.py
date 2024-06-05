# import math

# დავალება 3
#
# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
# და დაბეჭდავს შემდეგნაირად:
# input: “word”
# Output: „Tripled: wordwordword“


# def func():
#     x = input("sheiyvanet nebismieri sityva: ")
#     x3 = x * 3
#     print("Tripled:", x3)
#
# func()



# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)


# def gravity():
#     while True:
#         weight_on_earth = float(input("sheiyvanet tqveni wona: "))
#         if weight_on_earth > 0:
#             weight_on_moon = round((weight_on_earth / 6), 2)
#             print(f"tqveni wona mtvareze iqneboda: {weight_on_moon} kg")
#             return weight_on_earth
#         else:
#             print("tqven sheiyvanet araswori monacemi.\n"
#                   "scadet tavidan")
#
# gravity()




# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
# მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
# მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“ დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის
# მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი
# მესიჯი. ასევე ნულზე გაყოფა არ შეიძლება, ამ შემთხვევაშიც უნდა დააბრუნოს
# შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)


# def calculator():
#     while True:
#         num1 = float(input("sheiyvane pirveli ricxvi: "))
#         operation = input("sheiyvane mocemuli otxi moqmedebidan ert-erti (+ - * / ^): ")
#         num2 = float(input("sheiyvane meore ricxvi: "))
#
#         if operation == "+":
#             result = num1 + num2
#         elif operation == "-":
#             result = num1 - num2
#         elif operation == "*":
#             result = num1 * num2
#         elif operation == "^":
#             result = num1 ** num2
#         elif operation == "/":
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 result = print("0-ze gayofa ar sheidzleba")
#                 return result
#         else:
#             print("tqven sheiyvanet araswori monacemi.\nscadet tavidan")
#             continue
#
#         print(f"{num1} {operation} {num2} = {result}")
#         return result
#
# calculator()

