import tkinter

def hello():
    # print ("hello!!!")
    lab.config(text='123')

root = tkinter.Tk()
root.title("hello")
root.geometry("300x200")#规定程序框的大小。

btn=tkinter.Button(root,text='test',command=hello)
btn.grid(row=0)

lab= tkinter.Label(root,text='',bg='blue')
lab.grid(row=1)


quit=tkinter.Button(root,text='退出！',command=root.quit,fg='red',width='11')
quit.grid(row=3)

root.mainloop()

