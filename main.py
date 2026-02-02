import tkinter as tk

# interface
root = tk.Tk()
root.title("Roman to Decimal Converter")
root.geometry("400x700")
bg_path= tk.PhotoImage(file = "images/bg.png")
bg = tk.Label(root, image = bg_path)
bg.place(x = 0, y = 0)

# global variables
total = 0
roman = ""

# text configuration
text = tk.Text(root, height = 5, width = 52)
label_total = tk.Label(root, text=total, font = ("Sans", 50, "bold"), fg = "#011640", bg = "#D98B48")
label_total.place(x=15, y=55)
label_roman = tk.Label(root, text=roman, font = ("Sans", 20, "bold"), fg = "#8C322A", bg = "#D98B48")
label_roman.place(x=305, y=105) 

def submit():
    global roman, total

    if not roman:
        return
    
    total = 0

    # conversion logic
    hm = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
    cache = 0
    for i in range(0,len(roman)):
        if i!=0:
            if roman[i] != roman[i-1]:
                total = total + cache if hm[roman[i]] < hm[roman[i-1]] else total - cache
                cache = 0
        cache += hm[roman[i]]
    total += cache

    label_total.config(text=total)
    roman = ""
    label_roman.config(text="")

def get_click(event):
    global roman, total
    x,y = event.x, event.y

    # button map
    if 335 > y >= 155:
        if 135 > x >= 5:
            roman += "I"
        if 265 > x >= 135:
            roman += "V"
        if 395 > x >= 265:
            roman += "X"
    if 515 > y >= 335:
        if 135 > x >= 5:
            roman += "L"
        if 265 > x >= 135:
          roman += "C"
        if 395 > x >= 265:
            roman += "D"
    if y > 515:
        if 135 > x >= 5:
            roman += "L"
        else:
            submit()
    if y < 155:
        roman = ""
        total = 0

    label_roman.config(text=roman)

root.bind("<Button-1>", get_click)
root.mainloop()
