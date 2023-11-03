#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart    
from email.mime.base import MIMEBase
from email import encoders
import deprecated
import time 
import os 
import argparse
import sys

R='\033[31m' 
W='\033[0m' 

class Send_Mail():
         
         
      def __init__(self): 

            self.banner =R+"""     
  ______                                 _ ,__ __          _  
 (_) |                   o              | /|  |  |      o | | 
     |_   ,_    _  _  _      _  _   __, | ||  |  |  __,   | | 
   _ |/  /  |  / |/ |/ | |  / |/ | /  | |/ |  |  | /  | | |/  
  (_/|__/   |_/  |  |  |_|_/  |  |_\_/|_|__|  |  |_\_/|_|_|__/
                          \____/               by:jacstory     
                                                           """+W
            print(self.banner)
            self.control()
            self.main() 
                
      def Messags_heder(self) :
           self.mes = MIMEMultipart()
           self.mes["From"]= self.sendder
           self.mes["To"]= self.Receive
           self.mes["subject"] = self.subject
           
      def attached_file(self):

           try:
              try:
                 if self.args.attach :
                    self.mes.attach(MIMEText(self.body,"plain"))
                    self.path_attach = os.path.abspath(self.attach) 
                    self.attach_name =  os.path.basename( self.path_attach)   
                    print('📌️ Attach File             : '       , self.attach_name )
                    file_atta = open(self.path_attach ,'rb')    
                    get = MIMEBase("application","octet-stream")
                    get.set_payload((file_atta).read())
                    encoders.encode_base64(get)
                    file_name = self.attach_name
                    get.add_header("content-Disposition","file_atta ;filename ="+file_name)
                    self.mes.attach(get)
                    self.message= self.mes.as_string() 
              except IOError :
                    print (R+"[*] No such file or directory", self.path_attach+R)
                    print (self.banner)
                    exit()       
           except KeyboardInterrupt:
                    print(self.banner)
                    exit() 
                                
      def Send_email(self):
           try:
               if self.args.attach :
                      try : 
                        
                          server = smtplib.SMTP(self.smtp_machine,25 ,timeout=3)
                          server.starttls()
                          server.login(self.user_SMTP,self.auth)                                               
                          server.sendmail(self.sendder, self.Receive ,self.message)
                          server.quit()
                          print (R+"📬️ Email Status            :  Delivered "+W )
                      except Exception:
                             try : 
                                 server = smtplib.SMTP(self.smtp_machine,587,timeout=3)
                                 server.starttls()
                                 server.login(self.user_SMTP,self.auth)                                               
                                 server.sendmail(self.sendder, self.Receive ,self.message)
                                 server.quit()
                                 print (R+"📬️ Email Status            :  Delivered "+W )
                                 exit()
                             except Exception:
                                    try : 
                                       
                                        server = smtplib.SMTP(self.smtp_machine,465,timeout=3)
                                        server.starttls()
                                        server.login(self.user_SMTP,self.auth)                                               
                                        server.sendmail(self.sendder, self.Receive ,self.message)
                                        server.quit()
                                        print (R+"📬️ Email Status           :  Delivered "+W )
                                        exit()  
                                    except Exception as e :
                                         print (R+"📭️ Email Delivery Failure  : " ,e)
                                         
               else:
               
                   try:
                      
                       server = smtplib.SMTP(self.smtp_machine,25,timeout=3)
                       server.starttls()
                       server.login(self.user_SMTP,self.auth)
                       if self.args.html and self.args.format:
                          self.mes.attach(MIMEText(self.body,"plain"))
                          with open('HTML.HTML','r') as readHTML :
                               html = readHTML.read()
                          self.mes.attach(MIMEText(html,"html"))
                       else:   
                          self.mes.attach(MIMEText(self.body,"plain"))
                       self.mes=self.mes.as_string()
                       server.sendmail(self.sendder, self.Receive,self.mes)
                       server.quit()  
                       print (R+"📬️ Email Status            :  Delivered "+W)
                       exit()
                   except Exception : 
                        try :
                            
                            server = smtplib.SMTP(self.smtp_machine,587,timeout=3)
                            server.starttls()
                            server.login(self.user_SMTP,self.auth)
                            if self.args.html and self.args.format:
                                self.mes.attach(MIMEText(self.body,"plain"))
                                with open('HTML.HTML','r') as readHTML :
                                    html = readHTML.read()
                                self.mes.attach(MIMEText(html,"html"))
                            else:   
                                self.mes.attach(MIMEText(self.body,"plain"))
                            self.mes=self.mes.as_string()
                            server.sendmail(self.sendder, self.Receive,self.mes)
                            server.quit()  
                            print (R+"📬️ Email Status            :  Delivered "+W)
                            exit()
                        except Exception :
                                try :
                                   
                                    server = smtplib.SMTP(self.smtp_machine,465,timeout=3)
                                    server.starttls()
                                    server.login(self.user_SMTP,self.auth)
                                    if self.args.html and self.args.format:
                                       self.mes.attach(MIMEText(self.body,"plain"))
                                       with open('HTML.HTML','r') as readHTML :
                                           html = readHTML.read()
                                       self.mes.attach(MIMEText(html,"html"))
                                    else:   
                                        self.mes.attach(MIMEText(self.body,"plain"))
                                    self.mes=self.mes.as_string()
                                    server.sendmail(self.sendder, self.Receive,self.mes)
                                    server.quit()  
                                    print (R+"📬️ Email Status            :  Delivered "+W)
                                    exit()
                                except Exception as e:
                                       print (R+"📭️ Email Delivery Failure  : " ,e)
                                         
           except KeyboardInterrupt:
                  print(self.banner)
                  exit()              
                                          
      def control(self):
    
        parser = argparse.ArgumentParser( description="Usage: [OPtion] [arguments] [OPtion] [argument] ")
        parser.add_argument("-S","--sender"         , action=None  ,help = "sendder email account") 
        parser.add_argument("-R","--receive"        , action=None  ,help = "receive email acconut ") 
        parser.add_argument("-M","--smtp"           , action=None  ,help = "SMTP server sender email ") 
        parser.add_argument("-U","--user"           , action=None  ,help = "user name in SMTP server ") 
        parser.add_argument("-A","--authentication" , action=None  ,help = "password or api key for user smtp ") 
        parser.add_argument("-a","--attach"         ,action=None   ,help = "attach file txt,image..etc")
        parser.add_argument("-p","--post"           ,action=None   ,help = "read Message body form file")
        parser.add_argument("-C","--config"         ,action=None   ,help = "read Configroution for file")
        parser.add_argument("--html"                ,action='store_true'   ,help = "send Html mail Format")
        parser.add_argument("-F","--format"         ,action=None    ,help = "path of the html page ")
        self.args = parser.parse_args()
        if len(sys.argv)!=1 :
          if self.args.config:
                  with open(self.args.config,'r') as Config:
                      Config         = Config.readlines()
                  self.sendder       = str(Config[0]).replace('\n','').strip()
                  self.Receive       = str(Config[1]).replace('\n','').strip()
                  self.smtp_machine  = str(Config[2]).replace('\n','').strip()
                  self.user_SMTP     = str(Config[3]).replace('\n','').strip()
                  self.auth          = str(Config[4]).replace('\n','').strip()
                  self.subject       = str(input("📧️ Enter Email Subject : "))
                  if self.args.attach:
                      self.attach = self.args.attach    
                  if self.args.post:
                      with open(self.args.post,'r') as postmes:
                          self.body = postmes.read()
                          self.path_Mes = os.path.abspath(self.args.post) 
                          self.mes_name =  os.path.basename( self.path_Mes)       
                  else:         
                      self.body = str(input("📝️ Enter Email Message : "))  
                  print('='*30)       
          else:
                if self.args.sender:
                   self.sendder = self.args.sender
                else:
                    print("usage: terminalmail.py [-h] -S SENDER [-R RECEIVE] [-M SMTP] [-U USER] [-A AUTHENTICATION]"
                        +"[-a ATTACH] [-p POST] [-C CONFIG] [--html] [-F FORMAT]"+'\n'+
                        "terminalmail.py: error: the following arguments are required: -S/--sender")
                    exit()
                if self.args.receive:   
                   self.Receive = self.args.receive
                else:
                    print("usage: terminalmail.py [-h] -S SENDER [-R RECEIVE] [-M SMTP] [-U USER] [-A AUTHENTICATION]"
                         +"[-a ATTACH] [-p POST] [-C CONFIG] [--html] [-F FORMAT]"+'\n'+
                        "terminalmail.py: error: the following arguments are required: -R/--receive")
                    exit()
                if self.args.smtp:
                   self.smtp_machine =  self.args.smtp
                else:
                    print("usage: terminalmail.py [-h] -S SENDER [-R RECEIVE] [-M SMTP] [-U USER] [-A AUTHENTICATION]"
                        +"[-a ATTACH] [-p POST] [-C CONFIG] [--html] [-F FORMAT]"+'\n'+
                        "terminalmail.py: error: the following arguments are required: -M/--smtp")
                    exit()
                if self.args.user:   
                 self.user_SMTP = self.args.user
                else:   
                    print("usage: terminalmail.py [-h] -S SENDER [-R RECEIVE] [-M SMTP] [-U USER] [-A AUTHENTICATION]"
                        +"[-a ATTACH] [-p POST] [-C CONFIG] [--html] [-F FORMAT]"+'\n'+
                        "terminalmail.py: error: the following arguments are required: -U/--user")
                    exit()
                if self.args.authentication :
                   self.auth = self.args.authentication
                else:
                    print("usage: terminalmail.py [-h] -S SENDER [-R RECEIVE] [-M SMTP] [-U USER] [-A AUTHENTICATION]"
                        +"[-a ATTACH] [-p POST] [-C CONFIG] [--html] [-F FORMAT]"+'\n'+
                        "terminalmail.py: error: the following arguments are required: -A/--authentication")
                    exit()
                if self.args.attach:
                   self.attach = self.args.attach   
                self.subject   = str(input("📧️ Enter Email Subject : "))
                if self.args.post:
                   with open(self.args.post,'r') as postmes:
                       self.body = postmes.read()
                   self.path_Mes = os.path.abspath(self.args.post) 
                   self.mes_name =  os.path.basename( self.path_Mes)     
                elif self.args.html:
                    self.body      = str(input("📝️ Enter Email Message : "))  
                else:         
                    self.body      = str(input("📝️ Enter Email Message : "))     
                print('='*30)               
        else:
             print(self.banner)          
             parser.print_help()
             exit()

      def print_info(self):   
            time.sleep(0.45)
            print()     
            print('🪧️ From                    : ',self.sendder.strip())
            time.sleep(0.45)
            print('🪪️ To                      : ',self.Receive.strip())
            time.sleep(0.45)
            print('🖥️  SMTP Mail Server        : ',self.smtp_machine.strip())
            time.sleep(0.45)
            print('👤️ SMTP Mail User          : ',self.user_SMTP.strip() )
            time.sleep(0.45)
            print('🔏️ SMTP authentication     : ',self.auth.strip())
            time.sleep(0.45)
            print('📰️ Subject                 : ',self.subject.strip())
            time.sleep(0.45)
            if self.args.post:
               print('🧾️ Message File       : ',self.mes_name.strip())
               time.sleep(0.45)  
            elif self.args.html:
                 print('🧾️ Message                 : ',self.body.strip())
                 print('💼️ Email Type              :  HTML Format')  
            else:       
                 print('🧾️ Message              : ',self.body.strip())
                 time.sleep(0.45)         
      def main(self):
          self.print_info()
          self.Messags_heder()
          self.attached_file()
          self.Send_email()
                                                                              
if __name__=='__main__':
     Send_Mail()

