import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Label, Entry, Button, LabelFrame
from tkinter import Canvas, Scrollbar, Frame, Label, BOTH, LEFT, BOTTOM, X, Y
import sqlite3
import csv

window=Tk()
window.title('LOGIN PAGE')
window.geometry("900x500")
window.minsize(900,500)
window.iconbitmap("C:\Python310\icon.ico.ico")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Load the image
background_img = Image.open(r"C:\Python310\irctc.png")
background_img = background_img.resize((screen_width, screen_height))  
background_img = ImageTk.PhotoImage(background_img)


        
headinglabel=Label(window,text='Railway Ticket Booking',
                   font=('Century Schoolbook',30,'bold'),bg='wheat1')
headinglabel.pack( fill=X)



login_frame=LabelFrame(window,text='Login Page',font=('Arial MT',15,'italic'))
login_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

background_label = Label(login_frame, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



def on_enter(event):
    event.widget.config(bg="lavender", fg="black")

def on_leave(event):
    event.widget.config(bg="wheat2", fg="black")
    
userid_label=Label(login_frame,text='USER ID 👤',font =('Arial Narrow',15,'bold'),width=20,height=2,bg='slategray1')
userid_label.grid(row=0,column=5,padx=25,pady=10)
userid_label.bind("<Enter>", on_enter)
userid_label.bind("<Leave>", on_leave)

userid_entry = Entry(login_frame, font=('arial', 15), bd=5, width=20)
userid_entry.grid(row=0, column=8, padx=10, pady=5)


    
password_label=Label(login_frame,text='Password 🔑',font =('Arial Narrow',15,'bold'),width=20,height=2,bg='slategray1')
password_label.grid(row=1,column=5,padx=25,pady=10)
password_label.bind("<Enter>", on_enter)
password_label.bind("<Leave>", on_leave)

password_entry = Entry(login_frame, font=('arial', 15), bd=5, width=20)
password_entry.grid(row=1, column=8, padx=10, pady=5)








#--------------------------------------------------------------------------------------
def login_button_clicked():
    username = userid_entry.get()
    password = password_entry.get()
    if username == 'A' and password == 'A':
        messagebox.showinfo('Login Successful','Welcome to ticket booking')
        open_main_window()
    else:
        messagebox.showerror('Login Failed', 'please reset')
        
def reset_button_clicked():
    userid_entry.delete(0, tk.END)  # Clear username entry
    password_entry.delete(0, tk.END)



def open_main_window():
    # Close the login window
    window.withdraw()
    main_window = tk.Toplevel(window)
    main_window.title("TICKET BOOKING")
    main_window.geometry("1500x900") # default size


    head1=Label(main_window,text='Railway Ticket Booking',font=('Century Schoolbook',30,'bold')
                   ,bg='wheat2')
    head1.pack( fill=X)
    

   # First frame
    frame1 = tk.LabelFrame(main_window, bg='lavender', bd=5)
    frame1.place(x=10,y=50,width=620,height=730)

  # label frame1

    def on_enter(event):
        event.widget.config(bg="lavender blush", fg="black")

    def on_leave(event):
        event.widget.config(bg="lavender", fg="black")

    label_names = ['Manage Tickets', 'Aadhar no', 'Name', 'Email', 'Gender', 'Contact', 'Depature date', 'Departure']

    label_positions = {
    'Manage Tickets 🎟': (250, 30),
    'Aadhar no🪪': (60, 70),
    'Name 🏷': (60, 140),
    'Email 📧': (60, 210),
    'Gender ⚥': (60, 280),
    'Contact 📞': (60, 350),
    'Departure date 📌': (60, 420),
    'Departure 🚂': (60, 490)
     }

    for label_text, (x, y) in label_positions.items():
        label = tk.Label(frame1, text=label_text, font=('Arial', 14), bg='lavender')
        label.place(x=x, y=y)
        label.bind("<Enter>", on_enter)
        label.bind("<Leave>", on_leave)

  
  

    # combo box
    gender_box3 = ttk.Combobox(frame1, values=['Female', 'Male','Others'], width=23, font=('Arial', 12))
    gender_box3.place(x=250, y=280)



    # entry bocx frame1

# AADHAR
    def validate_aadhar_number(text):
    
        return text.isdigit() and len(text) <= 12

    Aadhar_entry0 = Entry(frame1, font=('arial', 15), bd=5, width=20)
    Aadhar_entry0.place(x=250, y=70)

    validate_aadhar = frame1.register(validate_aadhar_number)
    Aadhar_entry0.config(validate="key", validatecommand=(validate_aadhar, "%P"))
# NAME
    Name_entry1 = Entry(frame1, font=('arial', 15), bd=5, width=20)
    Name_entry1.place(x=250, y=140)
# EMAIL
    Email_entry2 = Entry(frame1, font=('arial', 15), bd=5, width=20)
    Email_entry2.place(x=250, y=210)
# CONTACT
    def validate_contact_number(text):
    
        return text.isdigit() and len(text) <= 12
    
    Contact_entry4 = Entry(frame1, font=('arial', 15), bd=5, width=20)
    Contact_entry4.place(x=250, y=350)

    validate_contact = frame1.register(validate_contact_number)
    Contact_entry4.config(validate="key", validatecommand=(validate_contact, "%P"))
    
# DATE
    Departure_date_entry5 = Entry(frame1, font=('arial', 15), bd=5, width=20)
    Departure_date_entry5.place(x=250, y=420)
# ADDRESS
    Departure_entry6 = Entry(frame1, font=('arial', 15), bd=5, width=20)
    Departure_entry6.place(x=250, y=490)

    s_no=1

    def add_values_to_tree():
        global s_no

        
        aadhar = Aadhar_entry0.get()
        name = Name_entry1.get()
        email = Email_entry2.get()
        gender = gender_box3.get()
        contact = Contact_entry4.get()
        departure_date =Departure_date_entry5.get()
        departure = Departure_entry6.get()

        
        if aadhar and name  and email and gender and contact and departure_date and departure:
           num_entries = len(tree.get_children())
           tree.insert('', 'end', text=str(num_entries + 1), values=(aadhar, name, email, gender, contact, departure_date, departure))
 
           
            # Clear the entry boxes for reuse
           Aadhar_entry0.delete(0,tk.END)
           Name_entry1.delete(0, tk.END)
           Email_entry2.delete(0, tk.END)
           Contact_entry4.delete(0,tk.END)
           Departure_date_entry5.delete(0, tk.END)
           Departure_entry6.delete(0, tk.END)
               # Reset the gender combobox selection

           gender_box3.set('')

        
       
             
        else: 
            messagebox.showerror("Error", "All fields are required")
      
    
        with open('RESERVED TICKETS.txt', mode='a+') as file:
           file.write(f"Aadhar: {aadhar}, Name: {name}, Email: {email}, Gender: {gender}, Contact: {contact}, Departure Date: {departure_date}, Departure: {departure}\n")
          


           messagebox.showinfo("Success", "Booking details saved successfully.")

# button in frame1

    def on_enter(event):
        event.widget.config(bg="lightblue", fg="black")

    def on_leave(event):
        event.widget.config(bg="white", fg="black")

    Add_button1 = Button(frame1, text='ADD ➕', font=('arial', 13), bd=5, width=10,command=add_values_to_tree)
    Add_button1.place(x=60, y=600)
    Add_button1.bind("<Enter>", on_enter)
    Add_button1.bind("<Leave>", on_leave)




    # DELETE
    def delete_selected_row():
   
        selected_item = tree.focus()
    
    
        if selected_item:
           tree.delete(selected_item)
       
        else:
            messagebox.showerror("Error", "No row selected for deletion")

    Delete_button3 = Button(frame1, text='DELETE 🚮', font=('arial', 13), bd=5, width=10,command=delete_selected_row)
    Delete_button3.place(x=200, y=600)
    Delete_button3.bind("<Enter>", on_enter)
    Delete_button3.bind("<Leave>", on_leave)


    # CLEAR COMMAND
    def clear_tree_view():
        for item in tree.get_children():
            tree.delete(item)

    Clear_button4 = Button(frame1, text='CLEAR🗑', font=('arial', 13), bd=5, width=10,command=clear_tree_view)
    Clear_button4.place(x=350, y=600)
    Clear_button4.bind("<Enter>", on_enter)
    Clear_button4.bind("<Leave>", on_leave)



    # Second frame
    frame2 = tk.LabelFrame(main_window, bg='light blue', bd=5)
    frame2.place(x=630,y=50,width=900,height=728)

    # labels frame2
    def on_enter(event):
        event.widget.config(bg="silver", fg="black")

    def on_leave(event):
        event.widget.config(bg="lightblue", fg="black")
        
    Search1 = tk.Label(frame2, text="Search by ⌕", font=('Arial', 15), bg='lightblue')
    Search1.place(x=50, y=30)
    Search1.bind("<Enter>", on_enter)
    Search1.bind("<Leave>", on_leave)

    


    # button frame2
    def on_enter(event):
        event.widget.config(bg="lightblue", fg="black")

    def on_leave(event):
        event.widget.config(bg="white", fg="black")


    def search_tree_view():
        search_term = Search_entry1.get().lower()  # Get the search term from the entry field and convert to lowercase for case-insensitive search

        for item in tree.get_children():
            values = tree.item(item, 'values')
            if values:  # Check if values exist
               if search_term in [str(value).lower() for value in values]:
                  tree.selection_set(item)  # Select the matching item
                  tree.focus(item)  # Ensure the matching item is in view
                  return
        
    Search_button1 = Button(frame2, text='SEARCH BY', font=('arial', 13), bd=7, width=10,command=search_tree_view)
    Search_button1.place(x=500, y=30)
    Search_button1.bind("<Enter>", on_enter)
    Search_button1.bind("<Leave>", on_leave)



    # entry frame2
    Search_entry1 = Entry(frame2, font=('arial', 15), bd=7, width=20)
    Search_entry1.place(x=200, y=30)

   


# FRAME 3(TREE VIEWS)

    frame3 = tk.LabelFrame(frame2, bg='white', bd=5)
    frame3.place(x=35,y=100,width=800,height=600)
# trEE VEIW
    tree = ttk.Treeview(frame3, columns=('Aadhar','Name','Email','Gender','Contact','Departure date','Departure'))

    # define columns
    tree.heading('#0', text='s_no')
    tree.heading('#1', text='Aadhar')
    tree.heading('#2', text='Name')
    tree.heading('#3', text='Email')
    tree.heading('#4', text='Gender')
    tree.heading('#5', text='contact')
    tree.heading('#6', text='Departure date')
    tree.heading('#7', text='Departure')

    # set column widths
    tree.column('#0', width=40)
    tree.column('#1', width=100)
    tree.column('#2', width=100)
    tree.column('#3', width=100)
    tree.column('#4', width=100)
    tree.column('#5', width=100)
    tree.column('#6', width=100)
    tree.column('#7', width=100)
# ADD TREEVIEW TO FRAME3
    tree.pack(fill=tk.BOTH, expand=True)

#Add a vertical scrollbar
    vsb = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

# Add a horizontal scrollbar
    hsb = ttk.Scrollbar(frame3, orient="horizontal", command=tree.xview)
    hsb.pack(side='bottom', fill='x')
    tree.configure(xscrollcommand=hsb.set)

    
# frame selection
    def on_tree_select(event):
        selected_item = tree.focus()  # Get the item that was selected
        values = tree.item(selected_item, ('Aadhar','Name','Email','Gender','Contact','Departure date','Departure'))
    
    # Update the entry fields with the values from the selected row
        if values:
            Aadhar_entry0.delete(0, tk.END)
            Name_entry1.delete(0, tk.END)
            Email_entry2.delete(0, tk.END)
            gender_box3.set('')
            Contact_entry4.delete(0, tk.END)
            Departure_date_entry5.delete(0, tk.END)
            Departure_entry6.delete(0, tk.END)
        
            Aadhar_entry0.insert(0, values[0])
            Name_entry1.insert(0, values[1])
            Email_entry2.insert(0, values[2])
            gender_box3.set(values[3])
            Contact_entry4.insert(0, values[4])
            Departure_date_entry5.insert(0, values[5])
            Departure_entry6.insert(0, values[6])

            
        tree.bind('<<TreeviewSelect>>', on_tree_select)
    
    frame3.mainloop()
 #------------------------------------------------------   
def on_enter(event):
    event.widget.config(bg="lightblue", fg="black")

def on_leave(event):
    event.widget.config(bg="white", fg="black")
    
login_button = Button(login_frame, text='LOGIN', font=('arial', 15), bd=5, width=6,command=login_button_clicked )
login_button.grid(row=6, column=6, padx=10, pady=5,columnspan=2)
login_button.bind("<Enter>", on_enter)
login_button.bind("<Leave>", on_leave)

reset_button = Button(login_frame, text='RESET', font=('arial', 15), bd=5, width=6,command=reset_button_clicked)
reset_button.grid(row=6, column=7, padx=10, pady=5,columnspan=2)
reset_button.bind("<Enter>", on_enter)
reset_button.bind("<Leave>", on_leave)

     

window.mainloop()
