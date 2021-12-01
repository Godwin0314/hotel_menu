from tkinter import *
import tkinter.messagebox as MessageBox
from PIL import ImageTk

window=Tk()
window.title('Food Menu')
window.geometry('500x500')

def briyani():
    food_name_lbl.place(x=20,y=300)
    food_name_txt.place(x=130,y=300)
    qty_lbl.place(x=20,y=327.5)
    qty_txt.place(x=130,y=330)
    order_btn.place(x=50,y=360)
    food_name_txt.delete(0,END)
    food_name_txt.insert(0,'Chicken Briyani')
    
def fri_rice():
    food_name_lbl.place(x=20,y=300)
    food_name_txt.place(x=130,y=300)
    qty_lbl.place(x=20,y=327.5)
    qty_txt.place(x=130,y=330)
    order_btn.place(x=50,y=360)
    food_name_txt.delete(0,END)
    food_name_txt.insert(0,'Chicken Fried Rice')
    
def noodles():
    food_name_lbl.place(x=20,y=300)
    food_name_txt.place(x=130,y=300)
    qty_lbl.place(x=20,y=327.5)
    qty_txt.place(x=130,y=330)
    order_btn.place(x=50,y=360)
    food_name_txt.delete(0,END)
    food_name_txt.insert(0,'Chicken Noodles')

def grill():
    food_name_lbl.place(x=20,y=300)
    food_name_txt.place(x=130,y=300)
    qty_lbl.place(x=20,y=327.5)
    qty_txt.place(x=130,y=330)
    order_btn.place(x=50,y=360)
    food_name_txt.delete(0,END)
    food_name_txt.insert(0,'Chicken Grill')

def tandoori():
    food_name_lbl.place(x=20,y=300)
    food_name_txt.place(x=130,y=300)
    qty_lbl.place(x=20,y=327.5)
    qty_txt.place(x=130,y=330)
    order_btn.place(x=50,y=360)
    food_name_txt.delete(0,END)
    food_name_txt.insert(0,'Chicken Tandoori')

def order():
    name = food_name_txt.get()
    qty = qty_txt.get()
    if name == 'Chicken Briyani':
        qty = int(qty)*120
        bill = Label(window,text='Bill amount is '+str(qty))
        bill.place(x=20,y=400)
        MessageBox.showinfo('order success','Order placed successfully')
        bill.destroy()
    elif name == 'Chicken Fried Rice':
        qty = int(qty)*100
        bill = Label(window,text='Bill amount is '+str(qty))
        bill.place(x=20,y=400)
        MessageBox.showinfo('order success','Order placed successfully')
        bill.destroy()
    elif name == 'Chicken Noodles':
        qty = int(qty)*100
        bill = Label(window,text='Bill amount is '+str(qty))
        bill.place(x=20,y=400)
        MessageBox.showinfo('order success','Order placed successfully')
        bill.destroy()
    elif name == 'Chicken Grill':
        qty = int(qty)*350
        bill = Label(window,text='Bill amount is '+str(qty))
        bill.place(x=20,y=400)
        MessageBox.showinfo('order success','Order placed successfully')
        bill.destroy()
    elif name == 'Chicken Tandoori':
        qty = int(qty)*300
        bill = Label(window,text='Bill amount is '+str(qty))
        bill.place(x=20,y=400)
        MessageBox.showinfo('order success','Order placed successfully')
        bill.destroy()
    else:
        MessageBox.showinfo('order warning','please type the food name correctly in the menu')
    food_name_txt.delete(0,END)
    qty_txt.delete(0,END)

heading_lbl=Label(window,text='Hello Restaurant',font=('bold',25),fg='brown').place(x=130,y=20)

dname_lbl=Label(window,text='Menu',font=('bold'))
dname_lbl.place(x=100,y=80)

price_lbl=Label(window,text='Price',font=('bold'))
price_lbl.place(x=220,y=80)

code_lbl=Label(window,text='Code',font=('bold'))
code_lbl.place(x=300,y=80)

bri_lbl=Label(window,text='Chicken Briyani')
bri_lbl.place(x=100,y=120)

bri_price_lbl=Label(window,text='120')
bri_price_lbl.place(x=230,y=120)

bri_code_lbl=Label(window,text='001')
bri_code_lbl.place(x=310,y=120)

fri_rice_lbl=Label(window,text='Chicken Fried Rice')
fri_rice_lbl.place(x=100,y=140)

fri_rice_price_lbl=Label(window,text='100')
fri_rice_price_lbl.place(x=230,y=140)

fri_rice_code_lbl=Label(window,text='002')
fri_rice_code_lbl.place(x=310,y=140)

noodles_lbl=Label(window,text='Chicken Noodles')
noodles_lbl.place(x=100,y=160)

noodles_price_lbl=Label(window,text='100')
noodles_price_lbl.place(x=230,y=160)

noodles_rice_code_lbl=Label(window,text='003')
noodles_rice_code_lbl.place(x=310,y=160)

grill_lbl=Label(window,text='Chicken Grill')
grill_lbl.place(x=100,y=180)

grill_price_lbl=Label(window,text='350')
grill_price_lbl.place(x=230,y=180)

grill_code_lbl=Label(window,text='004')
grill_code_lbl.place(x=310,y=180)

tandoori_lbl=Label(window,text='Chicken Tandoori')
tandoori_lbl.place(x=100,y=200)

tandoori_price_lbl=Label(window,text='300')
tandoori_price_lbl.place(x=230,y=200)

tandoori_code_lbl=Label(window,text='005')
tandoori_code_lbl.place(x=310,y=200)

select_food_name_lbl=Label(window,text='Press the Food Code')
select_food_name_lbl.place(x=20,y=260)

bri_btn=Button(window,text='001',command=briyani)
bri_btn.place(x=140,y=255)

fri_btn=Button(window,text='002',command=fri_rice)
fri_btn.place(x=180,y=255)

noodles_btn=Button(window,text='003',command=noodles)
noodles_btn.place(x=220,y=255)

grill_btn=Button(window,text='004',command=grill)
grill_btn.place(x=260,y=255)

tandoori_btn=Button(window,text='005',command=tandoori)
tandoori_btn.place(x=300,y=255)

food_name_lbl=Label(window,text='Food Name')
food_name_txt=Entry(window)

qty_lbl=Label(window,text='Enter the Quantity')
qty_txt=Entry(window)

order_btn=Button(window,text='Place Order',command=order,bg='skyblue')

window.mainloop()
