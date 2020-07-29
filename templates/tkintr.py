from tkinter import*
from PIL import ImageTk, Image
import os


root=Tk()

def send():
    send="you->"+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"BOT->Hey!!How can i help you")
    elif(e.get()=="Tell me something about yourself"):
        txt.insert(END,"\n"+"BOT->A chatbot is a computer program that's designed to simulate human conversation. Users communicate with these tools using a chat interface or via voice, just like they would converse with another person. Chatbots interpret the words given to them by a person and provide a pre-set answer")
    elif(e.get()=="example of chatbot!!"):
        txt.insert(END,"\n"+"BOT->chatbot example is 1800Flowers. The flower-delivery company has created a Facebook messenger chatbot. ... Users can order flowers and have them delivered in a breeze.") 
    elif(e.get()=="Glad to hear about this"):
        txt.insert(END,"\n"+"BOT->Thanks")
    else:
        txt.insert(END,"\n"+"BOT->Sorry I didn't get you!!")          
    e.delete(0,END)
    
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)

img = ImageTk.PhotoImage(Image.open("download.gif"))
panel = Label(txt, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

e=Entry(root,width=100)
e['background']='green'
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Chatbot :-) Ask your Query")


root.mainloop()