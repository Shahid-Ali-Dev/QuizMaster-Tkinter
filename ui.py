from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz_brain :QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.label = Label(text=f"Score: 0",bg=THEME_COLOR,fg="white",font=("Arial",15,"bold"))
        self.label.grid(row=0,column=2)
        self.canvas = Canvas(width=500,height=300)
        self.text = self.canvas.create_text(250, 150, text="hehe", font=("Arial", 25, "italic"), width=450)
        self.canvas.grid(row=1, column=0,columnspan=3,pady=50)
        false = PhotoImage(file="images/false.png")
        true = PhotoImage(file="images/true.png")
        self.button = Button(image=false, highlightthickness=0, background=THEME_COLOR, width=85, height=80,command=self.false)
        self.button.grid(row=2, column=0)
        self.button2 = Button(image=true, highlightthickness=0, background=THEME_COLOR, width=85, height=80,command=self.true)
        self.button2.grid(row=2, column=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text,text= q_text)

        else:
            self.canvas.itemconfig(self.text, text=f"Your final score is {self.quiz.score}")
            self.button.config(state="disabled")
            self.button2.config(state="disabled")

    def true(self):
        iss_right = self.quiz.check_answer("True")
        self.check(iss_right)

    def false(self):
        iss_right =  self.quiz.check_answer("True")
        self.check(iss_right)

    def check(self,iss_right):

        if iss_right:
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



q = QuizInterface
