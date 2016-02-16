
## brief: a GUI running on client side that download files on the server.


import getfile_thread
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import askokcancel


def onDownload():

   info = getfile_thread.client(content['Server'].get(), int(content['Port'].get()), content['File'].get())

   if not info: 
      showinfo('Error', 'No such file on the server.')
   else:
      showinfo('GetFile', 'Download complete')


def onCancel():

   ans = askokcancel('Verify exit', "Quit?")
   if ans: root.quit()


root = Tk()
root.geometry("430x130")
root.resizable(width=FALSE, height=FALSE)
labels = ['Server', 'Port', 'File']
rownum = 0
content = {}

for label in labels:
   Label(root, text=label, font=30).grid(row=rownum, column=0)
   entry = Entry(root)
   entry.grid(row=rownum, column=1, sticky=E+W)
   content[label] = entry
   rownum += 1

root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

Button(text='Download', command=onDownload, font=15, fg='blue').grid(row=rownum, column=1)
Button(text='Cancel', command=onCancel, font=15, fg='blue').grid(row=rownum+1, column=1)

root.title('GetFile')
root.bind('<Return>', (lambda event: onDownload()))
mainloop()

