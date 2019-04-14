# capstone-

import tkinter 
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.configure(bg = "white")
root.title("AP Economics Review Guide") 
root.geometry("3000x3000")


class Concept():
    def __init__(self, definition, explanation, example): 
        self.definition = definition
        self.explanation = explanation
        self.example = example

concept_1 = Concept("def1", "exp1", "exa1")
concept_2 = Concept("def2", "exp2", "exa2")
concept_3 = Concept("def3", "exp3", "exa3")
concepts = [concept_1, concept_2, concept_3]

def delete_one():
    lb_explanation.delete("active")
    print(explanation)

def show_concept_one():
    lb_explanation.delete(0, "end")
    for concept in concepts:
        print("Definition: {}".format(concept.definition))
        print("Explanation: {}".format(concept.explanation))
        print("Example: {}".format(concept.example))
    lb_explanation.insert("end", concept_1.definition, concept_1.explanation, concept_1.example)


def show_concept_two():
    lb_explanation.delete(0, "end")
    for concept in concepts:
        print("Definition: {}".format(concept.definition))
        print("Explanation: {}".format(concept.explanation))
        print("Example: {}".format(concept.example))
    lb_explanation.insert("end", concept_2.definition, concept_2.explanation, concept_2.example)

def show_concept_three():
    lb_explanation.delete(0, "end")
    for concept in concepts:
        print("Definition: {}".format(concept.definition))
        print("Explanation: {}".format(concept.explanation))
        print("Example: {}".format(concept.example))
    lb_explanation.insert("end", concept_3.definition, concept_3.explanation, concept_3.example)

def save_file():
    data = text_input
    data = pickle.dump(data, open("Computer Science.dat", "wb"))
    messagebox.showinfo("Please Confirm", "Where do you want to save?")

def exit():
    confirm = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to quit? Please make sure to save your notes before you quit.")
    if confirm: 
        global root
        root.quit()

def dates():
    pass

lbl_button = tkinter.Label(root, text = "Button", bg = "White")
lbl_button.grid(row = 0, column = 0)

btn_concept_1 = tkinter.Button(root, text = "Foreign Exchange Market", fg = "black", width = 20, height = 3, command = show_concept_one) 
btn_concept_1.grid(row = 1, column = 0)

btn_concept_2 = tkinter.Button(root, text = "Game Theory", fg = "black", width = 16, height = 3, command = show_concept_two) 
btn_concept_2.grid(row = 2, column = 0)

btn_concept_3 = tkinter.Button(root, text = "Marginal Analysis", fg = "black", width = 16, height = 3, command = show_concept_three) 
btn_concept_3.grid(row = 3, column = 0)

btn_delete_one = tkinter.Button(root, text = "Delete One", fg = "black", width = 16, height = 3, command = delete_one) 
btn_delete_one.grid(row = 4, column = 0)

btn_save_file = tkinter.Button(root, text = "Save File", fg = "black", width = 16, height = 3, command = save_file) 
btn_save_file.grid(row = 5, column = 0)

btn_exit = tkinter.Button(root, text = "Exit", fg = "black", width = 16, height = 3, command = exit) 
btn_exit.grid(row = 6, column = 0)

lbl_title = tkinter.Label(root, text = "Countdown Dates", bg = "White")
lbl_title.grid(row = 7, column = 0)

lb_dates = tkinter.Listbox(root, height = 2) 
lb_dates.grid(row = 7, column = 0)

lbl_explanation = tkinter.Label(root, text = "Explanation", bg = "White")
lbl_explanation.grid(row = 0, column = 4)

lb_explanation = tkinter.Listbox(root, width = 100, height = 48) 
lb_explanation.grid(row = 1, column = 4, rowspan = 9)

lb_graph = tkinter.Listbox(root, width = 58, height = 20) 
lb_graph.grid(row = 0, column = 8, rowspan = 5)

text_input = tkinter.Text(root, width = 58, bg="Yellow", bd=5)
text_input.grid(row = 7, column = 8, rowspan = 2) 





root.mainloop() 





