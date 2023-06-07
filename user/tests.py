from django.test import TestCase

# Create your tests here.
import pandas as pd
import sqlite3
from django.conf import settings
from django.shortcuts import render


import os

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'pg_app.settings'

# Configure the settings
settings.configure()

# Access the settings
print(settings.DATABASES)


df = pd.read_csv("/home/senthil/Data/Data/Data_Base/CSV_file/apy.csv")
conn = sqlite3.connect(settings.DATABASES['default']['NAME'])
# Save the DataFrame to the database
table_name = 'apy'  # Specify the name for the table in the database
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()