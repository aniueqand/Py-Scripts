
import json
import requests
import hashlib
import time
import os
import random
import string

# Replace {username} with the Instagram username of the profile picture you want
username = "type username"
file_path = "profile.jpg"
prev_hash = ""

while True:
 try:

    # Make a GET request to the Instagram API to get user information
    response = requests.get(f"https://www.instagram.com/{username}/?__a=1&__d=dis")
    
    # Extract the profile picture URL from the JSON response
    data = json.loads(response.text)
    profile_pic_url = data['graphql']['user']['profile_pic_url_hd']
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
        if os.path.isfile('D:\username\profile.jpg'):
              random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
              os.rename("D:\username\profile.jpg", "D:\username\ "+ random_name + ".jpg")
 except Exception as ni:
    print(ni)
    time.sleep(120)
else:
        print("Profile picture not updated.")
    
    # Wait for 120 seconds before checking again
time.sleep(120)

