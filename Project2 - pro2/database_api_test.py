import os
import requests
import json
from typing import List, Dict, Any

# --- CONFIGURATION ---
# IMPORTANT: Replace the placeholder with your actual Semantic Scholar API Key
# For production, load this securely from an environment variable.
SS_API_KEY = "4kA6Y6j2xB8Qckgn4FTGp7QYMAnJIAqg8AY5kakY" # <--- REPLACE THIS

DATASETS_API_BASE_URL = "https://api.semanticscholar.org/datasets/v1/release/"
DATASET_NAME = "papers" # Use 'papers' for core metadata (title, abstract, year, embeddings, etc.)

def get_dataset_download_links(api_key: str, dataset_name: str = DATASET_NAME) -> List[str]:
    """
    Retrieves the list of download URLs for the latest Semantic Scholar bulk dataset.
    """
    if not api_key or api_key == "YOUR_SEMANTIC_SCHOLAR_API_KEY":
        raise ValueError("Semantic Scholar API Key is missing or invalid.")

    # 1. Get the latest release date ID
    release_url = f"{DATASETS_API_BASE_URL}latest"
    print("Step 1: Fetching latest release ID...")
    
    try:
        # Note: This step typically does not require the API key
        resp_release = requests.get(release_url, timeout=10)
        resp_release.raise_for_status()
        release_data = resp_release.json()
        release_id = release_data.get('release_id')
        print(f"Latest Release ID Found: {release_id}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching release ID: {e}")
        return []

    # 2. Get the download links for the specified dataset
    download_link_url = f"{DATASETS_API_BASE_URL}{release_id}/dataset/{dataset_name}"
    headers = {"x-api-key": api_key}
    
    print(f"Step 2: Requesting download links for '{dataset_name}'...")
    
    try:
        # Authentication is REQUIRED for this step
        resp_links = requests.get(download_link_url, headers=headers, timeout=10)
        resp_links.raise_for_status()
        links_data = resp_links.json()
        
        # The core data is usually split into many files (shards)
        download_urls = links_data.get('files', [])
        
        if download_urls:
            print(f"Success! Found {len(download_urls)} data file shards.")
            
            # Print size information from the response description if available
            description = links_data.get('description', '')
            print(f"Dataset Description: {description}")
            
            return download_urls
        else:
            print(f"Error: Datasets API did not return any download links for '{dataset_name}'.")
            return []

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error {e.response.status_code}. Check API key or dataset name.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Error requesting download links: {e}")
        return []

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    
    if SS_API_KEY == "YOUR_SEMANTIC_SCHOLAR_API_KEY":
        print("Please set your actual Semantic Scholar API key before running.")
    else:
        # Get the list of all file URLs
        download_file_urls = get_dataset_download_links(SS_API_KEY)

        if download_file_urls:
            print("\n--- FIRST 3 DOWNLOAD LINKS ---")
            for url in download_file_urls[:3]:
                print(url)
            print(f"\nTotal file count: {len(download_file_urls)}")
            print("\nUse these URLs for your bulk, local download process.")
        else:
            print("Failed to retrieve any download URLs.")