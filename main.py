from tkinter import *

root=Tk()
root.title("Multiple Email Sender App")
root.geometry('780x620+100+50')
root.resizable(0, 0)
root.config(bg='gray26')


titleFrame=Frame(root, bg='honeydew4')
titleFrame.grid(row=0, column=0)


logoImage=PhotoImage(file='email.png')
titleLabel=Label(titleFrame, text='   Multiple Email Sender', image=logoImage, compound=LEFT,font=('Goudy Old Style', 28, 'bold') ,
                 bg='honeydew4', fg='gray26')
titleLabel.grid(row=0, column=0)

settingImage=PhotoImage(file='setting.png')
Button(titleFrame,image=settingImage,bd=0,bg='honeydew4',cursor='hand2',activebackground='honeydew4').grid(row=0,column=1,padx=20)

chooseFrame=Frame(root,bg='gray26')
chooseFrame.grid(row=1,column=0,pady=10)

singleVariable=StringVar()
multipleVariable=StringVar()


singleRadioButton=Radiobutton(chooseFrame,text='Single',font=('times new roman',25,'bold'),
                              variable=singleVariable,value='single',bg='gray26',activebackground='gray26')
singleRadioButton.grid(row=0,column=0,padx=10)
multipleRadioButton=Radiobutton(chooseFrame,text='Multiple',font=('times new roman',25,'bold'),
                              variable=multipleVariable,value='multiple',bg='gray26',activebackground='gray26')
multipleRadioButton.grid(row=0,column=1,padx=10)

toLabelFrame=LabelFrame(root,text='To (Email Address)',font=('times new roman',16,'bold'),bd=5,fg='black',bg='gray26')
toLabelFrame.grid(row=2,column=0,padx=140)

toEntryField=Entry(toLabelFrame,font=('times new roman',18,'bold'),width=30,bg='gray26')
toEntryField.grid(row=0,column=0)


browseImage=PhotoImage(file='browse.png')
Button(toLabelFrame,text=' Browse',image=browseImage,compound=LEFT,font=('arial',12,'bold'),bg='honeydew4',activebackground='honeydew4',cursor='hand2',bd=0).grid(row=0,column=1,padx=20)


subjectLableFrame=LabelFrame(root,text='Subject',font=('times new roman',16,'bold'),bd=5,fg='black',bg='gray26')
subjectLableFrame.grid(row=3,column=0,padx=140,pady=10)

subjectEntryField=Entry(subjectLableFrame,font=('times new roman',18,'bold'),width=30,bg='gray26')
subjectEntryField.grid(row=0,column=0)


emailLableFrame=LabelFrame(root,text='Compose Email',font=('times new roman',16,'bold'),bd=5,fg='black',bg='gray26')
emailLableFrame.grid(row=4,column=0)


micImage=PhotoImage(file='mic.png')
Button(emailLableFrame,text=' Speak',image=micImage,compound=LEFT,font=('arial',12,'bold'),bg='honeydew4',activebackground='honeydew4',cursor='hand2',bd=0).grid(row=0,column=0)

attachImage=PhotoImage(file='attachments.png')
Button(emailLableFrame,text=' Attachments',image=attachImage,compound=LEFT,font=('arial',12,'bold'),bg='honeydew4',activebackground='honeydew4',cursor='hand2',bd=0).grid(row=0,column=1)


textarea=Text(emailLableFrame,font=('times new roman',14),height=8,bg='gray26',bd=3)
textarea.grid(row=1,column=0,columnspan=2)

sendImage=PhotoImage(file='send.png')
Button(root,image=sendImage,compound=LEFT,font=('arial',12,'bold'),bg='gray26',activebackground='gray26',cursor='hand2',bd=0).place(x=490,y=545)

clearImage=PhotoImage(file='clear.png')
Button(root,image=clearImage,compound=LEFT,font=('arial',12,'bold'),bg='gray26',activebackground='gray26',cursor='hand2',bd=0).place(x=590,y=550)

exitImage=PhotoImage(file='exit.png')
Button(root,image=exitImage,compound=LEFT,font=('arial',12,'bold'),bg='gray26',activebackground='gray26',cursor='hand2',bd=0).place(x=690,y=550)

totalLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
totalLabel.place(x=10,y=560)


sentLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
sentLabel.place(x=100,y=560)

sentLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
sentLabel.place(x=190,y=560)


failedLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
failedLabel.place(x=280,y=560)


root.mainloop()