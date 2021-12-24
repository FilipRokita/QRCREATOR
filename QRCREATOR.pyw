#QRCREATOR
#Filip Rokita
#www.filiprokita.com

#import
import qrcode
import PIL
import tkinter as tk

#def
def qrcreate():
    qrValue = qrVar.get()
    qrOutput = qrcode.make(qrValue)
    qrOutput.save('QRCREATOR.png')

#main
if __name__ == '__main__':
    root = tk.Tk()
    root.title('QRCREATOR')
    root.geometry('300x150')
    root.resizable(False, False)

    qrVar = tk.StringVar()

    qrL = tk.Label(root, text='INPUT'); qrL.pack()
    qrE = tk.Entry(root, textvariable=qrVar, justify=tk.CENTER, width=30); qrE.pack()
    generateB = tk.Button(root, text='CREATE', command=qrcreate, width=15); generateB.pack(pady=10)
    authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack()

    root.mainloop()