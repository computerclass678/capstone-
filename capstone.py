import tkinter 

root = tkinter.Tk()
root.configure(bg = "white")
root.title("AP Economics Review Guide") 
root.geometry("3000x3000")



def concept_1(): 
    pass 

def concept_2(): 
    pass 

def concept_3(): 
    pass 

def update_listbox():
    pass

def clear_listbox(): 
    pass 

def show_all():
    pass


def delete_one():
    pass 

def save_file():
    pass 

def exit():
    pass
    







btn_concept_1 = tkinter.Button(root, text = "Foreign Exchange Market", fg = "black", width = 20, command = concept_1) 
btn_concept_1.grid(row = 0, column = 0)

btn_concept_2 = tkinter.Button(root, text = "Game Theory", fg = "black", width = 16, command = concept_2) 
btn_concept_2.grid(row = 1, column = 0)

btn_concept_3 = tkinter.Button(root, text = "Marginal Analysis", fg = "black", width = 16, command = concept_3) 
btn_concept_3.grid(row = 2, column = 0)

btn_show_all= tkinter.Button(root, text = "Show All", fg = "black", width = 16, command = show_all) 
btn_show_all.grid(row = 3, column = 0)

btn_delete_one = tkinter.Button(root, text = "Delete One", fg = "black", width = 16, command = delete_one) 
btn_delete_one.grid(row = 4, column = 0)

btn_save_file = tkinter.Button(root, text = "Save File", fg = "black", width = 16, command = save_file) 
btn_save_file.grid(row = 5, column = 0)

btn_quit = tkinter.Button(root, text = "Exit", fg = "black", width = 16, command = exit) 
btn_quit.grid(row = 6, column = 0)

lbl_title = tkinter.Label(root, text = "Countdown Dates", bg = "White")
lbl_title.grid(row = 8, column = 0)

lb_dates = tkinter.Listbox(root, height = 2) 
lb_dates.grid(row = 9, column = 0)

lb_explanation = tkinter.Listbox(root, width = 110, height = 20) 
lb_explanation.grid(row = 1, column = 1)

lb_graph = tkinter.Listbox(root, width = 50, height = 20) 
lb_graph.grid(row = 0, column = 3)

lb_note = tkinter.Listbox(root, width = 50, height = 20) 
lb_note.grid(row = 1, column = 3)

root.mainloop() 





