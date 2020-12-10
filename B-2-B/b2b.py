import webbrowser
from tkinter import *

window=Tk()

window.title('B_2_B')
window.geometry('450x455')
window.configure(bg='black')
window.resizable(False,False)

instagram_url='https://www.instagram.com'
github_url='https://github.com/M0u1ea5'
leetcode_url='https://leetcode.com/problemset/all'
gmail_url='https://mail.google.com/mail/u/0/#inbox'
linkedin_url='https://www.linkedin.com/feed'
youtube_url='https://www.youtube.com'

def instagram():
    webbrowser.open(instagram_url,new=1)

def github():
    webbrowser.open(github_url,new=2)

def leetcode():
    webbrowser.open(leetcode_url,new=3)
    
def Gmail():
    webbrowser.open(gmail_url,new=4)

def linkedin():
    webbrowser.open(linkedin_url,new=5)
    
def youtube():
    webbrowser.open(youtube_url,new=6)

button=Frame(window,bg='black')
button.pack()

title=StringVar()
title.set('BUTTON_2_BROWSER')
entry=Entry(button,textvariable=title,justify='center',font=('arial',28,'bold'))
entry.pack()

instagram=Button(button,text='INSTAGRAM',font=('arial',15),relief='ridge',bd=1,bg='#ff3333',width=38,height=2,command=instagram)
github=Button(button,text='GITHUB',font=('arial',15),relief='ridge',bd=1,bg='#ff661a',width=38,height=2,command=github)
leetcode=Button(button,text='LEETCODE',font=('arial',15),relief='ridge',bd=1,bg='#7575a3',width=38,height=2,command=leetcode)
Gmail=Button(button,text='G-mail',font=('arial',15),relief='ridge',bd=1,bg='#ffff4d',width=38,height=2,command=Gmail)
Linkedin=Button(button,text='LinkedIN',font=('arial',15),relief='ridge',bd=1,bg='#4d79ff',width=38,height=2,command=linkedin)
youtube=Button(button,text='YOUTUBE',font=('arial',15),relief='ridge',bd=1,bg='#ff3333',width=38,height=2,command=youtube)

entry.grid(row=0,column=0,pady=15)

instagram.grid(row=1,column=0)
github.grid(row=2,column=0)
leetcode.grid(row=3,column=0)
Gmail.grid(row=4,column=0)
Linkedin.grid(row=5,column=0)
youtube.grid(row=6,column=0)


