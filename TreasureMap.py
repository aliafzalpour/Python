row1 = ["🟦","🟦","🟦"]
row2 = ["🟦","🟦","🟦"]
row3 = ["🟦","🟦","🟦"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if int(position) >= 33 or int(position) <= 11 :
    print("you are lost!")

else :
    vertical = int(position[0])
    horizental = int(position[1])

    selected_row = map[vertical - 1]
    selected_row[horizental - 1] = "*"

    print(f"{row1}\n{row2}\n{row3}")