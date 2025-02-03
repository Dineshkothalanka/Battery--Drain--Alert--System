Battery Drain Alert System

A Python-based system to monitor battery levels and send alerts via SMS and email. This project is designed to help users proactively manage battery levels in medical devices or other critical systems.
Features
Real-Time Monitoring: Continuously monitors battery levels.
SMS Alerts: Sends SMS notifications using Twilio when the battery level drops below a threshold.
Email Alerts: Sends email notifications using SMTP for additional redundancy.
Visualization: Generates a graph of battery levels over time using Matplotlib.
Customizable Threshold: Users can set their own battery level threshold for alerts.

Requirements
Python 3.12.4
Libraries: pandas, numpy, matplotlib, twilio, smtplib

Installation
1. Clone the repository:
   bash
   git clone https://github.com/Dineshkothalanka/Battery--Drain--Alert.git
   
2. Navigate to the project folder:
   bash
   cd Battery-Drain-Alert-System
   
3. Install the required libraries:
   bash
   pip install -r requirements.txt
   

Configuration
1. Twilio Setup:
   Sign up for a Twilio account at Twilio 
   Get your Account SID, Auth Token, and a Twilio phone number.
   Replace the placeholders in the script with your Twilio credentials.

2. SMTP Setup:
   Use your Gmail account for SMTP.
   Enable Less Secure Apps or generate an App Password in your Google Account settings.
   Replace the placeholders in the script with your email credentials.

Usage
1. Run the script:
   bash
   python BDAMD.py
2. The system will simulate battery levels and send alerts when the level drops below 20%.

Example Output
SMS Alert
You will receive an SMS like this:
Low Battery Alert: 15% remaining!

Email Alert
You will receive an email with the subject:
Subject: Low Battery Alert
Body: Battery level is at 15%.

Visualization
A graph will be displayed showing battery levels over time:
Battery Level Graph 1
Battery Level Graph 2

Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch:
   bash
   git checkout -b feature/your-feature-name
   
3. Commit your changes:
   bash
   git commit -m "Add your feature"
   
4. Push to the branch:
   bash
   git push origin feature/your-feature-name
   
5. Open a pull request.
    git pull origin branch-name

License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Acknowledgments
Thanks to Twilio for providing the SMS API.
Thanks to Matplotlib for the visualization library.

Contact
For questions or feedback, feel free to reach out:
Email: dineshkothalanka2003@gmail.com
GitHub: https://github.com/Dineshkothalanka
