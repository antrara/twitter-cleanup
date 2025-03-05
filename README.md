# Twitter Cleanup 🐦

# Installation and Usage Guide on Kali Linux 🐧

Follow these steps to install and run the Twitter Cleanup script on Kali Linux.

## 1⃣ Install Git and Python
Before downloading the script, make sure Git and Python are installed on your system.

### ✅ Check if Git is installed:
```sh
git --version
```
If Git is not installed, run:
```sh
sudo apt update && sudo apt install git -y
```

### ✅ Check if Python is installed:
```sh
python3 --version
```
If Python is not installed, use:
```sh
sudo apt install python3 python3-pip -y
```

## 2⃣ Clone the Repository from GitHub
Download the project to a local folder using:
```sh
git clone https://github.com/username/twitter-cleanup.git
```
Replace `username` with your GitHub username.

Navigate into the project folder:
```sh
cd twitter-cleanup
```

## 3⃣ Install Dependencies
Before running the script, install the required dependencies:
```sh
pip install -r requirements.txt
```

## 4⃣ Run the Script
Once installation is complete, run the script with:
```sh
python3 main.py
```
On the first run, you will be prompted to enter your Twitter API Key. Input your credentials as follows:
```yaml
Enter API Key: xxxxxxxxxxxxxxxx
Enter API Secret: xxxxxxxxxxxxxxxx
Enter Access Token: xxxxxxxxxxxxxxxx
Enter Access Secret: xxxxxxxxxxxxxxxx
```
The API Key will be automatically saved, so you don't need to enter it again in the future.

## 5⃣ Use Available Features
After logging in, you will see a menu with various options:

✅ Unfollow specific accounts  
✅ Unlike all tweets  
✅ Unretweet all reposts  
✅ Delete comments from your tweets  
✅ Delete tweets since a specific date  
✅ Logout from the API system  

Select the feature you want to use by entering the corresponding menu number.

## 6⃣ Logout (Remove API Key)
If you want to remove your saved API Key, choose the Logout option from the menu or run:
```sh
rm .env
```
This will delete the file storing your API credentials.

## 7⃣ Remove the Script if No Longer Needed
If you want to remove the project from your system:
```sh
cd ..
rm -rf twitter-cleanup
```

Enjoy using **Twitter Cleanup** to manage your Twitter activity efficiently! 🛠️
