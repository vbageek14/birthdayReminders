# Birthday Reminder Program

The Birthday Reminder Program is a Python script designed to send automatic birthday reminders to designated recipients via email. It retrieves birthday information from a CSV file and checks for any birthdays matching the current date. If there are matches, it sends out reminder emails to the appropriate recipients.

## Features

- Sends automatic birthday reminders via email.
- Supports different recipients for reminders.
- Handles birthdays for individuals and for multiple people sharing the same birthday.

## Requirements

- Python 3
- Pandas library
- smtplib library
- Email account (Gmail used in this example)
- CSV file containing birthday information

## Example CSV Format

```Bash
Name,Birthdate,Birth Year,Reminder Recipient
John Doe,01-Jan,1990, [Your Name]
Jane Smith,15-May,1985,[Your Spouse's Name]
Adams Family,25-Dec,,Both
```

## Example Email Reminder
![image](https://github.com/vbageek14/birthdayreminders/assets/119551962/5140fa9c-7ff9-4681-8843-fae2346b20b6)


Feel free to customize it further based on your preferences or any additional information you'd like to include!
