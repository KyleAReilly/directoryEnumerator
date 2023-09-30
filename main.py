# Import the 'requests' library to make HTTP requests
import requests
import sys  # Import the 'sys' library for command-line arguments

# Read a list of directory names from a file named 'wordlist2.txt'
sub_list = open("wordlist2.txt").read()

# Split the contents of the file into a list of directory names
directories = sub_list.splitlines()

# Loop through each directory name in the list
for dir in directories:
    
    # Prompt the user for a URL and then enumerate it
    # user_input = input("Please enter a URL:  ")
    # if user_input.startswith("http://") or user_input.startswith("https://"):
    #     url = user_input
    # else:
    #     url = "http://" + user_input  # Add "http://" if it's missing
    # print(url)

    # Construct the URL to check (assuming the target domain is provided as a command-line argument. Replace sys.argv[1] with variable url to use prompted for url
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"

    # Send an HTTP GET request to the constructed URL
    r = requests.get(dir_enum)

    # Check the HTTP response status code
    if r.status_code == 404:
        # If the status code is 404 (Not Found), the directory does not exist
        pass
    else:
        # If the status code is not 404, the directory likely exists
        print("Valid directory:", dir_enum)
