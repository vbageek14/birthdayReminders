import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

df = pd.read_csv("/Users/konstimac/Documents/Coding/Python/Birthday Reminders/Birthdays.csv")

# Check the data type of the 'date_column' column
column_dtype = df['Birthdate'].dtype

# Convert 'Birthdate' column to datetime objects
df['Birthdate'] = pd.to_datetime(df['Birthdate'], format='%d-%b', errors='coerce')


df['Month_Name'] = df["Birthdate"].dt.strftime("%B")

df = df.groupby("Month_Name")["Name"].count().reset_index(name = "Count")

custom_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

mapping = {month: i for i, month in enumerate(custom_order)}
key = df["Month_Name"].map(mapping)

df = df.iloc[key.argsort()]


fig, ax = plt.subplots(1, figsize = (14, 10))
plt.bar(df["Month_Name"], df["Count"])
plt.xlabel("Month")
plt.ylabel("Number of Birthdays")
plt.title("Birthdays by Month")
plt.xticks(rotation=45)
plt.yticks(range(min(df["Count"]), max(df["Count"])+1))
plt.show()