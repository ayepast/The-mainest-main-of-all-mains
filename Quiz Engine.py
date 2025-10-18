
from tkinter import * ## Gui


window = Tk()
window.title("mega super duper ultra best python mega quiz") ## The best title of the year
window.geometry('1500x500') 



Generation = [ 
    {
     1:"Question",
     2:"Answ1",
     3:"Answ2",
     4:"Answ3", ## Right answer, change the fifth variable from 4 to answer thats right
     5:4  ## Right answer that graints a point (Current answer 3)
     }, ## Get rid of that text, duplicate this table to make second question 
    
]



curQuiz = 1 ## Dont change either if you want to your quiz start with the second question and skip first

quizNum = Label(window,text="Вопрос  " + str(curQuiz),)
quizNum.grid(column=0,row=0)

question = Label(window,text="",font=("Arial",20))
question.grid(column=0,row=1)

corrects = 0
maxcorrects = 1 ## WARNING!!!!!! THE ULTRA MEGA BEST VARIABLE!!!!!! THE QUANTITY OF ALL QUESTIONS

def Change(quiz,init):
    global corrects
    global curQuiz
    global Generation
    

    try:
        main = Generation[quiz - 1]
        
        

        curQuest = main[1]

        answ1 = main[2]
        answ2 = main[3]
        answ3 = main[4]
        quizNum.config(text="Question N " + str(quiz)) ## WARNING!!!!!! THE SECOND ULTRA MEGA BEST VARIABLE!!!!!! THE "...... N 1" EITHER THE NAME OF THE QUESTION
        question.config(text=curQuest)
        answer1.config(text=answ1)
        answer2.config(text=answ2)
        answer3.config(text=answ3)
    except:
        quizNum.config(text="Congratulations!")
        result = round(corrects / maxcorrects * 5)
        
        question.config(text="Your score is: " + str(result) + "  ( " + str(corrects) + " / " + str(maxcorrects) + " )")

        answer1.config(state="disabled")
        answer2.config(state="disabled")
        answer3.config(state="disabled")

        answer1.config(text="Just dont")
        answer2.config(text="look")
        answer3.config(text="here")

def butt1Touched():


    global curQuiz
    global corrects
    specular = Generation[curQuiz - 1]
    
    if specular[5] == 2:
        corrects += 1
        print('sec')
        

    curQuiz += 1
    Change(curQuiz,1)
    
def butt2Touched():
    global curQuiz
    global corrects
    specular = Generation[curQuiz - 1]
    
    if specular[5] == 3:
        corrects += 1
        print('sec')
        
    curQuiz += 1
    Change(curQuiz,2)
    
def butt3Touched():
    global curQuiz
    global corrects
    specular = Generation[curQuiz - 1]
    
    if specular[5] == 4:
        corrects += 1
        print('sec')
        
    curQuiz += 1
    Change(curQuiz,3)
    



answer1 = Button(window,text="",command= butt1Touched,font=("Arial",15))
answer1.grid(column=0,row=2)
answer2 = Button(window,text="",command= butt2Touched,font=("Arial",15))
answer2.grid(column=0,row=3)
answer3 = Button(window,text="",command= butt3Touched,font=("Arial",15))
answer3.grid(column=0,row=4)

Change(1,24)

window.mainloop()
