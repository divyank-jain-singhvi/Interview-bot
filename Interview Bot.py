import pyttsx3
import speech_recognition as sr
from tkinter import *
import random
import matplotlib.pyplot as plt
import csv
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

z=0
y = 'M'
question_label = None
num=1
text='CLICK ON READY TO START YOUR PRACTICE INTERVIEW SESSION'
xrange = []
below50 = 0
above50 = 0
equal0 = 0
def question_input():
    global y,num,xrange,ques,y_pos, corr,z,below50,above50,equal0
    questions = []
    keywords = []
    ques = []
    corr = []
    keyword_list2 = []
    below50 = 0
    above50 = 0
    equal0 = 0
    z=0
    
    recognizer = sr.Recognizer()
    
    while z != num:
        with open("Interview Question Dataset - Sheet1.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                questions.append(row[0])
                keywords.append(row[1])

        x = random.randint(0, len(questions) - 1)  
        question = questions[x]
        keyword = keywords[x]
        keyword = keyword.lower()
        print(question)
        Speak(question)
        
        text_label=question_label.config(text=question,font=('Arial',20))
        
        print(keyword)
        print("What is your answer to the question?")
        Speak("What is your answer to the question?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source, phrase_time_limit=5)
     
        try:
            answer = recognizer.recognize_google(audio)
            answer = answer.lower()
            print("Your answer is:", answer)
        except sr.UnknownValueError:
            answer = 'dont know'
            print("It's ok try your best in your next answer")
            Speak("It's ok try your best in your next answer")
        
        keyword_list = keyword.split(',')
        matches = []
        match_count = 0
        
        for i in keyword_list:
            i = i.strip()
            keyword_list2.append(i)
            if i in answer:
                matches.append(i)
                print(i)
                match_count += 1
        
        if match_count > 0:
            print("Great! You answered questions correctly. Keyword matches =", match_count)
            Speak(f'Great! You answered questions correctly. Keyword matches={match_count}')
            if len(keyword_list) > match_count:
                print('Missed Keywords is:', set(keyword_list2) - set(matches))
        else:
            print("You didn't answer questions correctly. Here are the keywords you missed:", set(keyword_list))
            Speak(f"You didn't answer questions correctly. Here are the keywords you missed: {set(keyword_list)}")
        
        z += 1
        ques.append(question)
        corr.append(match_count)
        xrange.append(len(keyword_list))
        keyword_list2 = []
        
        if 0 < ((match_count) / len(keyword_list)) * 100 <= 50:
            below50 += 1
        elif ((match_count) / len(keyword_list)) * 100 > 50:
            above50 += 1
        else:
            equal0 += 1
        
        if y == 'M':
            y = 'F'
        elif y == 'F':
            y = 'M'
        
    all_fontsize = 12
    width = 1
    bar_color = 'green'
    
    plt.xlabel('Keywords Matched')
    plt.ylabel('Questions')
    plt.title("Number of keywords matched according to your answer")
    plt.xlim([0, int(max(xrange) + 2)])
    y_pos = [i * (width + .5) for i in range(len(ques))]
    plt.barh(y_pos, corr, height=width, color=bar_color)
    plt.yticks(y_pos, ques)
    plt.show()
    
    # below50 = (below50 / num) * 100
    # above50 = (above50 / num) * 100
    # equal0 = (equal0 / num) * 100
    
    pie_edgecolor = 'black'
    pie_lable = ['below 50 \n need to work on questions', 'above 50 excellent', 'equal to 0 poor']
    pie_list = [abs(below50), abs(above50), abs(equal0)]
    pie_colors = ['yellow', 'green', 'blue']
    plt.pie(pie_list, shadow=True, explode=[0, .2, 0], colors=pie_colors, startangle=-90, labels=pie_lable,wedgeprops={'edgecolor': pie_edgecolor}, textprops={"fontsize": all_fontsize})
    plt.show()


def question1():
    
    thread = threading.Thread(target=question_input)
    thread.start()

def Speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    
    if y == 'M':
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM')
    elif y == 'F':
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    
    engine.setProperty('rate', 140)
    engine.say(audio)
    engine.runAndWait()
    
def graph():
    global canvas,below50,above50,equal0,num,canvas1
    
    width = 1
    bar_color = 'purple'
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('Keywords Matched')
    ax.set_ylabel('Questions')
    ax.set_title("Number of keywords matched according to your answer")
    ax.set_xlim([0, int(max(xrange))])
    y_pos = [i * (width + .5) for i in range(len(ques))]
    ax.barh(y_pos, corr, height=width, color=bar_color)
    ax.set_yticks(y_pos, ques)
    plt.show()
    canvas = FigureCanvasTkAgg(fig, master=screen)
    canvas.draw()
    canvas.get_tk_widget().config(width=550,height=270)
    canvas.get_tk_widget().pack()

    
    all_fontsize = 12
    pie_edgecolor = 'black'
    pie_lable = ['below 50 \n need to work on questions', 'above 50 excellent', 'equal to 0 poor']
    pie_colors = ['yellow', 'green', 'blue']
    below50 = (below50 / num) * 100
    above50 = (above50 / num) * 100
    equal0 = (equal0 / num) * 100
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    
    pie_list = [abs(below50), abs(above50), abs(equal0)]
    ax.pie(pie_list, shadow=True, explode=[0, .2, 0], colors=pie_colors, startangle=-90, labels=pie_lable,wedgeprops={'edgecolor': pie_edgecolor}, textprops={"fontsize": all_fontsize})
    plt.show()
    canvas1 = FigureCanvasTkAgg(fig, master=screen)
    canvas1.draw()
    canvas1.get_tk_widget().config(width=550,height=270)
    canvas1.get_tk_widget().pack()
    
def clear_graph():
    global z,num,canvas,canvas1
    if z==num:
        canvas.get_tk_widget().pack_forget()
        canvas1.get_tk_widget().pack_forget()
        del canvas
        del canvas1
        

answers = []
screen = Tk()
screen.title("Interview Bot")
screen.geometry("1200x650")
bg = PhotoImage(file="interview1.png")

label1 = Label(screen, image=bg)
label1.place(x=0, y=0, width=1200, height=650)
def thread_start():
    
    thread3 = threading.Thread(target=question1)
    
    thread2 = threading.Thread(target=clear_graph)
    thread2.start()
    thread3.start()
    


ready_img = PhotoImage(file="ready1.png")
ready = Button(text="ready", command=thread_start, image=ready_img, borderwidth=2)
ready.place(x=529, y=613, width=140, height=27)

try:
    button= Button(text= "Result", command= graph)
    button.place(x=1100,y=550)
except:
    text='after interview you can see graph'

question_label = Label(screen, text=text, font=("Arial", 12))
question_label.place()
question_label.pack(padx=50,pady=10)

screen.mainloop()
