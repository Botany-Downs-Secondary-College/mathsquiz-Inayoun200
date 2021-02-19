#Welcome.py

from tkinter import*
from tkinter import ttk

#Parent class
class MathQuiz:
    def __init__(self,parent) :

        ' ' 'Widgets for welcome frame' ' '

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Qiuz",
                                bg = "black", fg = "white", width = 20, padx = 30,pady = 10,
                                font = ("Time", '14', "bold italic"))
        self.TitleLabel.grid(columnspan = 2)

        self.NextButton = ttk.Button(self.Welcome, text = 'Next', command = self.show_Questions)
        self.NextButton.grid(row = 8, column = 1)

        ' ' ' Widgets for Questions Frame' ' '

        self.Questions = Frame(parent)
        #self.Questions.grid(row=0, column = 1)

        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                                    bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                    font = ("Time", '14', "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)

        self.HomeButton = ttk.Button(self.Questions, text = 'Home', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 1)

        ' ' 'A method that removes Questions Frame' ' '
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()
        
    def show_Questions(self):
        self.Welcome.grid_remove()
        self.Questions.grid()

        #Name and Age labels
        self.NameLabel = Label(self.Welcome, text = "Next", anchor = W,
                               fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
        self.NameLabel.grid(row = 2, column = 0)

        self.AgeLabel = Label(self.Welcome, text = "Age", anchor=W,
                              fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
        self.AgeLabel.grid(row=3, column = 0)


        #Name and Age Entry
        self.NameEntry = ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row=2, column = 1, columnspan = 2)

        self.AgeEntry = ttk.Entry(self.Welcome, width =20)
        self.AgeEntry.grid(row=3, column = 1)

        #Difficulty level label and radio buttons
        self.DifficultyLabel = Label(self.Welcome, text = "Choose Difficulty level", anchor=W,
                                     fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
        self.DifficultyLabel.grid(row=4, column = 0)

        self.difficulty = ["Easy", "Medium", "Hard", 'Super hard']
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i],
                             anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+5, column = 0, sticky = W)
                
                                                                                     
    
#Main routine
if __name__ == "__main__":
        root =Tk()
        frames = MathQuiz(root)
        root.title("Quiz")
        root.mainloop() #binds the above commands together


            

