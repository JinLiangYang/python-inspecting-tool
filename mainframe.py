import tkinter
# from tkinter import *
from hillstone_ssh_20180526 import *





def hello():
    # print ("hello!!!")
    lab.config(text='123')

root = tkinter.Tk()
root.title("hello")
# root.geometry("280x300")#规定程序框的大小。

#------------------------------------------------------------
lab= tkinter.Label(root,text='设备IP地址：')
lab.grid(row=0,column=0,sticky=tkinter.E)

ipaddress_entry = tkinter.Entry(root)#IP地址的输入框，
ipaddress_entry.grid(row=0,column=1,sticky=tkinter.W)
#------------------------------------------------------------

lab= tkinter.Label(root,text='端口：')
lab.grid(row=1,column=0,sticky=tkinter.E)

# port_entry_text = tkinter.StringVar()
# port_entry_text.set("22")
# port_entry=tkinter.Entry(root,width=7,textvariable=port_entry_text)#端口的输入框，
port_entry=tkinter.Entry(root,width=7,text='22')#端口的输入框，
port_entry.grid(row=1,column=1,sticky=tkinter.W)

lab= tkinter.Label(root,text='（默认为SSH）')
lab.grid(row=1,column=1)

#------------------------------------------------------------


#------------------------------------------------------------
lab= tkinter.Label(root,text='登录账号：')
lab.grid(row=2,column=0,sticky=tkinter.E)

adminuser_entry=tkinter.Entry(root)#账号的输入框，
adminuser_entry.grid(row=2,column=1,sticky=tkinter.W)
#------------------------------------------------------------

#------------------------------------------------------------
lab= tkinter.Label(root,text='登录密码：')
lab.grid(row=3,column=0,sticky=tkinter.E)

password_entry=tkinter.Entry(root)#密码的输入框，
password_entry.grid(row=3,column=1,sticky=tkinter.W)
#------------------------------------------------------------


#------------------------------------------------------------

line_bg=tkinter.Canvas(root,height=16)
line_bg.grid(row=4,columnspan=2)#占2个列宽，

line_bg.create_line(4,10,
                    276,10,
                    fill='gray')
                    # dash=(1,1))     #虚线
#------------------------------------------------------------
lab= tkinter.Label(root,width=16,text='',background='skyblue')
lab.grid(row=5,column=0,sticky=tkinter.E)

# chose_dir_btn=tkinter.Button(root,text='开始转换',command=trans_btnclicked,width='11')
chose_dir_btn=tkinter.Button(root,text='指定报告存放文件夹',width='16')
chose_dir_btn.grid(row=5,column=1,sticky=tkinter.W)

#------------------------------------------------------------

line_bg_mid=tkinter.Canvas(root,width=280,height=16)
line_bg_mid.grid(row=6,columnspan=2)#占2个列宽，

line_bg_mid.create_line(4,10,
                    276,10,
                    fill='gray')
                    # dash=(1,1))     #虚线
#------------------------------------------------------------

lab= tkinter.Label(root,text='当前巡检状态：')
lab.grid(row=7,column=0,sticky=tkinter.E+tkinter.N)

curt_status_text=tkinter.StringVar()
curt_status_text.set("yyyssssssssssssssssssssssssssssssssssssssssssssss")
lab= tkinter.Label(root,textvariable=curt_status_text,width=28,height=8,wraplength=120,bg='floralwhite',anchor='w')
lab.grid(row=7,column=1,sticky=tkinter.W)

#------------------------------------------------------------

line_bg_down=tkinter.Canvas(root,width=280,height=16)
line_bg_down.grid(row=8,columnspan=2)#占2个列宽，

line_bg_down.create_line(4,10,
                    276,10,
                    fill='gray')
                    # dash=(1,1))     #虚线


#------------------------------------------------------------

def begin_btn_cliked():
    # port_entry.
    login(ipaddress_entry.get(),int(port_entry.get()),adminuser_entry.get(),password_entry.get())
    # curt_status_text.se
    pass
    return 0

begin_btn=tkinter.Button(root,text='开始巡检',command=begin_btn_cliked,width='11')
begin_btn.grid(row=20,column=0,sticky=tkinter.E)

quit=tkinter.Button(root,text='退出！',command=root.quit,fg='red',width='11')
quit.grid(row=20,column=1)

#------------------------------------------------------------



root.mainloop()

