import requests
from bs4 import BeautifulSoup

# URL of the application tracking page
url = "https://ceoaperolls.ap.gov.in/AP_MLC_2024/ERO/Status_Update_2024/knowYourApplicationStatus.aspx"

# Set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

# Start a session to persist cookies
session = requests.Session()

# Step 1: Make an initial GET request to obtain VIEWSTATE and EVENTVALIDATION
response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract hidden fields like VIEWSTATE, EVENTVALIDATION, etc.
viewstate = soup.find("input", {"id": "__VIEWSTATE"})["value"]
eventvalidation = soup.find("input", {"id": "__EVENTVALIDATION"})["value"]

# Step 2: Update the form payload for submission
payload = {
    "__VIEWSTATE": viewstate,
    "__EVENTVALIDATION": eventvalidation,
    "txtApplicationID": "YOUR_APPLICATION_ID_HERE",  # Replace with your actual application ID
    "btnSubmit": "Submit",  # Update based on button name
}

# Step 3: Perform a POST request to submit the form and track the application
post_response = session.post(url, headers=headers, data=payload)

# Parse the response HTML to extract the tracking information
soup = BeautifulSoup(post_response.text, "html.parser")

# Extract the relevant tracking data - this depends on the HTML structure of the response page
tracking_status = soup.find("div", {"id": "statusDiv"})  # Update with correct tag/ID

if tracking_status:
    print(tracking_status.text.strip())
else:
    print("Unable to extract tracking information. Check the HTML structure.")

