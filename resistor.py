print ("\tResistor color coding decoder")
print ("\n\n")
color = []
colornum = { "black" : "0", "brown" : "1", "red" : "2", "orange" : "3", "yellow" : "4" , "green" : "5", "blue" : "6", "violet" : "7" ,"grey" : "8" , "white" : "9" }
colorraise = { "black" : "⁰", "brown" : "¹", "red" : "²", "orange" : "³", "yellow" : "⁴" , "green" : "⁵", "blue" : "⁶", "violet" : "⁷" ,"grey" : "⁸" , "white" : "⁹" }
tolerance = {  "brown" : "+/-1%", "red" : "+/-2%", "orange" : "+/-3%", "yellow" : "+/-4%" , "green" : "+/-0.5%", "blue" : "+/-0.25%", "violet" : "+/-0.1%" ,"grey" : "+/-0.05%"  , "gold" : " +/- 5 %", "silver" : " +/- 10 %"}
colorcode = ''
for i in range (4):
    while True:
        colorin =  input (f"color of {i + 1} th line in resistor :")
        if i < 3:
            if colorin in colornum:
                break
            else:
                print ("\nEnter a valid color code \n")
        elif i < 4:
            if colorin in colorraise:
                break
            else:
                print ("\nEnter a valid color code \n")
        else:
             if colorin in tolerance:
                break
             else:
                print ("\nEnter a valid tolarance color code\n")
             
    color.append(colorin)
for i in range (4):
    if i < 2:
        colorcode += colornum[color[i]]
    elif i == 2:
        colorcode += f" x 10{colorraise[color[i]]}"
    else:
        colorcode += f"  {tolerance[color[i]]}"

print ("\n\nresistance = ",colorcode)
