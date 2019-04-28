import tkinter 
from tkinter import messagebox
import pickle

root = tkinter.Tk()
root.configure(bg = "white")
root.title("AP Economics Review Guide") 
root.geometry("3000x3000")

to_delete = ""

class Concept():
    def __init__(self, definition, explanation, example): 
        self.definition = definition
        self.explanation = explanation
        self.example = example

concept_1 = Concept("Monopoly: a market structure with one firm producing a unique product, determine the product price with high barriers to enter and exit the market. Natural Monopoly: An industry makes the price cheaper and produces efficiently by having a monopoly than several smaller competing firms.", "Examples: Facebook, Paypal, Electric Power Companies, Phone Companies", "")
concept_2 = Concept("def2", "exp2", "exa2")
concepts = [concept_1, concept_2]


def show_concept_one():
    change_graph("monopoly.gif")
    for concept in concepts:
        definition = "{}".format(concept.definition)
        explanation = "{}".format(concept.explanation)
        example = "{}".format(concept.example)
    lbl_definition["text"] = concept_1.definition
    lbl_explanation["text"] = concept_1.explanation
    lbl_example["text"] = concept_1.example



def show_concept_two():
    change_graph("game.gif")
    for concept in concepts:
        definition = "{}".format(concept.definition)
        explanation = "{}".format(concept.explanation)
        example = "{}".format(concept.example)
    lbl_definition["text"] = concept_2.definition
    lbl_explanation["text"] = concept_2.explanation
    lbl_example["text"] = concept_2.example


def set_delete_definition(event = None):
    print("DEFINITION SET")
    global to_delete
    if to_delete == "definition":
        lbl_definition.configure(fg = "red")
    else: 


def set_delete_example(event = None):
    print("EXAMPLE SET")
    global to_delete
    to_delete = "example"
    lbl_example.configure(fg = "red")

def set_delete_explanation(event = None):
    print("EXPLANATION SET")
    global to_delete
    to_delete = "explanation"
    lbl_explanation.configure(fg = "red")


def delete_one():
    print("DELETE ONE")
    global to_delete
    print(to_delete)
    if to_delete == "definition":
        lbl_definition["text"] = ""
    elif to_delete == "explanation":
        lbl_explanation["text"] = ""
    elif to_delete == "example":
        lbl_example["text"] = ""


def load_file():
    data = pickle.load(open("Capstone.dat", "rb"))
    print("Loaded Data: {}".format(data))
    text_input.delete(1.0, "end")
    text_input.insert("end", data)


def save_file():
    data = text_input.get(1.0, "end")
    pickle.dump(data, open("Capstone.dat", "wb"))
    print("Saved Data: {}".format(data))



def exit():
    confirm = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to quit? Please make sure to save your notes before you quit.")
    if confirm: 
        global root
        root.quit()

def change_graph(image):
    photo = tkinter.PhotoImage(file = image )
    lb_graph.configure(image = photo)
    lb_graph.image = photo


lbl_button = tkinter.Label(root, text = "Button", bg = "White")
lbl_button.grid(row = 0, column = 0)

btn_concept_1 = tkinter.Button(root, text = "MOnopoly", fg = "black", width = 20, height = 3, command = show_concept_one) 
btn_concept_1.grid(row = 1, column = 0)

btn_concept_2 = tkinter.Button(root, text = "Game Theory", fg = "black", width = 16, height = 3, command = show_concept_two) 
btn_concept_2.grid(row = 2, column = 0)


btn_delete_one = tkinter.Button(root, text = "Delete One", fg = "black", width = 16, height = 3, command = delete_one) 
btn_delete_one.grid(row = 3, column = 0)

btn_save_file = tkinter.Button(root, text = "Save File", fg = "black", width = 16, height = 3, command = save_file) 
btn_save_file.grid(row = 4, column = 0)

btn_load_file = tkinter.Button(root, text = "Load File", fg = "black", width = 16, height = 3, command = load_file) 
btn_load_file.grid(row = 5, column = 0)

btn_exit = tkinter.Button(root, text = "Exit", fg = "black", width = 16, height = 3, command = exit) 
btn_exit.grid(row = 6, column = 0)

lbl_title = tkinter.Label(root, text = "Dates of Test: May 17 2019", bg = "White")
lbl_title.grid(row = 7, column = 0)

lbl_e = tkinter.Label(root, text = "Explanation", bg = "White")
lbl_e.grid(row = 0, column = 4)

lbl_definition = tkinter.Label(root, text = "" , bg = "white", width = 100)
lbl_definition.grid(row = 2, column = 4)
 
lbl_explanation = tkinter.Label(root, text = "" , bg = "white", width = 100)
lbl_explanation.grid(row = 4, column = 4)
 
lbl_example = tkinter.Label(root, text = "" , bg = "white", width = 100)
lbl_example.grid(row = 6, column = 4)
 
photo = tkinter.PhotoImage()
lb_graph = tkinter.Label(image = photo)
lb_graph.image = photo 
lb_graph.grid(row = 0, column = 8, rowspan = 7)

text_input = tkinter.Text(root, width = 58, bg="Yellow", bd=5)
text_input.grid(row = 7, column = 8, rowspan = 2) 

lbl_definition.bind("<Button-1>", set_delete_definition)

lbl_explanation.bind("<Button-1>", set_delete_explanation)

lbl_example.bind("<Button-1>", set_delete_example )



root.mainloop() 





