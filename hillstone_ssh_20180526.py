#创建人：jazhu@hillstonenet.com
#输出时间：2018年4月26日
#版本：v0.1
#基于python3.6的环境开发

import paramiko
import time
import os
#import telnellib

#执行show命令
def exec_cmd(cmd_list,log_folder,lic,port,channel):
    for cmd in open(cmd_list):
        print('正在收集'+cmd)

        channel.send(cmd+'\n') #执行命令
        if 'show license' in cmd:#收集lic信息
            for l in lic:
                channel.send('show license '+l+'\n')
        if 'show interface' in cmd: #收集接口的信息
            print('第一次收集端口信息')
            for p1 in port:
                channel.send(p1+'\n')
            time.sleep(5)
            channel.send('\n\n\n\n')
            print('第二次收集端口信息')
            for p2 in port:
                channel.send(p2+'\n')
        time.sleep(2) #歇会
        temp= channel.recv(32768)  #接收输出
        while  not temp.endswith(b'# '):#判断是否接收完毕，注意结尾有空格
            temp+=channel.recv(32768)
        outlog = temp.decode() #程序输出的内容的byte转换str
        #print(temp.decode()) #程序执行过程中打印输出内容
        cmd_name=cmd.replace(' ','-')
        cmd_log=cmd_name.replace('\n','')   
        log=open(log_folder+'/'+cmd_log+'.log','w')
        log.write(outlog)
        print('收集完成!'+'\n')
        print('日志文件存放在：'+log_folder+'/'+cmd_log+'.log')
        print('***********************************\n')
        log.close #关闭写入，养成好习惯


def get_license(channel):
    #获取license的列表
    channel.send('show license\n')
    time.sleep(1)
    lic=channel.recv(32768)
    while not lic.endswith(b'# '):
        lic+=channel.recv(32768)
    liclist=lic.decode().split('\r\n')
    liclist.remove(liclist[0])#移除第一个元素
    liclist.pop()#移除最后一个元素
    lic_name=[]
    for l in liclist:
        if l=='':continue
        lic_temp=l.split('  ')
        lic_name+=[lic_temp[0],]
    return lic_name

def get_interface(channel):
    #获取interface的列表
    channel.send('show interface\n')
    time.sleep(1)
    int_info=channel.recv(32768)
    while not int_info.endswith(b'# '):
        int_info+=channel.recv(32768)
    intlist=int_info.decode().split('\r\n')
    intlist.remove(intlist[0])#移除第一个元素
    intlist.remove(intlist[0])#移除第一个元素
    intlist.remove(intlist[0])#移除第一个元素
    intlist.remove(intlist[0])#移除第一个元素
    intlist.remove(intlist[0])#移除第一个元素
    intlist.remove(intlist[0])#移除第一个元素
    intlist.remove(intlist[0])#移除第一个元素
    intlist.pop()#移除最后一个元素
    intlist.pop()#移除最后一个元素
    int_name=[]
    sc=[]
    for i in intlist:
        if i=='':continue
        if 'U U U' in i:
            if 'ethernet' in i:
                int_temp=i.split('  ')
            else:
                continue
        else:
            continue
        #print(int_temp)     
        #int_name+=[int_temp[0],]
        int_name=int_temp[0]
        #print(int_name)
        sc+=['show controller slot '+int_name[8]+' port '+int_name[10:]+' statistic ',]
    return sc

def login(host,port,username,password,fileuri):
    #连接设备
    print('正在连接设备中...')
    # try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=int(port), username=username, password=password,timeout=30)
    # except:
    #     print('设备登录失败，请检查输入参数！')

    #创建对象，后面就靠这个对象了
    chan = ssh.invoke_shell()
    while not chan.recv_ready():
        time.sleep(1)
    chan.send('terminal length 0\n')    
    chan.send('terminal width 512\n')
    time.sleep(1)
    #循环执行cmd.txt的命令
    temp=''
    out=''
    print('设备登录成功，开始收集日志！')
    print('***********************************\n')
    #预读取内容
    folder=create_logdir(host,chan) #创建日志文件夹
    lic_name=get_license(chan) #获取license信息
    sc=get_interface(chan)
    time.sleep(1)
    exec_cmd('cmd.txt',folder,lic_name,sc,chan)#执行命令
    print('日志收集完成！') 
    input('Press <Enter> to end!')   
    ssh.close() #关闭SSH连接

def create_logdir(hostip,channel):
   
    #从show version中提取出序列号作为本次收集日志的文件夹的名称
    channel.send('show version\n')
    time.sleep(1)
    t= channel.recv(32768)
    tlist=t.decode().split()
    log_folder=tlist[tlist.index('S/N:')+1]+'-'+host_ip #获取sn+ip创建文件夹
    if not os.path.exists('logfile'): 
        os.mkdir('logfile')#创建log文件夹
    log_folder='logfile/'+log_folder
    if not os.path.exists(log_folder): #判断是否存在该文件夹
        os.mkdir(log_folder)#创建存放在log下面的设备日志文件夹
    return log_folder




    
#主程序开始
#输入登录信息
if __name__ == '__main__':
    host_ip=input("plase input host IP(default:192.168.11.10)：") or '192.168.11.10'
    host_port=input("plase input ssh port(default:22) ：") or '22'
    user=input("plase input username(default:hillstone):") or 'hillstone'
    password=input("plase input password(default:hillstone):") or 'hillstone'

    login(host_ip,host_port,user,password)





