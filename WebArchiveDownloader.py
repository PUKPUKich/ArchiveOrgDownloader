import os
import requests
from concurrent.futures import ThreadPoolExecutor

os.makedirs("photo", exist_ok=True)

headers = {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru,uk-UA;q=0.9,uk;q=0.8,en-US;q=0.7,en;q=0.6",
    "cookie": "YOUR_COOKIES",
    "priority": "i",
    "referer": "YOUR_REFERER",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}

def download_image(page_num):
    # URL with page number
    url = f"YOUR_URL"
    try:
        # Send GET request to download the image
        response = requests.get(url, headers=headers, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the image to the 'photo' directory
            with open(f"photo/{page_num}.jp2", "wb") as file:
                file.write(response.content)
            print(f"Downloaded page {page_num}")
        else:
            print(f"Failed to download page {page_num}, status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading page {page_num}: {e}")

with ThreadPoolExecutor(max_workers=10) as executor:
    # Loop through pages from 0000 to 1000
    page_numbers = [f"{i:04}" for i in range(0, 1000)]
    executor.map(download_image, page_numbers)