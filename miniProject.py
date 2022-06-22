from tkinter import *
from tkinter import messagebox,filedialog
from pygame import mixer
import speech_recognition
from email.message import EmailMessage
import smtplib
import os
import imghdr
import pandas
check=False
def iexit():
    result = messagebox.askyesno('Notification','Confirm if you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def clear():
    toEntryField.delete(0,END)
    subjectEntryField.delete(0,END)
    textarea.delete(1.0,END)


def speak():
    mixer.init()
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            audio=sr.listen(m)
            text=sr.recognize_google(audio)
            textarea.insert(END,text+'')
        except:
            pass

def sendingEmail(toAddress,subject,body):
    f=open('credentials.txt','r')
    for i in f:
        credentials=i.split(',')

    message=EmailMessage()
    message['Subject']=subject
    message['to']=toAddress
    message['from']=credentials[0]
    message.set_content(body)
    if check:
        if filetype=='png' or filetype=='jpg' or filetype=='jpeg':
            f=open(filepath,'rb')
            file_data=f.read()
            subtype=imghdr.what(filepath)

            message.add_attachment(file_data,maintype='image',subtype=subtype,filename=filename)
        else:
            f = open(filepath, 'rb')
            file_data = f.read()
            message.add_attachment(file_data,maintype='image',subtype='octet_stream',filename=filename)

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(credentials[0],credentials[1])
    s.send_message(message)
    x=s.ehlo()
    if x[0]==250:
        return 'sent'
    else:
        return 'failed'


    messagebox.showinfo('Information','Email sent successfully')



def send_email():
    if toEntryField.get=='' or subjectEntryField.get()=='' or textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        if choice.get()=='single':
            result=sendingEmail(toEntryField.get(),subjectEntryField.get(),textarea.get(1.0,END))
            if result=='sent':
                messagebox.showinfo('Success','Email is sent succefully')
            if result=='failed':
                messagebox.showerror('Error','Email has not been sent yet')

        if choice.get()=='multiple':
            sent=0
            failed=0
            for x in final_emails:
                result=sendingEmail(x,subjectEntryField.get(),textarea.get(1.0,END))
                if result=='sent':
                    sent+=1
                if result=='failed':
                    failed+=1
                totalLabel.config(text='')
                sentLabel.config(text='Sent:' + str(sent))
                leftLabel.config(text='Left:'+ str(len(final_emails)-(sent+failed)))
                failedLabel.config(text='Failed:'+ str(failed))

                totalLabel.update()
                sentLabel.update()
                leftLabel.update()
                failedLabel.update()
            messagebox.showinfo('Success','Emails are sent Successfully')



def attachment():
    global filename,filetype,filepath,check
    check=True
    filepath=filedialog.askopenfilename(initialdir='c:/',title='Select File')
    filetype=filepath.split('.')
    filetype=filetype[1]
    filename=os.path.basename(filepath)
    textarea.insert(END,f'\n{filename}\n')


def button_check():
    if choice.get()=='multiple':
        browseButton.config(state=NORMAL)
        toEntryField.config(state='readonly')
    if choice.get=='single':
        browseButton.config(state=DISABLED)
        toEntryField.config(state=NORMAL)
def browse():
    global final_emails
    path=filedialog.askopenfilename(initialdir='c:/',title='Select Excel File')
    if path=='':
        messagebox.showerror('Error','Please select an excel file')
    else:
        data=pandas.read_excel(path)
        if 'Email' in data.columns:
            emails=list(data['Email'])
            final_emails=[]
            for i in emails:
                if pandas.isnull(i)==False:
                    final_emails.append(i)
            if len(final_emails)==0:
                messagebox.showerror('Error','File does not contains any email address')
            else:
                toEntryField.config(state=NORMAL)
                toEntryField.insert(0,os.path.basename(path))
                toEntryField.config(state='readonly')
                totalLabel.config(text='Total:'+str(len(final_emails)))
                sentLabel.config(text='Sent:')
                leftLabel.config(text='Left:')
                failedLabel.config(text='Failed:')


def settings():
    def clear1():
        fromEntryField.delete(0,END)
        passwordEntryField.delete(0,END)

    def save():
        if fromEntryField.get()=='' or passwordEntryField.get=='':
            messagebox.showerror('Error','All fields should be filled ',parent=root1)
        else:
            f=open('credentials.txt','w')
            f.write(fromEntryField.get()+','+passwordEntryField.get())
            f.close()
            messagebox.showinfo('Information','CREDENTIALS SAVED SUCCESSFULLY',parent=root1)

    root1=Toplevel()
    root1.title('Setting')
    root1.geometry('650x340+350+90')


    root1.config(bg='gray26')

    Label(root1,text='Credential Settings',image=logoImage,compound=LEFT,font=('goudy old style',40,'bold'),
          fg='black',bg='honeydew4').grid(padx=60)

    fromLabelFrame = LabelFrame(root1, text='From (Email Address)', font=('times new roman', 16, 'bold'), bd=5, fg='black', bg='gray26')
    fromLabelFrame.grid(row=1, column=0,pady=20)

    fromEntryField = Entry(fromLabelFrame, font=('times new roman', 18, 'bold'), width=30, bg='gray26')
    fromEntryField.grid(row=0, column=0)

    passwordLabelFrame = LabelFrame(root1, text='Password', font=('times new roman', 16, 'bold'), bd=5,
                                fg='black', bg='gray26')
    passwordLabelFrame.grid(row=2, column=0, pady=20)

    passwordEntryField = Entry(passwordLabelFrame, font=('times new roman', 18, 'bold'), width=30, bg='gray26',show='*')
    passwordEntryField.grid(row=0, column=0)

    Button(root1,text="Save",font=('times new roman',18,'bold'),cursor='hand2',bg='gold2',
           fg='black',command=save).place(x=210,y=280)

    Button(root1, text="Clear", font=('times new roman', 18, 'bold'), cursor='hand2', bg='gold2',
           fg='black',command=clear1).place(x=340, y=280)
    f=open('credentials.txt','r')
    for i in f:
        credentials=i.split(',')
    fromEntryField.insert(0,credentials[0])
    passwordEntryField.insert(0,credentials[1])





    root1.mainloop()




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
Button(titleFrame,image=settingImage,bd=0,bg='honeydew4',cursor='hand2',activebackground='honeydew4'
       ,command=settings).grid(row=0,column=1,padx=20)

chooseFrame=Frame(root,bg='gray26')
chooseFrame.grid(row=1,column=0,pady=10)

choice=StringVar()


singleRadioButton=Radiobutton(chooseFrame,text='Single',font=('times new roman',25,'bold'),
                              variable=choice,value='single',bg='gray26',activebackground='gray26',command=button_check)
singleRadioButton.grid(row=0,column=0,padx=10)
multipleRadioButton=Radiobutton(chooseFrame,text='Multiple',font=('times new roman',25,'bold'),
                              variable=choice,value='multiple',bg='gray26',activebackground='gray26',
                                command=button_check)
multipleRadioButton.grid(row=0,column=1,padx=10)
choice.set('single')

toLabelFrame=LabelFrame(root,text='To (Email Address)',font=('times new roman',16,'bold'),bd=5,fg='black',bg='gray26')
toLabelFrame.grid(row=2,column=0,padx=140)

toEntryField=Entry(toLabelFrame,font=('times new roman',18,'bold'),width=30,bg='gray26')
toEntryField.grid(row=0,column=0)


browseImage=PhotoImage(file='browse.png')
browseButton=Button(toLabelFrame,text=' Browse',image=browseImage,compound=LEFT,font=('arial',12,'bold'),bg='honeydew4',activebackground='honeydew4',cursor='hand2',bd=0,state=DISABLED,command=browse)
browseButton.grid(row=0,column=1,padx=20)


subjectLableFrame=LabelFrame(root,text='Subject',font=('times new roman',16,'bold'),bd=5,fg='black',bg='gray26')
subjectLableFrame.grid(row=3,column=0,padx=140,pady=10)

subjectEntryField=Entry(subjectLableFrame,font=('times new roman',18,'bold'),width=30,bg='gray26')
subjectEntryField.grid(row=0,column=0)


emailLableFrame=LabelFrame(root,text='Compose Email',font=('times new roman',16,'bold'),bd=5,fg='black',bg='gray26')
emailLableFrame.grid(row=4,column=0)


micImage=PhotoImage(file='mic.png')
Button(emailLableFrame,text=' Speak',image=micImage,compound=LEFT,font=('arial',12,'bold'),bg='honeydew4',activebackground='honeydew4',cursor='hand2',bd=0
       ,command=speak).grid(row=0,column=0)

attachImage=PhotoImage(file='attachments.png')
Button(emailLableFrame,text=' Attachments',image=attachImage,compound=LEFT,font=('arial',12,'bold'),bg='honeydew4',activebackground='honeydew4',cursor='hand2',bd=0,
       command=attachment).grid(row=0,column=1)


textarea=Text(emailLableFrame,font=('times new roman',14),height=8,bg='gray26',bd=3)
textarea.grid(row=1,column=0,columnspan=2)

sendImage=PhotoImage(file='send.png')
Button(root,image=sendImage,compound=LEFT,font=('arial',12,'bold'),bg='gray26',activebackground='gray26',cursor='hand2',bd=0,
      command=send_email ).place(x=490,y=545)

clearImage=PhotoImage(file='clear.png')
Button(root,image=clearImage,compound=LEFT,font=('arial',12,'bold'),bg='gray26',activebackground='gray26',cursor='hand2',bd=0
       ,command=clear).place(x=590,y=550)

exitImage=PhotoImage(file='exit.png')
Button(root,image=exitImage,compound=LEFT,font=('arial',12,'bold'),bg='gray26',activebackground='gray26',cursor='hand2',bd=0
       ,command=iexit).place(x=690,y=550)

totalLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
totalLabel.place(x=10,y=560)


sentLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
sentLabel.place(x=100,y=560)

sentLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
sentLabel.place(x=190,y=560)

leftLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
leftLabel.place(x=280,y=560)


failedLabel=Label(root,font=('times new roman',18,'bold'),bg='gray26',fg='black')
failedLabel.place(x=350,y=560)



root.mainloop()