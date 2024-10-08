import string
from random import choice, randint, shuffle
from tkinter import END, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox
import json

color_wndw_img_lbl = "#0C3C78"
color_ntr = "white"
color_bttm = "#3498DB"
letter = "#ECF0F1"
letter2 = "black"

def generate_password():
  letters = [choice(string.ascii_lowercase) for _ in range(randint(0,4))]
  LETTERS = [choice(string.ascii_uppercase) for _ in range(randint(0,4))]
  numbers = [str(randint(0,9)) for _ in range(randint(0,2))]
  symbols = [choice(string.punctuation) for _ in range(randint(0,2))]
  password_list = letters + LETTERS + numbers + symbols
  shuffle(password_list)
  password = ''.join(password_list)
  pass_entry.delete(0,END)
  pass_entry.insert(0,password)
  
def search():
  search = web_entry.get().lower()
  try:
    if search == "":
      messagebox.showwarning(title="Oops", message="Please enter key for seaching")
    else:
      with open("data.json", "r") as file:
        if search not in json.load(file).keys():
          messagebox.showinfo(title="Error", message=f"No details for {search} exists")
        else:
          with open("data.json", "r") as file:
            for key, value in json.load(file).items():
              if search == key.lower():
                name = key
                messagebox.showinfo(title=name, message=f"Email: {value['email']}\nPassword: {value['password']}")
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No Data File Found")     
  finally:            
    web_entry.delete(0,END)
    web_entry.focus()      

def save_clear():
  website = web_entry.get()
  email = email_user_entry.get()
  password = pass_entry.get()
  new_data = {
    website: {
      "email": email,
      "password": password
    }
  }
  if len(website) == 0 or len(password) == 0 or len(email) == 0 :
    messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
  else:
    is_ok = messagebox.askokcancel(title=website, message="This are the details you have entered\n" + 
      f"Email: {email}\n" + 
      f"Password: {password}\n"+
      "Is it ok to save?")
    if is_ok:
        try:
          with open("data.json", "r") as data_file:
            data = json.load(data_file)
        except FileNotFoundError:
          with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
        else:
          data.update(new_data)
          with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        finally:
          web_entry.delete(0,END)
          email_user_entry.delete(0,END)
          pass_entry.delete(0,END)
          web_entry.focus()

window = Tk()
window.title("Password Manager By Aaron Diaz")
window.config(width=500, height=380, padx=5, pady=5, bg=color_wndw_img_lbl)
window.resizable(False, False)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.config( highlightthickness=0, bg=color_wndw_img_lbl)
canvas.place(x=150, y=50)

web_label = Label(text="Website:", bg=color_wndw_img_lbl, fg=letter)
web_label.place(x=60, y=251)
web_entry = Entry(width=21, highlightthickness=0, bg=color_ntr, fg=letter2)
web_entry.place(x=150, y=251)

email_user_label = Label(text="Email/Username:", bg=color_wndw_img_lbl, fg=letter)
email_user_label.place(x=30, y=280)
email_user_entry = Entry(width=38, highlightthickness=0, bg=color_ntr, fg=letter2)
email_user_entry.place(x=150, y=280)

pass_label = Label(text="Password:", bg=color_wndw_img_lbl, fg=letter)
pass_label.place(x=50,y=308)
pass_entry = Entry(width=21, highlightthickness=0, bg=color_ntr, fg=letter2)
pass_entry.place(x=150,y=308)
pass_button = Button(text="Generate Password",highlightthickness=1, fg=letter, bg=color_bttm, command = generate_password)
pass_button.config(padx=1, pady=0)
pass_button.place(x=325, y=308)

add_button = Button(text="Add", width=38,highlightthickness=0, fg=letter, bg=color_bttm, command=save_clear)
add_button.config(padx=1, pady=0)
add_button.place(x=149, y=339)

search_button = Button(text="Search", fg=letter,width=15, bg=color_bttm, command=search)
search_button.config(highlightthickness=1, padx=1, pady=0)
search_button.place(x=330, y=250)

window.mainloop()