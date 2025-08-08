import requests

# Prompt user for URL once
user_input = input("Please enter a URL: ").strip()

# Sanitize URL input
if user_input.startswith("http://") or user_input.startswith("https://"):
    url = user_input.rstrip("/")
else:
    url = "http://" + user_input

print(f"\n🔍 Starting enumeration on: {url}\n")

# Load wordlist
with open("wordlist2.txt", "r") as file:
    directories = file.read().splitlines()

total = len(directories)
valid_dirs = []  # Store valid URLs here

# Start enumeration
for i, dir in enumerate(directories, start=1):
    target_url = f"{url}/{dir}.html"

    try:
        r = requests.get(target_url)

        if r.status_code == 404:
            print(f"[{i}/{total}] ❌ Not found: {target_url}")
        else:
            print(f"[{i}/{total}] ✅ Found: {target_url}")
            valid_dirs.append(target_url)

    except requests.exceptions.RequestException as e:
        print(f"[{i}/{total}] ⚠️ Error: {target_url} - {e}")

# Final summary
print("\n📋 Summary of valid directories found:")
if valid_dirs:
    for valid in valid_dirs:
        print(f" - {valid}")
else:
    print("No valid directories were found.")
