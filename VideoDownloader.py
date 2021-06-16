from tkinter import *
from pytube import YouTube
from wget import *

root = Tk ()                                                
root.geometry('500x300')                                    
root.resizable(0,0)                                         
root.title("Noise Video Downloader")
Label(root,text='Noise Video Downloader',font='arial 15 bold').pack()

link=StringVar()
Label(root,text='Paste Link Here To Download Video',font='arial 10 bold').place(x=160, y=60)
link_e=Entry(root,width=70,textvariable=link).place(x=32,y=90)

def Downloading():
    url= YouTube(str(link.get()))
    video=url.streams.first()
    video.download('F:\Python Projects')
    Label(root,text='DOWNLOADED',font='arial 10 bold').place(x=180,y=210)
Button(root,text='DOWNLOAD',font='arial 10 bold', bg='red',padx=2, command=Downloading).place(x=180,y=150)
root.mainloop()