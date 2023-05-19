# COVID-19-Bot
This code starts with:

Import necessary libraries: The code starts by importing the required libraries, including requests, json, pandas, and time.

Setting up Slack webhook URL: The Slack webhook URL is assigned to the slack_webhook_url variable. This URL allows the code to post messages to a specific Slack channel or user.

Defining the get_monthly_trend() function: This function takes a month as input and retrieves the monthly trend analysis for COVID-19 deaths. It performs the following steps:

1. Loads the COVID-19 state-level data from a CSV file using pd.read_csv().

2. Filters the data to include only records for the specified month using the startswith() method of the 'date' column.

3. Calculates the total number of deaths for each state by grouping the data by state and summing the 'deaths' column using groupby() and sum().

4. Sorts the states in descending order based on the number of deaths.

5. Calculates the total deaths in the US by summing the 'deaths' column of the state_deaths DataFrame.

6. Generates a summary message that includes the top 3 states with the highest number of COVID-19 deaths for the given month, along with the percentage of those deaths compared to the total US deaths.

Defining the send_to_slack() function: This function takes a message as input and sends it to Slack using the Slack webhook URL. It constructs a JSON payload with the message text and sends a POST request using requests.post().

Defining the months list: This list contains the months for which summaries should be sent.

Sending the summaries at a fixed interval: The code iterates over the months list, calls the get_monthly_trend() function to retrieve the monthly trend analysis for each month, and then calls the send_to_slack() function to send the summary message to Slack. The time.sleep(1) statement introduces a 1-second delay between each summary to control the frequency of messages being sent.

This code fetches COVID-19 data from a CSV file, generates monthly trend analyses for the top 3 states with the highest COVID-19 deaths, and posts the summaries to Slack using a webhook URL. It allows users to stay updated on the COVID-19 situation in specific states for different months.
