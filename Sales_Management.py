import mysql.connector as m
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# database connectivity
mydatabase=m.connect(host="localhost",user="root",password="12345678",database="pythondb1")
cursor=mydatabase.cursor()

# creating the GUI
root = tk.Tk()
root.title("Sales Management System")
root.geometry('400x400')
root.config(bg="#ADD8E6")

# creating the labels and entry fields for sales data
product_label = tk.Label(root, text="Product Name", bg="#ADD8E6")
product_entry = tk.Entry(root)  
price_label = tk.Label(root, text="Price", bg="#ADD8E6")
price_entry = tk.Entry(root)
quantity_label = tk.Label(root, text="Quantity Sold", bg="#ADD8E6")
quantity_entry = tk.Entry(root)
date_label = tk.Label(root, text="Date", bg="#ADD8E6")
date_entry = tk.Entry(root)


# creating a button to add sales data to the database
def add_sales_data(): 
    # inserting the sales data into the database
    query1="INSERT INTO sales (product_name, price, quantity_sold, date) VALUES (%s,%s,%s,%s)"
    cursor.execute(query1, (product_entry.get(), price_entry.get(), quantity_entry.get(), date_entry.get()))
    messagebox.showinfo("Information","Record inserted Successfully")
    # commit the changes
    mydatabase.commit()


# creating a button that shows sales data
def show_sales_data():
    new_root = tk.Tk()
    new_root.geometry('440x550')
    new_root.title("Sales Data")
    new_root.config(bg="#ADD8E6")

    label = tk.Label(new_root,text="Sales Data",font="time 15 bold",bg="#0B5EC2",fg="White",padx=170,pady=15)   #Times New Roman, 15, Bold
    label.grid(row=0,column=0,columnspan=10)

    l1 = tk.Label(new_root, text="Product Name",font="time 12 bold", fg="#0B5EC2",bg="#ADD8E6")
    l1.grid(row=1,column=0,padx=10,pady=10)

    l2 = tk.Label(new_root, text="Price",font="time 12 bold", fg="#0B5EC2",bg="#ADD8E6")
    l2.grid(row=1,column=1,padx=10,pady=10)

    l3 = tk.Label(new_root, text="Quantity Sold",font="time 12 bold", fg="#0B5EC2",bg="#ADD8E6")
    l3.grid(row=1,column=2,padx=10,pady=10)

    l4 = tk.Label(new_root, text="Date",font="time 12 bold", fg="#0B5EC2",bg="#ADD8E6")
    l4.grid(row=1,column=3,padx=10,pady=10)


    # retrieve the sales data
    query2 = "SELECT * FROM sales"
    cursor.execute(query2)
    results = cursor.fetchall()
    
    # display the search results
    num = 2   # used to give row number in label
    for result in results:
        product_name = tk.Label(new_root,text=result[0],font="time 10 bold", fg="black",bg="#ADD8E6")
        product_name.grid(row=num, column = 0, padx=10,pady=10)

        Price = tk.Label(new_root,text=result[1],font="time 10 bold", fg="black",bg="#ADD8E6")
        Price.grid(row=num, column = 1, padx=10,pady=10)

        Quantity_Sold = tk.Label(new_root,text=result[2],font="time 10 bold", fg="black",bg="#ADD8E6")
        Quantity_Sold.grid(row=num, column = 2, padx=10,pady=10)

        Date = tk.Label(new_root,text=result[3],font="time 10 bold", fg="black",bg="#ADD8E6")
        Date.grid(row=num, column = 3, padx=10,pady=10)

        num=num+1
    

def graph():
    query3 = "SELECT sum(price*quantity_sold) from sales group by date"
    cursor.execute(query3)
    sum_price = cursor.fetchall()
    query4 = "SELECT date from sales group by date"
    cursor.execute(query4)
    date = cursor.fetchall()
    l1=[]
    for i in sum_price:
        l1.append(int(i[0]))
    l2=[]
    for i in date:
        l2.append(str(i[0]))
    plt.bar(l2,l1)
    plt.ylabel("Total Sale (Rs)")
    plt.xlabel("Date")
    plt.title("Daily Sales Details")
    plt.show()
    # print(sum_price)
    # print(date)


# creating the buttons for adding and showing sales data and graph
add_button = tk.Button(root, text="Add Sales Data", bg="#90EE90", command=add_sales_data)
show_button = tk.Button(root, text="Show Sales Data", bg="#90EE90",command=show_sales_data)
graph_button = tk.Button(root, text="Graph",bg="#90EE90",command=graph)

# pack GUI elements onto the screen
product_label.pack(pady=10)
product_entry.pack()
price_label.pack(pady=10)
price_entry.pack()
quantity_label.pack(pady=10)
quantity_entry.pack()
date_label.pack(pady=10)
date_entry.pack()
add_button.pack(pady=10)
show_button.pack(pady=10)
graph_button.pack()
root.mainloop()