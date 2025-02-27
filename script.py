import requests
import pandas as pd

# GitHub API URL for Kubernetes pull requests
url = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Fetch pull requests data
response = requests.get(url)  # Add headers=headers for authentication if required

if response.status_code == 200:
    # Load data into a Pandas DataFrame
    df = pd.DataFrame(response.json())
    
    # Extract PR creators and count occurrences
    pr_counts = df['user'].apply(lambda x: x['login']).value_counts()
    
    # Display results
    print("PR Creators and Counts:\n", pr_counts)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")