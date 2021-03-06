from tkinter import *
import tkinter as tk
import time
import RPi.GPIO as io

def asetukset():
    
    io.setwarnings(False)
    io.setmode(io.BCM)
    io.setup(26, io.OUT)
    io.setup(19, io.OUT)
    io.setup(6, io.OUT)
    io.setup(5, io.OUT)
    print("Motors has been set up")

def asetukset_backround():
    t = threading.Thread(target=asetukset)
    t.start()

def function1a():
    io.output(26, io.HIGH)
    io.output(19, io.LOW)
    io.output(6, io.HIGH)
    io.output(5, io.LOW)
    root.after(5000, function1b)
    ##time.sleep(5)
    print ("Eteen")

def function1b():
    io.output(19, io.HIGH)
    io.output(26, io.LOW)
    io.output(6, io.LOW)
    io.output(5, io.HIGH)
    root.after(5000, function1a)
    ##time.sleep(5)

def function1a_background():
    t = threading.Thread(target=function1a)
    t.start()

def function2():
    io.output(26, io.LOW)
    io.output(19, io.HIGH)
    time.sleep(20)
    print ("Kaikki alas")

def function2_backround():
    t = threading.Thread(target=function2)
    t.start()

def function3():
    io.output(26, io.LOW)
    io.output(19, io.LOW)
    io.cleanup()
    print("Lopetettu")

def function3_backround():
    t = threading.Thread(target=function3)
    t.start()

root = Tk()
root.title('Moottorit')

w = 450 # width for the Tk root
h = 500# height for the Tk root

frame = Frame(root, width=w,height =h)
button1 = Button(frame, text = 'Moottori loop', fg='black', command=function1a).grid(row=1,column=1)
button1 = Button(frame, text='Moottori loop', fg='black', command=function1a_background)

button2 = Button(frame, text = 'Kaikki alas',fg='black',command=function2).grid(row=1,column=2)
button2 = Button(frame, text ='Kaikki alas', fg='black',command=function2_backround)

button3 = Button(frame, text = 'Seis', fg='red',command=function3).grid(row=1,column=4)
button3 = Button(frame, text ='Seis', fg='red',command=function3_backround)

button4 = Button(frame, text='Asetukset', fg='black',command=asetukset).grid(row=2,column=1)
button4 = Button(frame, text ='Asetukset', fg='black',command=asetukset_backround)

frame.pack()
root.mainloop()
