from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse

# Define the message to be sent
MESSAGE = "Hello! Just sending my greetings. Have a nice day! 😊"

# Specify the file containing the contact numbers (one number per line)
CONTACTS_FILE = "contacts.txt"

# Load the contact numbers from the specified file
with open(CONTACTS_FILE, "r") as file:
    contacts = [line.strip() for line in file.readlines() if line.strip()]

# Set up the Selenium WebDriver for Chrome (ensure ChromeDriver is in the PATH)
driver = webdriver.Chrome()

# Open WhatsApp Web in the browser
driver.get("https://web.whatsapp.com/")
print("Please scan the QR code to log in to WhatsApp Web.")

# Wait until the WhatsApp Web main page is fully loaded (e.g., by detecting a search bar)
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true']"))
)
print("Successfully logged in!")

# Loop through the contact numbers and send the message to each one
for number in contacts:
    try:
        # Encode the message to handle special characters, spaces, and emojis
        encoded_message = urllib.parse.quote(MESSAGE)

        # Construct the WhatsApp URL with the phone number and message
        url = f"https://web.whatsapp.com/send?phone={number}&text={encoded_message}"
        driver.get(url)

        # Wait for the 'Send' button to become clickable
        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
        )
        send_button.click()
        print(f"Message successfully sent to {number}")

        # Optional pause before moving to the next contact
        time.sleep(5)
    except Exception as error:
        print(f"Could not send message to {number}: {error}")
        continue

# Close the browser once all messages are sent
print("Finished sending messages.")
driver.quit()
