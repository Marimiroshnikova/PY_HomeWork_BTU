
# #1
# # დაწერე პროგრამა, რომელიც მოსთხოვს მომხმარებელს
# # სახელის შეყვანას (ლათინური ასოებით).
# # თუ სახელი იქნება "Bond"-ი, გამოიტანეთ წარწერა
# # "Welcome on board 007!".
# # სხვა შემთხვევაში გამოიტანეთ წარწერა "Good morning Name".
# # (Name-ის ადგილზე ჩასვით მომხმარებლის სახელი)
# # იგივე კოდი მუშაობდეს "bond"-ზეც.
#
# a = input("sheiyvanet momxmareblis saxeli: ").lower()
# if a == "Bond":
#     print("Welcome on board 007!")
# else:
#     print(f"Good morning {a}")


# #2
# # პროგრამა სთხოვს მომხმარებლებს წლოვანებას (მთელი რიცხვი)
# # და გამოაქვს მესიჯი, შეუძლია თუ არა მას არჩევნებში მონაწილეობის
# # მიღება (18 წლის ან ზემოთ)
#
#
# age = int(input("gtxovt sheiyvanet tqveni asaki: "))
# if age >= 18:
#     print("gilocavt, tqven shegidzliat monawileoba miigot archevnebshi!")
# elif age > 0 and age < 18:
#     print("samwuxarod, tqven ar shegidzliat archevnebshi monawileobis migeba")
# else:
#     print("tqven sheiyvanet araswori monacemi. scadet tavidan")


# # 3
# # მომხმარებელს პროგრამა სთხოვს ორი რიცხვის შეყვანას
# # და აბრუნებს მათ შორის უმცირესს.
#
# a = float(input("gtxovt sheiyvanet pirveli ricxvi: "))
# b = float(input("gtxovt sheiyvanot meore ricxvi: "))
#
# if a > b:
#     print(f"\nmeore ricxvi {b} aris umciresi\n"
#           f"{b} < {a}")
# elif b > a:
#     print(f"\npirveli ricxvi {a} aris umciresi\n"
#           f"{a} < {b}")
# elif a == b:
#     print(f"\npirveli ricxvi {a} da meore ricxvi {b} aris toli\n"
#           f"{b} = {a}")


# # 4
# # პროგრამა მომხმარებელს სთხოვს, შეიყვანოს სამი მთელი რიცხვი
# #  და ბეჭდავს მოცემულ რიცხვებს შორის უდიდესს.
#
# a = int(input("gtxovt sheiyvanet pirveli ricxvi: "))
# b = int(input("gtxovt sheiyvanot meore ricxvi: "))
# c = int(input("gtxovt sheiyvanot mesame ricxvi: "))
#
# if a >= b and a >= c:
#     print(f"\n{a} aris udidesi")
# elif b >= a and b >= c:
#     print(f"\n{b} aris udidesi")
# elif c >= b and c >= a:
#     print(f"\n{c} aris udidesi\n")


# # 5
# # პროგრამა სთხოვს მომხმარებელს რიცხვის შეყვანას,
# # ამოწმებს პოზიტიურია რიცხვი თუ ნეგატიური და
# # აბრუნებს შესაბამის პასუხს.
#
# x = float(input("sheiyvanet ricxvi: "))
#
# if x > 0:
#     print(f"mocemuli ricxvi {x}, aris dadebiti")
# elif x < 0:
#     print(f"mocemuli ricxvi {x}, aris uaryofiti")
# else:
#     print(f"mocemuli ricxvi aris nulis toli. arc dadebitia arc uaryofiti.")


# # 6
# # პროგრამა სთხოვს მომხმარებელს შეიყვანოს მთელი რიცხვი
# # და ამოწმებს იყოფა თუ არა შეყვანილი რიცხვი 2-ზე და 3-ზე.
# # შემდეგ ბეჭდავს შესაბამის მესიჯს.
#
# a = int(input("sheiyvanet mteli ricxvi: "))
#
# if a % 2 == 0 and a % 3 == 0:
#     print(f"mocemuli ricxvi {a}, iyofa 2-ze da 3-ze")
# elif a % 2 != 0 and a % 3 != 0:
#     print(f"mocemuli ricxvi {a}, ar iyofa arc 2-ze da arc 3-ze")
# elif a % 2 != 0 and a % 3 ==0:
#     print(f"mocemuli ricxvi {a}, ar iyofa 2-ze da iyofa 3-ze")
# elif a % 2 == 0 and a % 3 !=0:
#     print(f"mocemuli ricxvi {a}, iyofa 2-ze da ar iyofa 3-ze")


# # 7
# # მოითხოვე მომხმარებლისგან მთელი რიცხვი. დაბეჭდე True
# # თუ შეყვანილი რიცხვი ლუწია, ხოლო თ კენტია False.
#
# x = int(input("sheiyvanet nebismieri mteli ricxvi: "))
#
# if x > 0:
#     if x % 2 == 0:
#         print(True)
#     elif x % 2 == 1:
#         print(False)
# else:
#         print("mocemuli mteli ricxvi arc kentia da arc luwi.")


# # 8
# #  პროგრამა ითხოვს მომხმარებლისგან ქულის ოდენობას (მაქს 100) და ბეჭდავს:
# # A შეფასებას, თუ ქულა მეტია 90_ზე.
# # B შეფასებას, თუ ქულა მეტია 80_ზე და ნაკლებია ან ტოლია 90 ზე.
# # C შეფასებას, თუ ქულა მეტია ან ტოლია 60 ზე და ნაკლებია ან ტოლია 80 ზე.
# # D თუ ქულა ნაკლებია 60_ზე.
# # ფორმატი:
# # Grade: A
#
#
# score = float(input("sheiyvanet tqveni qula: "))
#
# if score >= 0 and score <= 100:
#     if score > 90:
#         print(f"{score} - grade: A")
#     elif score > 80 and score <= 90:
#         print(f"{score} - grade: B")
#     elif score >= 60 and score <= 80:
#         print(f"{score} - grade: C")
#     else:
#         print(f"{score} - grade: D")
# else:
#     print("tqven sheiyvanet araswori monacemi.\n"
#           "qula motavsebuli unda iyos 0-100 shualedshi")


# # 9. პროგრამა გთხოვს შეიყვანო მომხმარებელი და პაროლი
# # პლატფორმაზე დასარეგისტრირებლად. თუ პაროლში სიმბოლოების
# # ოდენობა 8 ზე ნაკლებია, არ დაარეგისტრიროს ახალი
# # მომხმარებელი და დააბრუნოს შესაბამისი მესიჯი.
# #
# # თუ რეგისტრაცია წარმატებით დასრულდა მომხმარებელს
# # მიეცეს ანგარიშში შესვლის საშუალება მონაცემების ხელმეორედ
# # სწორად შეყვანის შემთხვევაში. (დაიბეჭდოს მესიჯი
# # „ავტორიზაცია წარმატებით შესრულდა!")
# #
# # თუ შეყვანილი მონაცემები არ დაემთხვა რეგისტრაციის მონაცემებს,
# # გამოიტანოს შესაბამისი მესიჯი. („მომხმარებელი ან პაროლი
# # არ არის სწორად შეყვანილი!")
#
# name = input("gtxovt sheiyvanet momxmareblis saxeli: ")
# pas = input("gtxovt sheiyvanot momxmareblis paroli: ")
#
# if len(pas) < 8:
#     print("tqveni paroli sheicavs 8 simboloze naklebs.\n"
#           "tqven ver daregistrirdit. scadet tavidan.")
# else:
#     print("registracia warmatebit dasrulda")
#     name1 = input("sheiyvanet tqveni saxeli: ")
#     pas1 = input("tavidan sheiyvanet tqveni paroli: ")
#
#     if name1 == name and pas1 == pas:
#         print("avtorizacia warmatebit shesrulda.")
#     else:
#         print("momxmarebeli an paroli ar aris sworad sheyvanili.")


# # 10. პროგრამა ითხოვს შეიყვანო რიცხვი 1 დან 7_ის ჩათვლით
# # და გამოაქვს შესაბამისი კვირის დღის სახელი
# # (ორშაბათი, სამშაბათი... არასწორი ინფორმაციის შემთხვევაში
# # გამოაქვს მესიჯი: „შეიყვანე რიცხვი 1_დან 7_ის ჩათვლით!
#
# x = float(input("sheiyvane ricxvi (1-7) diapazonshi: "))
#
# if x >= 1 and x <= 7:
#     if x == 1:
#         print("orshabati")
#     elif x == 2:
#         print("samshabati")
#     elif x == 3:
#         print("otxshabati")
#     elif x == 4:
#         print("xutshabati")
#     elif x == 5:
#         print("paraskevi")
#     elif x == 6:
#         print("shabati")
#     elif x == 7:
#         print("kvira")
#     else:
#         print("sheiyvane mteli ricxvi 1-dan 7-mde")
# else:
#     print("araswori monacemi.\n"
#           "sheiyvane mteli ricxvi 1-dan 7-mde")


# # 11. პროგრამა სთხოვს მომხმარებელს მთელი რიცხვის შეყვანას
# # და ამოწმებს სამნიშნაა თუ არა შეყვანილი რიცხვი.

# x = int(input("sheiyvanet ricxvi: "))
#
# if abs(x // 100) in (1,2,3,4,5,6,7,8,9):
#     print(f"tqvens mier sheyvanili ricxvi {x} aris samnishna")
# else:
#     print(f"tqven mier sheyvanili ricxvi ar aris samnishna")


# # 12. პროგრამა ითხოვს ქვეყნის მოსახლეობის რაოდენობის შეყვანას.
# # შემდეგ ითხოვს ანტიდოტის ოდენობის შეყვანას.
# # თითო ადამიანზე 2 ანტიდოტია საჭირო.
# # თუ ზედმეტი ანტიდოტი გვაქვს ვბეჭდავთ მოკავშირე
# # ქვეყნისთვის დასახმარებლად გადასაცემ ანტიდოტების
# # რაოდენობას.
# # თუ დეფიციტი გვაქვს, ვბეჭდავთ რა ოდენობის ანტიდოტი
# # უნდა გამოვითხოვოთ მოკავშირე ქვეყნებისგან.
#
#
# n = int(input("sheiyvanet qveyanashi mosaxleobis raodenoba: "))
# a = int(input("sheiyvanet antidotebis raodenoba: "))
#
# if a >= 0 and n >= 0:
#     if a == 2 * n:
#         print("antidotebis raodenoba sakmarisia qveynis mosaxleobistvis.\n"
#               "damatebiti antidoti sxva qveynistvis agar rcheba")
#     elif a > 2 * n:
#         x = a - 2 * n
#         print(f"mokavshire qveyanas shegvidzlia gadavcet {x} antidoti.")
#     elif a < 2 * n:
#         y = 2 * n - a
#         print(f"mokavshire qveynebidan unda gamovitxovot {y} antidoti")
# else:
#     print("tqven sheiyvanet araswori monacemebi.\n"
#           "scadet tavidan.")


# # 13. პროგრამა სთხოვს მომხმარებელს შეიყვანოს მისი ხელზე ასაღები ხელფასის ოდენობა და წლების რაოდენობა.
# # პროგრამა აბრუნებს წლების მანძილზე მომხმარებლის მიერ ხელზე აღებულ და ქვეყნის ბიუჯეტში შესულ თანხას.
# # (საშემოსავლო გადასახადი 26%)
#
# x = float(input("sheiyvanet tqveni xelfasis raodenoba: "))
# y = int(input("sheiyvanet wlebis raodenoba: "))
#
# print(f"{y} welshi xelze asagebi xelfasi raodenoba: ", 0.74*x*y)
# print(f"{y} welshi sashemosavlos raodenoba: ", 0.26*x*y)


# # 14. პილოტი შტორმში მოხვდა და ვერ შეძლო აეროპორტში დროული დაშვება.
# # საწვავის რაოდენობა შეზღუდულია. პილოტს სჭირდება კომპიუტერის დახმარება.
# # შექმენი პროგრამა, რომელიც მოითხოვს პილოტისგან დარჩენილი
# # საწვავის რაოდენობას (ლიტრებში) და მიაწოდებს ინფორმაციას იმ ქალაქების
# # აეროპორტების შესახებ, რომლამდე მიღწევაც შესაძლებელია.
# # ზემოაღნიშნული თვითმფრინავი ხარჯავს 12 ლიტრ საავიაციო საწვავს
# # 1 კილომეტრის მანძილის დაფარვისას.
# # თვითმფრინავის ახლომდებარე სამი ქალაქია:
# # Zaragoza (50km) Valencia (75 km)
# # Madrid (100km)
# # თუ თვითმფრინავს არ ჰყოფნის საწვავი არცერთ ქალაქამდე.
# # დაბეჭდე მესიჯი: „ავარიული დაშვება!"
#
#
# n = float(input("sheiyvanet darchenili sawvavis raodenoba: "))
#
# if n >= 0:
#     if 100*12 <= n:
#         print("tqventan axlomdebare qalaqi sadac shegidzliat dajdet: \n"
#               "Madrid - 100km\n"
#               "Valencia - 75 km\n"
#               "Zaragoza - 50km")
#     elif 75*12 <= n:
#         print("tqventan axlomdebare qalaqi sadac shegidzliat dajdet: \n"
#               "Valencia - 75 km\n"
#               "Zaragoza - 50km")
#     elif 50*12 <= n:
#         print("tqventan axlomdebare qalaqi sadac shegidzliat dajdet: \n"
#               "Zaragoza - 50km")
#     else:
#         print("avariuli dashveba!")
# else:
#     print("araswori monacemi.\n"
#           "scadet tavidan.")
