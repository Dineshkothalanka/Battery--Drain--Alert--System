#pandas library used to manipulate data
import pandas as pd
#numpy library used for numerical operations
import numpy as np
#used to work emails
import smtplib
#matplotlib is used for visualization
import matplotlib.pyplot as plt
#used to perform time operations
import time
#in order to send sms we need a library that is twilio by register in twilio we will get a twilio phone number, authentication and account sid
from twilio.rest import Client
#to use environment variables we need to import load_dotenv
from dotenv import load_dotenv
#to use environment variables we need to import os
import os

# Simulate realistic battery drain with random variations
battery_levels = np.clip(np.cumsum(np.random.normal(-0.8, 0.3, 200)), 0, 100)  # Random walk with mean decrease
battery_data = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-01-01', periods=len(battery_levels), freq='min'),
    'battery_level': battery_levels
})

#load environment variables from .env file
load_dotenv()
# Twilio credentials by accessing environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')# Twilio phone number
recipient_number = '+917075697459'  # Recipient's phone number

# Email credentials
sender_email = os.getenv('SENDER_EMAIL')  # Replace with your email
sender_password =os.getenv('SENDER_EMAIL_PASSWORD')  # Replace with your password or app password
recipient_email = 'dineshkothalanka@gmail.com'  # Recipient's email

# Cooldown period (in seconds)
COOLDOWN_PERIOD = 300  # 5 minutes

# Track the last alert time
last_alert_time = 0

# SMS Alert with Twilio
def send_sms_alert(battery_level):
    if not all([account_sid, auth_token, twilio_number]):
        print("Error: Missing Twilio credentials. SMS alert skipped.")
        return
        
    try:
        client = Client(account_sid, auth_token)
        # Verify credentials by checking account balance
        balance = client.balance.fetch()
        print(f"Twilio account balance: {balance.balance} {balance.currency}")
        
        message = client.messages.create(
            body=f"Low Battery Alert: {battery_level}% remaining!",
            from_=twilio_number,
            to=recipient_number
        )
        print(f"SMS Alert Sent: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS. Detailed error:")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {str(e)}")
        if hasattr(e, 'status'):
            print(f"HTTP Status Code: {e.status}")
        if hasattr(e, 'code'):
            print(f"Error Code: {e.code}")
        if hasattr(e, 'more_info'):
            print(f"More Info: {e.more_info}")

# Email Alert with SMTP
def send_email_alert(battery_level):
    message = f"Subject: Low Battery Alert\n\nBattery level is at {battery_level}%."
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()  # Enable TLS encryption
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, recipient_email, message)
        print("Email Alert Sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Monitor battery levels
def monitor_battery(data):
    global last_alert_time
    prev_level = 100  # Initialize previous level
    for index, row in data.iterrows():
        battery_level = row['battery_level']
        # Only alert when crossing below 20% threshold
        if battery_level < 20 and prev_level >= 20 and (time.time() - last_alert_time) > COOLDOWN_PERIOD:
            print(f"Low Battery Detected: {battery_level}% at {row['timestamp']}")
            try:
                send_sms_alert(battery_level)
            except Exception as e:
                print(f"SMS alert failed: {str(e)}")
            send_email_alert(battery_level)
            last_alert_time = time.time()  # Update the last alert time
        prev_level = battery_level  # Update previous level

# Visualize battery data
def visualize_battery_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data['battery_level'], marker='o', linestyle='-')
    plt.axhline(y=20, color='r', linestyle='--', label='Low Battery Threshold (20%)')
    plt.title('Battery Level Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Battery Level (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the system
monitor_battery(battery_data)
visualize_battery_data(battery_data)
