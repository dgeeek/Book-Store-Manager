from tkinter import*
import book_store_backend

def view_all():
    list1.delete(0, END)
    for item in book_store_backend.view():
        list1.insert(END, item)

def search_entry():
    item = book_store_backend.search(title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get())
    list1.delete(0, END)
    for i in item:
        list1.insert(END, i)

def add_entry():
    book_store_backend.insert(title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get())
    list1.delete(0, END)
    for item in book_store_backend.view():
        list1.insert(END, item)


def selected_row_tuple(event):
    global selected_row
    index = list1.curselection()[0] #pointing to the 1st element of the selected row's[here i.e. id]
    selected_row = list1.get(index)#saving the tuple at the pointed position

def delete_row():
    book_store_backend.delete(selected_row[0])

def update_row():
    id = selected_row[0]
    book_store_backend.update(id, title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get())
    view_all()

window = Tk()

l1 = Label(window,text="Title")
l1.grid(row = 0, column = 0)

l2 = Label(window,text="Author")
l2.grid(row = 0, column = 2)

l3 = Label(window,text="Year")
l3.grid(row = 1, column = 0)

l4 = Label(window,text="ISBN")
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

Author_text = StringVar()
e1 = Entry(window, textvariable = Author_text)
e1.grid(row = 0, column = 3)

Year_text = StringVar()
e1 = Entry(window, textvariable = Year_text)
e1.grid(row = 1, column = 1)

ISBN_text = StringVar()
e1 = Entry(window, textvariable = ISBN_text)
e1.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

scroll1 = Scrollbar(window)
scroll1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = scroll1.set)
scroll1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>',selected_row_tuple)

b1 = Button(window, text = "View All", width = 12, command = view_all)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command = search_entry)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = add_entry)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update", width = 12, command = update_row)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete", width = 12, command = delete_row)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()
