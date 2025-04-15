from tkinter import *
from random import randint, choice

root = Tk()
root.geometry("800x600")
root.title("✨ Maths Quiz Game ✨")
root.configure(bg="#E3F2FD")  # Softer blue background

question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()

FONT_TITLE = ("Helvetica", 30, "bold")
FONT_MAIN = ("Helvetica", 24)
FONT_NORMAL = ("Helvetica", 18)
COLOR_CORRECT = "#2E7D32"
COLOR_WRONG = "#C62828"
COLOR_FINAL = "#6A1B9A"
COLOR_BTN = "#039BE5"
COLOR_BG = "#E3F2FD"
COLOR_TEXT = "#0D47A1"

def generateQuestion():
    if questionNumber.get() >= 10:
        return
    questionNumber.set(questionNumber.get() + 1)
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operator = choice(["+", "-", "*", "/"])
    if operator == "/":
        number1 *= number2  #to restrict the answer into whole number we make number1=number1*number2
    question.set(f"{number1} {operator} {number2}")
    answer.set(str(round(eval(question.get()), 2)))
    questionLabel.config(text=f"Q{questionNumber.get()}: {question.get()}")
    answerEntry.delete(0, END)

def checkAnswer():
    if questionNumber.get() > 10:
        return 

    if str(answer.get()) == givenAnswer.get().strip():
        score.set(score.get() + 1)
        resultLabel.config(text="✅ Correct!", fg=COLOR_CORRECT)
    else:
        resultLabel.config(text=f"❌ Incorrect! Ans: {answer.get()}", fg=COLOR_WRONG)

    scoreLabel.config(text=f"Score: {score.get()}")

    if questionNumber.get() == 10:
        questionLabel.config(text="🎉 Quiz Complete!")
        resultLabel.config(text=f"🎯 Final Score: {score.get()}/10", fg=COLOR_FINAL)
        submitButton.config(state=DISABLED)
        answerEntry.config(state=DISABLED)
    else:
        root.after(500, generateQuestion)

def restart():
    score.set(0)
    questionNumber.set(0)
    scoreLabel.config(text="Score: 0")
    resultLabel.config(text="")
    answerEntry.config(state=NORMAL)
    submitButton.config(state=NORMAL)
    generateQuestion()

# Layout
headingLabel = Label(root, text="✨ Maths Quiz Game ✨", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_TEXT)
headingLabel.grid(row=0, column=0, columnspan=3, pady=30)

questionLabel = Label(root, text="Question", font=FONT_MAIN, bg=COLOR_BG, fg="black")
questionLabel.grid(row=1, column=0, columnspan=3, pady=20)

answerEntry = Entry(root, textvariable=givenAnswer, font=FONT_MAIN, width=10, justify='center', bd=3, relief="groove")
answerEntry.grid(row=2, column=0, pady=10, padx=10)

submitButton = Button(root, text="Submit", font=FONT_NORMAL, bg=COLOR_BTN, fg="white", width=10, command=checkAnswer)
submitButton.grid(row=2, column=1, padx=10)

resultLabel = Label(root, text="", font=FONT_NORMAL, bg=COLOR_BG)
resultLabel.grid(row=3, column=0, columnspan=3, pady=20)

scoreLabel = Label(root, text="Score: 0", font=FONT_NORMAL, bg=COLOR_BG, fg=COLOR_TEXT)
scoreLabel.grid(row=4, column=0, columnspan=3, pady=10)

restartButton = Button(root, text="🔁 Restart", font=FONT_NORMAL, bg="#00695C", fg="white", width=12, command=restart)
restartButton.grid(row=5, column=0, columnspan=3, pady=20)

# Add column spacing
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

generateQuestion()
root.mainloop()
