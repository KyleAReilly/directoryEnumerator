# 🔍 Directory Enumerator (Python)

This is a lightweight, beginner-friendly Python script that uses a brute-force strategy to **enumerate directories** on a target web server using a wordlist. Ideal for learning web recon concepts and basic scripting.

---

## ✨ Features

- Prompts for target URL interactively
- Automatically sanitizes input (adds protocol, strips slashes)
- Iterates through a wordlist and checks each path (e.g., `/admin.html`)
- Displays ❌ for 404 responses and ✅ for valid hits
- Prints a clean summary of all valid directories at the end
- Includes basic error handling for bad responses

---

## 🧠 What You’ll Learn

- Using Python’s `requests` module to make HTTP GET requests
- How to interpret HTTP status codes
- Looping through wordlists to automate recon tasks
- Graceful error handling in scripts
- Basic automation used in bug bounty and ethical hacking

---

## 📦 Requirements

- Python 3.x
- `requests` module (install with `pip install requests`)

---
