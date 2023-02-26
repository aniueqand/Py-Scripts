
import json
import requests
import hashlib
import time
import os
import random
import string

# Replace {username} with the Instagram username of the profile picture you want to monitor
username = "ire3mllyy"

# Define the file path to save the profile picture
file_path = "profile.jpg"

# Initialize the previous profile picture hash value
prev_hash = ""

while True:
 try:

    # Make a GET request to the Instagram API to get user information
    response = requests.get(f"https://www.instagram.com/ire3mllyy/?__a=1&__d=dis")
    
    # Extract the profile picture URL from the JSON response
    data = json.loads(response.text)
    profile_pic_url = data['graphql']['user']['profile_pic_url_hd']
    
    # Compute the hash value of the profile picture URL
    current_hash = hashlib.sha256(profile_pic_url.encode()).hexdigest()
    
    # Compare the current hash value with the previous hash value
    if current_hash != prev_hash:
        # Download the profile picture using the extracted URL
        response = requests.get(profile_pic_url)
        
        # Save the profile picture to a file
        with open(file_path, "wb") as f:
              f.write(response.content)
        
        # Update the previous hash value with the current hash value
        prev_hash = current_hash
        
        print("Profile picture updated.")
        if os.path.isfile('D:\ire3mllyy\profile.jpg'):
              random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
              os.rename("D:\ire3mllyy\profile.jpg", "D:\ire3mllyy\ "+ random_name + ".jpg")
 except Exception as ni:
    print(ni)
    time.sleep(120)
else:
        print("Profile picture not updated.")
    
    # Wait for 10 seconds before checking again
time.sleep(120)

