from tkinter import *
from pytube import YouTube
import os
import subprocess

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("MP3 - youtube audio downloader")

Label(root,text = 'Youtube Audio Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Вставь ссылку:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)


def Downloader():


	yt = YouTube(str(link.get()))

	videos = yt.streams.get_by_itag(251)

	videos.download()

	in_file = videos.default_filename.split()
	in_file = "-".join(in_file)


	os.rename(videos.default_filename, in_file)

	base, ext = os.path.splitext(in_file)
	out_file = base + '.mp3'




	cmd = "ffmpeg -i " + in_file + ' -vn -ab 128k -ar 44100 -y ' + out_file
	subprocess.run(cmd)
	os.remove(in_file)



	Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(root, text = 'Скачать' , font = 'arial 15 bold' , bg = 'gray', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()