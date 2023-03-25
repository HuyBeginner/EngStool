import random
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
import time
import csv

#----------------------------------------kho tu vung ktra----------------------------------
lesson = ''
les_choice = int(input("[1] unit 6 , [2] unit 7 , [3] unit 8: "))
if les_choice == 1:
    lesson = 'unit6.csv'
elif les_choice == 2:
    lesson = 'unit7.csv'
elif les_choice == 3:
    lesson = "unit8.csv"
else:
    exit()

def inp(a):
    interestingrows =[[]]
    key = []
    with open(lesson , encoding = "utf8") as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx == a-1]
        key = interestingrows[0]
        if a == 1:
            key[0] = '1'
    return key
 
def pre_edit(st):
    st = st.strip(' ')
    st = st.strip('\n')
    return st
with open(lesson , encoding = "utf8") as fd:
    reader=csv.reader(fd)
    rowcount= len(list(reader))

reset_file = open("can_hoc_thuoc.txt" , "w" , encoding = "utf-8-sig")
reset_file.write("")

ques_list = random.sample(range(rowcount) , rowcount)
for i in range(0,len(ques_list)):
    ques_list[i] +=1
    
print(ques_list)

mode = 2

screen = Tk()
screen.title("") 
screen.geometry("500x300") 

#-----------------------------------------------main logic------------------------------------
dapantn = Combobox(screen , width = 30 , font="Helvetica 16 bold")
dapantn['state'] = 'readonly'

def generator():
    global ques_num
    ques_inp = inp(ques_list[x])
    ques_raw = map(pre_edit,ques_inp)
    ques_num = list(ques_raw)

def refill():
    if (mode == 0) :
        thutu = random.sample(ques_list,3)
        for i in range(0,len(thutu)):
            thutu[i] = str(thutu[i])
        while ques_num[0] in thutu:
            thutu = random.sample(ques_list,3)
            for i in range(0,len(thutu)):
                thutu[i] = str(thutu[i])

        thutu.append(ques_num[0])    
        random.shuffle(thutu)
        print(thutu)
        print(inp(int(thutu[1])))
        dapanlist = []
        for i in range(4):
            dapanlist.append(inp(int(thutu[i]))[1])

        print(dapanlist)
        dapantuple = tuple(dapanlist)
        dapantn['values'] = dapantuple
         
        
def next_but(): 
    global x

    if x < rowcount:       
        generator()
        refill()
        ques.configure(text = "Từ "+ '"'+ques_num[2] + '" tiếng Anh là gì ?')
        x += 1 
    else:
        exit()
    
    
def submit_but(event):
    global point
    if mode == 1:
        user_ans = typetext.get()
    else:
        user_ans = dapantn.get()
        
    if user_ans == ques_num[1]:
        
        point += 1         
        score.configure(text = str(point)+"/"+str(rowcount))  
        answer.configure(text = "")
    else:
        answer.configure(text = ques_num[1])
        canhoc = open("can_hoc_thuoc.txt" , "a" , encoding = "utf-8-sig")
        canhoc.writelines(ques_num[1]+":"+ques_num[2]+"\n")
        canhoc.close()
    if mode == 1:
        typetext.delete(0,END) 
    next_but() 
    
#------------------------------------------setting--------------------------------------
x = 0
point= 0
passed = 0 

#--------------------------------------------GUI-----------------------------------------

ques = Label(screen , text = "" , font=('Helvetica', 16))


typetext = Entry(screen, width = 30 , font=('Helvetica 16'))

buttonFont = font.Font(family='Helvetica', size=16)

sub = tkinter.Button(screen , text = "Submit" , font=buttonFont)

sub.bind('<Button-1>', submit_but)
screen.bind('<Return>', submit_but)    

next = tkinter.Button(screen, text = "Next >" , command = next_but , font=buttonFont)

answer = Label(screen , text = "" , font=('Helvetica', 16))

score = Label(screen , text = "" , font=('Helvetica', 16))
   
start_label = Label(screen , text = "Choose mode", font=('Helvetica', 16))
start_label.pack()

start_option = Combobox(screen , width = 30 , font="Helvetica 16 bold") 
start_option['value'] = ("Trắc Nghiệm","Tự Luận")
start_option.pack()

def show(k):
    if k == 1:
        next_but()
        ques.pack(padx = 0 , pady = 0)
        if mode == 1:
            typetext.pack(padx = 0 , pady = 0)
            typetext.focus()
        else: 
            dapantn.pack() 
        sub.pack(padx = 0 , pady = 0)
        next.pack(padx = 0 , pady = 0)
        answer.pack(padx = 0, pady = 0)
        score.pack(padx = 0, pady = 0)

appear_sign = "False"
show(0)
def collect():
    global mode
    global appear_sign
    mode = start_option.current()
    appear_sign = "True"
    start_button.destroy()
    start_label.destroy()
    start_option.destroy()
    show(1)
    
start_button = tkinter.Button(screen , text = "Start" , command = collect , font=buttonFont)
start_button.pack()

screen.mainloop()
