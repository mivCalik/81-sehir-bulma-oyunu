from turtle import *
import pandas as pd
import time

data = pd.read_csv("81-il.csv")
# print(data)
# data is an pd object
# we need to use [] to access values
sehir_data = dict(data)
sehir_list = list(sehir_data["sehir"])
print(sehir_list)



window = Screen()
window.title("Şehir bulmaca 🤔")
window.bgpic("tr-şehirleri.png")
window.setup(width=1000, height=600)

# #### with code below approximate x-y city coordinates are found
# def mouse_click_coor(x, y):
#     print(x, y)
#
# window.onscreenclick(fun=mouse_click_coor)

writer = Turtle()
writer.penup()
writer.seth(90)
writer.hideturtle()

writer.goto(-200, 220)
writer.write("Bakalım kaçını bileceksin...\nBitirmek için \"pes\" yazabilirsin",font=("Arial",24,"normal"),)


def print_city(name):
    city = data[data.sehir == name]
    x_cor = int(city.x)
    y_cor = int(city.y)
    writer.goto(x_cor, y_cor)
    writer.pencolor("DarkGreen")
    writer.write(name)
    time.sleep(0.2)
    if name in guessed_cities:
        writer.pencolor("Black")
    else:
        writer.pencolor("DarkRed")
    writer.write(name)


score = 0
header = "Şehirleri bul bakalım!"
guessed_cities = []
missed_cities = []
user_input = ""

while score < 81 and user_input != "Pes":
    user_input = window.textinput(title=header, prompt="Şehir: ")
    if user_input[0] == "i":
        user_input = "İ"+ user_input[1:]   # bug caused by capitalizing "i" -> "I" is fixed this way
    user_input = user_input.capitalize()
    if input is None:
        print(guessed_cities)
        print(f"{score}/81 şehir buldun.")
        break
    else:
        if user_input in sehir_list:
            if user_input in guessed_cities:
                header = f"Daha önce söylemiştin 🙁 {score}/81"
            else:
                score += 1
                guessed_cities.append(user_input)
                print_city(user_input)
                header = f"{score}/81 şehir buldun."
        elif user_input == "Pes":
            writer.pencolor("DarkRed")

            for _ in sehir_list:
                if _ not in guessed_cities:
                    missed_cities.append(_)
                    print_city(_)




        else:
            header = f"Yanlış cevap {score}/81"

window.mainloop()


print(f"Sonuç: {score}/81 il buldun.")
print("Kaçırdıkların: ")

i = 1
for _ in missed_cities:
    print(i, _)
    i += 1