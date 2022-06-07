from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.geometry("900x500")
label_selected_doctor=Label(root)
label_selected_doctor.place(relx=0.01, rely=0.3,anchor=W)
label_selected_IT=Label(root)
label_selected_IT.place(relx=0.01, rely=0.6,anchor=W)
label_selected_chemical=Label(root)
label_selected_chemical.place(relx=0.01, rely=0.9,anchor=W)
class parent():
    def __init__(self):
        print("This is parent class")
    def doctor(doctor_name):
        hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
        random_hospital = random.randint(0,3)
        label_selected_doctor['text'] = doctor_name+" has been alloted to "+hospital_list[random_hospital]
    def softwareEngineer(it_professional_name):
        IT_company_list = ["I code", "Web Access", "Dotcom Services", "ATOS"]
        random_IT_company = random.randint(0,3) 
        #update the below code by storing it inside the 'text' property of the label_selected_IT
        label_selected_IT = it_professional_name+" has been alloted to "+IT_company_list[random_IT_company]
        
        #define a function chemicalEngineer() and inside it pass the variable chemical_engineer_name
    def chemicalEngineer(chemical_engineer_name):
        company_list = ["Google", "Amazon", "Nividia", "Github", "Apple"]
        #define variable company_list and inside it store the list of companies of your choice in square bracktes.
      
        # generate a random number between 0 and 3 using randint() function and store it in variable random_company.
        random_company = random.randint(0, 4)
        label_selected_chemical['text'] = chemical_engineer_name+" has been alloted to "+company_list[random_company] 
        
class child1(parent):
    def __init__(self):
        print("This is child1 class")
    def getDoctor(self):
        name = "Micheal"
        parent.doctor(name)
        
class child2(parent):
    def __init__(self):
        print("This is child2 class")
    def getIT(self):
        name = "Jessica"
        parent.softwareEngineer(name) 

#define the class child3(parent) inside.
class child3(parent):
    #define the __init__(self) function and inside it print the statement as "This is child3 class"
    def __init__(self):
        print("CHILD3 has been summoned")
    #define the getChemical(self) function 
    def getChemical(self):
        #define a variable name and store a name of your choice
        name = "LOOMPA"
        parent.chemicalEngineer(name)
        
obj1 = child1()
obj2 = child2()
obj3 = child3()
btn_doctor = Button(root, text="Show the hospital alloted", command=obj1.getDoctor)
btn_doctor.place(relx=0.1, rely=0.23,anchor=CENTER)
btn_it = Button(root, text="Show the IT company alloted", command=obj2.getIT)
btn_it.place(relx=0.11, rely=0.53,anchor=CENTER)
btn_chemical = Button(root, text="Show the chemical company alloted", command=obj3.getChemical)
btn_chemical.place(relx=0.13, rely=0.83,anchor=CENTER)
root.mainloop()