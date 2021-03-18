''' importing all modules from tkinter'''
from tkinter import *
import tkinter.ttk as ttk
from random import *
import datetime 

''' Declare parent class called MathsQuiz, All objects created from parent class'''
class MathsQuiz:
    ''' use init method for all widgets'''
    def __init__(self,parent):
        
        '''Widget for Welcome Frame '''
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        self.TitleLable = Label(self.Welcome, text = "Welcome to Maths Quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.TitleLable.grid(columnspan = 2)
        
        self.NextButton = ttk.Button(self.Welcome, text = 'Next', command = self.show_Questions)
        self.NextButton.grid(row = 10, column = 1)
        self.NextButton.bind("<Return>", lambda event: self.show_Questions()) #binds NextButton to Enter key
        root.bind("<Return>", lambda event: self.show_Questions())
        
        
        ''' Widgets for questions frame'''
        
        self.index = 0
        self.score = 0
        
        self.Questions = Frame(parent)
        #self.Questions.grid(row=0, column=1)
        
        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)
        
        self.HomeButton = ttk.Button(self.Questions, text = 'Next', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 0)
        
        
        self.Problems = Label(self.Questions, text = "")
        self.Problems.grid(row = 1, column = 0)
        
        self.AnswerEntry = ttk.Entry(self.Questions, width = 20)
        self.AnswerEntry.grid(row=1, column = 1)
        #Create scorelabel
        self.ScoreLabel = Label(self.Questions, text = "")
        self.ScoreLabel.grid(row = 1, column = 2)
        
        
        self.feedback = Label(self.Questions, text = "")
        self.feedback.grid(row=2, column = 0)
        
        self.Homebutton = ttk.Button(self.Questions, text = "Home", command = self.show_Welcome)
        self.Homebutton.grid(row=8, column=0)
        
        self.check_button = ttk.Button(self.Questions, text = "Check Answer", command = self.check_answer)
        self.check_button.grid(row=8, column=1)
        
        #self.next_button = ttk.Button(self.Questions, text = 'Next Question', command = self.next_question)
        #self.next_button.grid(row=8, column=2)
        
        
        ''' Name and Age labels '''
        self.NameLabel = Label(self.Welcome, text = "Name", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.NameLabel.grid(row = 2, column = 0)
        
        self.AgeLabel = Label(self.Welcome, text = "Age", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.AgeLabel.grid(row=3, column = 0)
        
        #Name and Age Entry
        self.name = StringVar()
        self.name.set("")
        self.NameEntry = ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row=2, column = 1, columnspan = 2)
        
        self.age = IntVar()
        self.age.set("")
        self.AgeEntry = ttk.Entry(self.Welcome, width = 20)
        self.AgeEntry.grid(row=3, column = 1)
        
        #Difficulty level label/radio buttons
        self.WarningLabel = Label(self.Welcome, text = "", anchor=W, fg = "red", width = 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row=4, columnspan = 2)
        self.DifficultyLabel = Label(self.Welcome, text = "Choose Difficulty", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.DifficultyLabel.grid(row = 5, column = 0)
        
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0) #Ref to onenote for usage info
        self.diff_btns = []
        
        for i in range(len(self.difficulty)):
            self.rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(self.rb)
            self.rb.grid(row = i+6, column = 0, sticky = W)
            
        '''Widgets for Report Frame'''
        
        self.Report_frame = Frame(parent)
        self.Report_frame.grid_propagate(4)
        
        Report_page = ["Name", "Age", "Score"]
        self.report_labels = []
        
        for i in range(len(Report_page)):
            ColumnHeading = Label(self.Report_frame, text = Report_page[i], width = "7", height = "2", font = ("Times", "15", "bold"))
            self.report_labels.append(ColumnHeading)
            ColumnHeading.grid(row=0, column = i+1)
            
        self.user_name = Label(self.Report_frame, textvariable = self.name)
        self.user_name.grid(row = 3, column=1)
        
        self.user_age = Label(self.Report_frame, textvariable = self.age)
        self.user_age.grid(row=3, column=2)
        
        self.user_score = Label(self.Report_frame, text = "")
        self.user_score.grid(row=3, column=3)
        
        self.Home = ttk.Button(self.Report_frame, text = 'Home', command = self.show_Welcome)
        self.Home.grid(row = 8, column = 1)
        
        self.Exit = ttk.Button(self.Report_frame, text = 'Close', command = self.show_Welcome)
        self.Exit.grid(row = 8, column = 4)
        
        
        
        ''' a method that removes quesitons frame'''
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()
        
    def show_Questions(self):
        try:   
            if self.NameEntry.get() == "":
                self.WarningLabel.configure(text = "Please enter your name")
                self.NameEntry.focus()
                
            elif self.NameEntry.get().isalpha() == False:
                self.WarningLabel.configure(text = "Please enter a text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()
                
            elif self.AgeEntry.get() == "":
                self.WarningLabel.configure(text = "Please enter your age")
                self.AgeEntry.focus()
                
            elif int(self.AgeEntry.get()) > 12:
                self.WarningLabel.configure(text = "You are too old!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()
                
            elif int(self.AgeEntry.get()) < 0:
                self.WarningLabel.configure(text = "You are too old")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()
            elif int(self.AgeEntry.get()) < 7:
                self.WarningLabel.configure(text = "You are too young!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()
            else:
                self.name.set(self.NameEntry.get())
                self.age.set(self.AgeEntry.get())
                self.Welcome.grid_remove()
                self.Questions.grid()
                self.next_question() #calls next question function
                score_text = "Score: " + str(self.score)
                self.ScoreLabel.configure(text = score_text)

        except ValueError:
            self.WarningLabel.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()
            
    def next_question(self):
        '''creates questions and stores answers'''
        x = randrange(10)
        y = randrange(10)
        self.answer = x + y
        self.index += 1 #keep adding to index number
        
        question_text = str(x) + " + " + str(y) + " = "
        
        self.Problems.configure(text = question_text)
        #update QL with question number
        self.QuestionsLabel.configure(text = "Quiz Question " + str(self.index) + "/5")
        #limit number questions to 5, then remove questions frame, move to welcome
        if self.index >=6:
            self.Questions.grid_remove()
            self.Report_frame.grid(row=1, columnspan=4)
            ''' records user details to record.txt '''
            with open('records.txt', 'a+') as data_file:
                data_file.write(self.name.get() + ' ' + str(self.age.get()) + ' ' + str(self.score) + ' ' + '/n')
                
        
    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())
            
            if ans == self.answer:
                self.feedback.configure(text = "Correct", fg = "green")
                self.score += 1 #add 1 to the score for correct answer
                score_text = "Score =" + str(self.score)
                self.ScoreLabel.configure(text = score_text)
                self.user_score.configure(text = score_text)
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()
                
            else: 
                self.feedback.configure(text = "Incorrect", fg = "red")
                self.AnswerEntry.delete(0, END) 
                self.AnswerEntry.focus()
                self.next_question()
                
        except ValueError:
            self.feedback.configure(text = "Enter a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()
            
    def Restart(self):
        self.Report_frame.grid_remove()
        restart = MathsQuiz(root)
            
#Main Routine
if __name__ == "__main__":
    root =Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop()
        
