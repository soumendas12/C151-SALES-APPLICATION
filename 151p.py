from tkinter import *
import random
root=Tk()
root.title("SALES APPLICATION")
root.geometry("700x500")
root.configure(bg="yellow")

month = ("January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

max_profits = Label(root)
min_profits = Label(root)
label_month = Label(root)
label_profit = Label(root)

label_month["text"] = "Months : " + str(month)
label_profit["text"] = "Profits : " + str(profits)

def maxprofit():
    max_profits["text"] =  " The maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month)
    
def minprofit():
    min_profits["text"] =  " The minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print( " The maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month))

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print( " The minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month))

btn1 = Button(root)
btn1 = Button(root, text = "Show Max Profitable Month", command = maxprofit, bg="blue", fg="white")    
btn1.place(relx = 0.5,rely = 0.4, anchor = CENTER)
btn2 = Button(root)
btn2 = Button(root, text = "Show Min Profitable Month", command = minprofit, bg="blue", fg="white")    
btn2.place(relx = 0.5,rely = 0.6, anchor = CENTER)

label_month.place(relx=0.5,rely=0.2, anchor=CENTER)
label_profit.place(relx=0.5,rely=0.3, anchor=CENTER)
max_profits.place(relx=0.5,rely=0.5, anchor=CENTER)
min_profits.place(relx=0.5,rely=0.7, anchor=CENTER)
    
root.mainloop()