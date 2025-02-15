# 🔐 Key_Keeper 🚀


Passwords can be a challenge to remember, and they usually remain unchanged until you decide to update them. **This got me thinking: what if passwords were dynamic—automatically updating at regular intervals, yet still easily predictable for the user?** Imagine a system where all your passwords are secure and accessible through a single master-password. The innovative twist is that the master-password refreshes every minute. Currently, I've implemented it using the current time in 24-hour [HHMM] format, so it updates automatically every minute. With further development, this dynamic approach could significantly boost security.


**🔁 The Solution:**

Enter **Key_Keeper**, where your **master password** changes **every minute** based on the current time in `[HHMM]` format! ⏳ That means:
- No more memorizing long, complicated passwords.
- No need for internet-dependent password vaults.
- An extra layer of security, as master-password constantly evolve!
- At present, the master-password is a 4-digit number: the first two digits represent the current hour (00-24), and the last two represent the current minute (00-59).

All you need is the **current time** (yes, if you forgot the password just turn your head to the clock 🕒), and you’re in. Cool, right? 😎

**💡 The Doubt :** 

Imagine someone saying, *"Using time as a password is predictable—hackers could easily guess it."* While that's a valid concern, there are ways to make time-based passwords more secure:

1. **Different Time Zones:**  
   - If the password is generated based on local time, it will differ depending on the time zone. For example, a person in India might have a password like `2200` (representing 10:00 PM), while at the same moment, someone in Dubai could have `2030` (representing 8:30 PM).

2. **Adding a Constant Value:**  
   - Another option is to combine a fixed constant with the dynamic time. For instance, appending or prepending a number like `999` to the time-based part could result in a password like `9992030`. Here, `999` remains constant while `2030` changes with the time.

3. **Additional Techniques:**  
   - There are many other methods to further complicate the password, enhancing its security even more.
   
 `Imagine a hacker using brute force methods to try and crack a password that's changing every minute! 🤖💥`

---

## 🛠️ Tech Stack

- **Python 3.x** 🐍
- **`shelve`** (for secure local storage 🗄️)
- **`os`** (for handling directories 🏗️)
- **`PrettyTable`** (for displaying passwords in a clean, tabular format 📊)

---

## 🚀 Getting Started

🔹 **Step 1:** Clone the repository
```bash
 git clone https://github.com/malik-l0l/Key_Keeper.git
```

🔹 **Step 2:** Navigate into the directory
```bash
 cd Key_Keeper
```

🔹 **Step 3:** install prettytable
```bash
 pip install prettytable
```

🔹 **Step 4:** Run the script
```bash
 
 python Pswd.py
```

And that’s it! You’re now the proud owner of a **time-based password manager!** 🎉

---

## 🕹️ How It Works

🔑 **Store a Password**  
- Enter the domain name (e.g., `gmail.com`).
- Type your password when prompted.
- Your password is now stored securely!

📖 **Retrieve Your Passwords**  
- Enter the current time in **HHMM format** (e.g., `1430` for 2:30 PM).
- Watch as your stored passwords magically appear in a formatted table. ✨

🧹 **Clear All Passwords**  
- Type `clear` to erase everything.
- Confirm by typing `y`. (No regrets, right? 😅)

ℹ️ **Need Help?**  
- Type `help` to see a list of commands.

🚪 **Exit the Program**  
- Type `q` to quit like a pro. 🏃‍♂️💨

---

## 🔥 Cool Features

- **🛡️ Local & Secure:** No internet connection needed, all data is stored **locally**.
- **⏳ Dynamic Master Password:** Your master password updates every **minute**!
- **📋 Simple Commands:** Intuitive CLI interface that makes password management **fun**.
- **💎 Pretty Table Display:** No messy text—just a **clean, structured** password list.
- **⚡ Lightning Fast:** Enter the current time and retrieve all your stored passwords instantly!

---

## 🚀 Future Upgrades (Ideas in the Pipeline! 💡)

🔐 **Encryption Support:** Currently, passwords are stored in plaintext. Encrypting them will take security to the next level! 🔒

🔍 **Search Feature:** Easily find specific passwords instead of scrolling through a list.

💾 **Backup & Restore:** Export your password vault and restore it whenever needed.

🖥️ **GUI Version:** A sleek desktop interface for those who prefer clicking over typing. 😉

📱 **Mobile Support:** Because why not manage passwords on the go? 🤳

---


## 🖥️ Demo



https://github.com/user-attachments/assets/1f26ad40-5c38-4a95-95cf-b06cf6a3a044

The master-password was initially 2236 [10:36 PM], then it changed to 2237 [10:37 PM]



---

## ⚠️ Known Issues

- Currently tested on **Windows 10**. Compatibility with **MacOS/Linux** needs more testing.
- Plaintext storage—encryption is **coming soon!** 🚧

---

## 🎉 Ready to Secure Your Passwords the Smart Way?

Give **Key_Keeper** a spin and experience the **power of dynamic passwords**! Your time is literally your key. 🕒🔑

Happy password-keeping! 😃

**Cheers,**  
🚀 *malik-l0l*

