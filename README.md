# TerminalMail

TerminalMail is a command-line tool that allows you to send emails from your terminal, supporting both plain text and HTML emails, with or without attachments. Whether you need to send a quick message or a beautifully formatted HTML email with attachments, TerminalMail has you covered.
## Features
  * Send plain text emails. 
  * Send HTML emails with custom styling.
  * Attach files to your emails.
  * Send emails from your command line.
  * Detect open ports on a target server.
## Installation
 * git clone https://github.com/jac11/TerminalMail.git
 * cd  TerminalMail
 * chmod +x terminalmail.py
 * terminalmail.py -h
   ```
    -S or --sender: Specify the sender's email account.
    -R or --receive: Specify the recipient's email account.
    -M or --smtp: Specify the SMTP server for the sender's email.
    -U or --user: Specify the username used for authentication with the SMTP server.
    -A or --authentication: Provide the password or API key for user authentication with the SMTP server.
    -a or --attach: Attach a file to the email. You can attach various file types (e.g., text, image).
    -p or --post: Read the message body from a file.
    -C or --config: Read configuration from a file.
    --html: Send the email in HTML format.
    -F or --format: Specify the path of the HTML page.
   ```
## encryption 
* TerminalMail use SSL in port 465 or  SLT in port 587 to encryption the server login you heve to select the encryption type 
## TerminalMail attachment
* smtp_email.py allow to attach file 
* attach singel file not multiple  file
* to attach file you change the current working directory same like /root/Desktop/
* after you change the current work directory TerminalMail will ask you to Enter the file name 
## Sendgrid
* you can  use sendgrid Smtp login user name and API-KEY with out import extra module
## spoofing email
* you can use TerminalMailto spoofing email in order to do that have 
to login SMTP server free relay and send email from any one to anther
# connect me 
* jac11devel@gmail.com
