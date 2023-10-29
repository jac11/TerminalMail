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
            global R   
            global W 
            self.banner ="""     
  ______                                 _ ,__ __          _  
 (_) |                   o              | /|  |  |      o | | 
     |_   ,_    _  _  _      _  _   __, | ||  |  |  __,   | | 
   _ |/  /  |  / |/ |/ | |  / |/ | /  | |/ |  |  | /  | | |/  
  (_/|__/   |_/  |  |  |_|_/  |  |_\_/|_|__|  |  |_\_/|_|_|__/
                          \____/               by:jacstory     
                                                           """
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
                    self.path_attach = os.path.abspath(self.attach) 
                    self.attach_name =  os.path.basename( self.path_attach)   
                    print('[+] Attach File             : '       , self.attach_name )
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
                          print (R+"[*] Email Status            :  Delivered "+W )
                      except Exception:
                             try : 
                                
                                 server = smtplib.SMTP(self.smtp_machine,587,timeout=3)
                                 server.starttls()
                                 server.login(self.user_SMTP,self.auth)                                               
                                 server.sendmail(self.sendder, self.Receive ,self.message)
                                 server.quit()
                                 print (R+"[*] Email Status            :  Delivered "+W )
                                 exit()
                             except Exception:
                                    try : 
                                       
                                        server = smtplib.SMTP(self.smtp_machine,465,timeout=3)
                                        server.starttls()
                                        server.login(self.user_SMTP,self.auth)                                               
                                        server.sendmail(self.sendder, self.Receive ,self.message)
                                        server.quit()
                                        print (R+"[*] Email Status           :  Delivered "+W )
                                        exit()  
                                    except Exception as e :
                                         print (R+"[*] Email Status            : " ,e)
                                         
               else:
               
                   try:
                      
                       server = smtplib.SMTP(self.smtp_machine,25,timeout=3)
                       server.starttls()
                       server.login(self.user_SMTP,self.auth)
                       self.mes.attach(MIMEText(self.body,"plain"))
                       self.mes=self.mes.as_string()
                       server.sendmail(self.sendder, self.Receive,self.mes)
                       server.quit()  
                       print (R+"[*] Email Status            :  Delivered "+W)
                       exit()
                   except Exception : 
                        try :
                            
                            server = smtplib.SMTP(self.smtp_machine,587,timeout=3)
                            server.starttls()
                            server.login(self.user_SMTP,self.auth)
                            self.mes.attach(MIMEText(self.body,"plain"))
                            self.mes=self.mes.as_string()
                            server.sendmail(self.sendder, self.Receive,self.mes)
                            server.quit()  
                            print (R+"[*] Email Status            :  Delivered "+W)
                            exit()
                        except Exception :
                                try :
                                   
                                    server = smtplib.SMTP(self.smtp_machine,465,timeout=3)
                                    server.starttls()
                                    server.login(self.user_SMTP,self.auth)
                                    self.mes.attach(MIMEText(self.body,"plain"))
                                    self.mes=self.mes.as_string()
                                    server.sendmail(self.sendder, self.Receive,self.mes)
                                    server.quit()  
                                    print (R+"[*] Email Status            :  Delivered "+W)
                                    exit()
                                except Exception as e:
                                       print (R+"[*] Email Status             : " ,e)
                                         
           except KeyboardInterrupt:
                  print(self.banner)
                  exit()              
                                          
      def control(self):
    
        parser = argparse.ArgumentParser( description="Usage: [OPtion] [arguments] [OPtion] [argument] ")
        parser.add_argument("-S","--sender"         ,required=True , action=None  ,help = "sendder email account") 
        parser.add_argument("-R","--receive"        ,required=True , action=None  ,help = "receive email acconut ") 
        parser.add_argument("-M","--smtp"           ,required=True, action=None  ,help = "SMTP server sender email ") 
        parser.add_argument("-U","--user"           ,required=True, action=None  ,help = "user name in SMTP server ") 
        parser.add_argument("-A","--authentication" ,required=True, action=None  ,help = "password or api key for user smtp ") 
        parser.add_argument("-s","--subject"        ,required=True, action=None  ,help = "email subject  ")
        parser.add_argument("-m","--massage"        ,action=None  ,help = "email massage  ")
        parser.add_argument("-a","--attach"         ,action=None  ,help = "attach file txt,image..etc")
        
        self.args = parser.parse_args()
        if len(sys.argv)!=1 :
              if self.args.sender:
                 self.sendder = self.args.sender
              if self.args.receive:   
                 self.Receive = self.args.receive
              if self.args.smtp:
                 self.smtp_machine =  self.args.smtp
              if self.args.user:   
                 self.user_SMTP = self.args.user
              if self.args.authentication :
                 self.auth = self.args.authentication
              if self.args.subject:
                 self.subject = self.args.subject
              if self.args.massage :
                 self.body=  self.args.massage
              if self.args.attach:
                 self.attach= self.args.attach   
                                 
        else:
             print(self.banner)          
             parser.print_help()
             exit()
             
      def print_info(self):   
          time.sleep(0.45)
          print()     
          print('[+] From                    : '              ,self.args.sender )
          time.sleep(0.45)
          print('[+] To                      : '              ,self.args.receive )
          time.sleep(0.45)
          print('[+] SMTP Mail Server        : '  ,self.args.smtp )
          time.sleep(0.45)
          print('[+] SMTP Mail User          : '  ,self.args.user )
          time.sleep(0.45)
          print('[+] SMTP authentication     : ',self.args.authentication )
          time.sleep(0.45)
          print('[+] Subject                 : '           ,self.args.subject )
          time.sleep(0.45)
          print('[+] Massage                 : '           ,self.args.massage )
          time.sleep(0.45)         
      def main(self):
          self.print_info()
          self.Messags_heder()
          self.attached_file()
          self.Send_email()
                                                                              
if __name__=='__main__':
     Send_Mail()
