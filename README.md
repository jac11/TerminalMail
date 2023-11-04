# TerminalMail

TerminalMail is a command-line tool that allows you to send emails from your terminal, supporting both plain text and HTML emails, with or without attachments. Whether you need to send a quick message or a beautifully formatted HTML email with attachments, TerminalMail has you covered.
## SMTP Service :
  * to send emails through an SMTP relay service, you typically need to create an account 
   ##  Here are some free SMTP relay services:
   * Gmail (smtp.gmail.com)
   * Yahoo Mail (smtp.mail.yahoo.com)
   * Outlook.com (smtp.live.com)
   * SendinBlue (smtp.sendinblue.com)
   * SendGrid (smtp.sendgrid.net)
   * Elastic Email (smtp.elasticemail.com)
* Please note that the availability and terms of these services may change over time, so it's a good idea to check their websites for the most up-to-date information and any potential limitations or restrictions on their free plans.
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
  ## Required options 
  ```
     -S or --sender: Specify the sender's email account.
     -R or --receive: Specify the recipient's email account.
     -M or --smtp: Specify the SMTP server for the sender's email.
     -U or --user: Specify the username used for authentication with the SMTP server.
     -A or --authentication: Provide the password or API key for user authentication with 
 ```
* To provide users with the option to create a configuration file where they can store the required options for your terminalmail tool, you can structure the command and README as follows:README
  In your README, you should explain how to create and use a configuration file. Here's a modified section:
  ## Using a Configuration File
    * You have the option to store the required options in a configuration file, making it easier to send emails without repeatedly specifying the options. To do this, follow these steps:
    * explain how to create and use a configuration file. Here's a modified section:
     Using a Configuration File
   * You have the option to store the required options in a configuration file, making it easier to send emails without repeatedly specifying the options. To do this, follow these steps:
   * Create a configuration file (e.g., email_config.txt) and add the required options one by one in the following format:
   * You can add these options one per line, just as you would provide them in the command line.

      ```
      sender@example.com
      recipient@example.com
      smtp.example.com
      username
      password
      ```
   * Save the configuration file with a ".txt" extension.
   * Use the -C or --config flag to specify the path to the configuration file when running terminalmail. Here's the command to send an email using the configuration file:
  ```
  terminalmail -C /Desktop/Config.txt 
  ```
 ## HTML Email Option
  * With TerminalMail, you have the flexibility to create and send HTML emails.
  * To use this feature, you can provide your own custom HTML code for the email body.
  * Additionally, you can specify the path to an HTML file to use as the email content using the -F or --format flag, and include the --html flag to indicate that the email content should be in HTML format.
  * Using Custom HTML Code
    * You can compose an HTML email directly from the command line by providing your HTML code enclosed in double quotes. For example:
    ```
    terminalmail send -S sender@example.com -R recipient@example.com -M smtp.example.com -U username -A password --html -F "your_custom_email.html"
    ```

## Writing Your Email Message
  * You can create your email message in a plain text file, and the content of the file will be used as the email body. For example, you can create a file named email_message.txt and write your email content in it.
  * Sending Email Using a Message File
  * To send an email with the message content from the file, use the -p or --post option and specify the path to the file containing the email message:
```
terminalmail send -S sender@example.com -R recipient@example.com -M smtp.example.com -U username -A password -p email_message.txt
```
* In this command, the -p or --post flag is used to indicate that the email message should be read from the email_message.txt file. The tool will use the content of the file as the email body.
* By using this option, you can easily send email messages stored in files, making it convenient for sending pre-written messages or messages generated by other processes.
* Ensure that the content of the text file is formatted according to your email requirements, including the subject, recipient, and any other necessary details.
## Connect me
jac11devel@gamil.com
