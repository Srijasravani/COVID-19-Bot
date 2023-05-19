import requests
import json
import pandas as pd
import time


slack_webhook_url = 'Slack_url'


def get_monthly_trend(month):
   
    df = pd.read_csv('data.csv')

    
    df_filtered = df[df['date'].str.startswith(month)]


    state_deaths = df_filtered.groupby('state')['deaths'].sum().reset_index()

 
    state_deaths = state_deaths.sort_values('deaths', ascending=False)

    
    total_deaths_us = state_deaths['deaths'].sum()


    summary_message = f"Top 3 states with the highest number of COVID deaths for the month of {month}:\n\n"

    for i, (_, row) in enumerate(state_deaths.head(3).iterrows()):
        state = row['state']
        deaths = row['deaths']
        percentage = (deaths / total_deaths_us) * 100

        summary_message += f"State #{i+1}: {state} - {deaths} deaths, {percentage:.2f}% of total US deaths\n"

    return summary_message


def send_to_slack(message):
    payload = {'text': message}
    response = requests.post(slack_webhook_url, data=json.dumps(payload))
    if response.status_code != 200:
        print(f"Failed to send message to Slack. Error: {response.text}")


months = ['03', '04', '05', '06']


for month in months:
    summary = get_monthly_trend(month)
    send_to_slack(summary)
    time.sleep(1)  
