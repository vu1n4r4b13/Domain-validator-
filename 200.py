import requests
import os
from tqdm import tqdm
import subprocess
import sys

# Check if required modules are installed, install them if not
try:
    import requests
    from tqdm import tqdm
    from termcolor import colored
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', 'tqdm', 'termcolor'])
    import requests
    from tqdm import tqdm
    from termcolor import colored

# Define your name as ASCII art
name = r"""
             __          ___        ___ _     __   _____ 
            /  |        /   |      /   | |   /  | |____ |
__   ___   _`| | _ __  / /| |_ __ / /| | |__ `| |     / /
\ \ / / | | || || '_ \/ /_| | '__/ /_| | '_ \ | |     \ \
 \ V /| |_| || || | | \___  | |  \___  | |_) || |_.___/ /
  \_/  \__,_\___/_| |_|   |_/_|      |_/_.__/\___/\____/ 

                                   twitter:@intuneric_boy
"""

# Define a list of colors to choose from
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

# Choose a random color for your name
color = colors[hash(name) % len(colors)]

# Print your name in the chosen color
print(colored(name, color))

# Get input and output file names
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

# Read in domains from input file
with open(input_file, 'r') as f:
    domains = f.read().splitlines()

# Initialize list of reachable domains
reachable_domains = []

# Check each domain and append reachable domains to list
for domain in tqdm(domains, desc="Checking domains", unit="domains"):
    try:
        response = requests.get('http://' + domain, timeout=5)
        if response.status_code == 200:
            reachable_domains.append(domain)
    except:
        pass

# Write reachable domains to output file
with open(output_file, 'w') as f:
    f.write('\n'.join(reachable_domains))

# Print confirmation message
print('Done. Reachable domains saved to', output_file)
