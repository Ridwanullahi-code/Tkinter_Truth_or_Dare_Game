from tkinter import*
from TruthDare import TruthQuestion,DareQuestion 

def Truth_Dare_Game():
	Display_root()
	Display_widget()
	root.mainloop()

def truth_button():
	text.delete(1.0,END)
	text.insert(END,TruthQuestion())
	
def dare_button():
	text.delete(1.0,END)
	text.insert(END,DareQuestion())

def Display_root():
	global root
	root = Tk()
	root.geometry("835x468+335+172")
	root.resizable(width=NO,height=NO)
			
def Display_widget():
	global text			
	label = Label(root,text="TRUTH OR DARE GAME",bg="white",fg="green",bd=4,relief=GROOVE,font=("Verdana",20,"bold"))
	label.pack(side=TOP,fill="x")
	frame = Frame(root,bg="white")
	frame.place(x=140,y=80,width=550,height=200)
	text = Text(frame,bg="white",font=("Verdana",15,"bold"))
	text.pack(side=LEFT)
	label2 = Label(root,text="TRUTH OR DARE ",bg="white",bd=4,relief=GROOVE,font=("Verdana",18,"bold"))
	label2.place(x=310,y=310)
	truth = Button(root,text="TRUTH",fg="white",bg="Green",bd=3,relief=GROOVE,font=("Verdana",17,"bold"),command=truth_button)
	truth.place(x=250,y=375,width=150)
	dare = Button(root,text="DARE",fg="white",bg="Green",bd=3,relief=GROOVE,font=("Verdana",17,"bold"),command=dare_button)
	dare.place(x=460,y=375,width=150)

print(Truth_Dare_Game())