import pandas as pd
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import config
import math

def main():
    # Create a dataframe from csv file with birthdate info
    df = pd.read_csv("/Users/konstimac/Documents/Coding/Python/Birthday Reminders/Birthdays.csv")

    # Create separate filtered dataframes for each condition
    df_Dina = df[df["Recipient"] != "Konsti"]
    df_Konsti = df[df["Recipient"] != "Dina"]
    df_Both = df[df["Recipient"] == "Both"]

    # Check each dataframe for any birthdays matching today's date
    birthday_names_Dina = checkBirthday(df_Dina)
    birthday_names_Konsti = checkBirthday(df_Konsti)
    birthday_names_Both = checkBirthday(df_Both)

    # Send email reminders to recipients
    if birthday_names_Both and not birthday_names_Dina and not birthday_names_Konsti:
        send_mail(birthday_names_Both, "Both")
    if birthday_names_Dina:
        send_mail(birthday_names_Dina, "Dina")
    if birthday_names_Konsti:
        send_mail(birthday_names_Konsti, "Konsti")

def checkBirthday(df):
    today = datetime.today().strftime("%d-%b")
    today_birthdays = df[df["Birthdate"]==today] 
    if not today_birthdays.empty:
        return [(row["Name"], row["Year"], row["Recipient"]) for index, row in today_birthdays.iterrows()]
    else:
        return []

def get_mail(names):
    subject = "Birthday Alert"
    current_year = int(datetime.now().year)

    # Extract name from tuple
    name_list = [name for name, _, _, in names]

    if len(names) == 1:
        name, year, recipient = names[0]
        body = f"{name} has a birthday today.\n\n"
        if year and not math.isnan(year):
            age = current_year - int(year)
            body += f"They are turning {age} years old."
    else:
        body = ", ".join(name_list[:-1]) + ", and " + name_list[-1] + " have birthdays today.\n\n"

        for name, year, recipient in names:
            if not math.isnan(year):
                age = current_year - int(year)
                body += f"{name} is turning {age} years old.\n"
                
    return subject, body

def send_mail(birthday_names, recipient):
    
    subject, message_text = get_mail(birthday_names)

    # Add "Good morning" to email body
    message_text = "Good morning, \n\n" + message_text

    # Set the content type to plain text
    msg = MIMEMultipart()
    msg.attach(MIMEText(message_text, "plain"))
    
    # Set the subject separately
    msg["Subject"] = subject

    # Set up email sending code using smtplib including app password for Gmail and recipient email addresses
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(config.EMAIL_ADDRESS, config.EMAIL_APP_PASSWORD)

        if recipient == "Dina":
            smtp.sendmail(config.EMAIL_ADDRESS, config.RECIPIENT1, msg.as_string())
            
        if recipient == "Konsti":
            smtp.sendmail(config.EMAIL_ADDRESS, config.RECIPIENT2, msg.as_string())
            
        if recipient == "Both":
            smtp.sendmail(config.EMAIL_ADDRESS, config.BOTH_RECIPIENTS, msg.as_string())            
    
if __name__ == "__main__":
    main()
