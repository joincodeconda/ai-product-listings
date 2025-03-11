# Automate Product Listings with Python and the ShopTag.ai API

If you run an eCommerce business, creating compelling product listings can be time-consuming. Writing titles, descriptions, and keywords manually for every product can take hours. But what if you could automate this process using AI?

With [ShopTag.ai](https://www.shoptag.ai), you can generate high-quality product titles, descriptions, and SEO-friendly keywords from just an image. In this tutorial, we'll show you how to use Python to integrate the [ShopTag.ai API](https://www.shoptag.ai/api) and automate your product listing process.

---

## Why Automate Product Listings?

Manually crafting product descriptions can be tedious and inconsistent. Automating this process with AI ensures that your listings:

- Are **SEO-optimized**, helping customers find your products easily.
- Maintain a **consistent style and tone** across your store.
- **Save time** so you can focus on growing your business.

By the end of this guide, you'll have a working Python script that uses the [ShopTag.ai API](https://www.shoptag.ai/api) to generate product listings automatically and save them in a CSV file.

---

## Prerequisites

Before getting started, you'll need:

1. A **ShopTag.ai API key**, which you can generate [here](https://www.shoptag.ai/api).
2. Python installed on your computer ([download it here](https://www.python.org/downloads/)).
3. The `requests` and `pandas` Python libraries (install them with `pip install requests pandas`).
4. A directory containing product images.

---

## Step 1: Install Required Libraries

Ensure you have the necessary Python libraries installed. Open your terminal or command prompt and run:

```sh
pip install requests pandas
```

This installs `requests` for API communication and `pandas` for handling CSV files.

---

## Step 2: Create the Python Script

Create a new Python file (e.g., `ai_product_listings.py`) and add the following code:

```python
import os
import csv
import argparse
import requests
import pandas as pd

def generate_product_listing(image_path, api_token):
    url = "https://server.shoptag.ai/api/keywords"
    headers = {"Authorization": f'Bearer {api_token}'}
    payload = {
        "language": "en",  # Specify the language
        "maxKeywords": 25,  # Adjust keyword count
    }
    files = [('file', open(image_path, 'rb'))]
    
    response = requests.post(url, headers=headers, data=payload, files=files)
    return response.json()

def process_images(input_dir, output_file, api_token):
    data = []
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            image_path = os.path.join(input_dir, filename)
            print(f"Processing {filename}...")
            result = generate_product_listing(image_path, api_token)
            
            if result["error"] is None:
                data.append([
                    filename,
                    result["data"]["title"],
                    result["data"]["description"],
                    ", ".join(result["data"]["keywords"])
                ])
            else:
                print(f"Error processing {filename}: {result['error']}")
    
    df = pd.DataFrame(data, columns=["File Name", "Title", "Description", "Keywords"])
    df.to_csv(output_file, index=False)
    print(f"CSV file saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate product listings using ShopTag.ai API")
    parser.add_argument("input_dir", help="Path to the directory containing product images")
    parser.add_argument("output_file", help="Path to save the output CSV file")
    parser.add_argument("api_token", help="ShopTag.ai API token")
    args = parser.parse_args()
    
    process_images(args.input_dir, args.output_file, args.api_token)
```

---

## Step 3: Run the Script

Use the following command in your terminal to process all images in a directory:

```sh
python ai_product_listings.py /path/to/images output.csv YOUR_API_TOKEN
```

Replace:
- `/path/to/images` with the folder containing your product images.
- `output.csv` with the desired output CSV filename.
- `YOUR_API_TOKEN` with your actual ShopTag.ai API key.

---

## Example CSV Output

| File Name            | Title                    | Description                                   | Keywords               |
|----------------------|-------------------------|-----------------------------------------------|------------------------|
| blanket.jpg         | Teal Blue Weighted Blanket | This teal blue weighted blanket is perfect for sleeping. | blanket, weighted, teal, sleep, cotton |
| tshirt.jpg          | Cotton T-Shirt            | A comfortable cotton t-shirt for everyday wear. | t-shirt, cotton, casual, soft, lightweight |

---

## Step 4: Upload Listings to Your eCommerce Platform

Once you have your AI-generated content, you can import the CSV file into platforms like Shopify, WooCommerce, Wix, or BigCommerce.

For automation, you can modify the script to directly update your store's database or use platform-specific APIs to upload the content automatically.

---

## Pricing & API Limits

Each API call consumes **one product credit**, which you can purchase at [ShopTag.ai Pricing](https://www.shoptag.ai/pricing). The API allows **one request per second**, so keep that in mind if processing large inventories.

---

## Conclusion

With Python and [ShopTag.ai](https://www.shoptag.ai), you can automate product listings effortlessly. This saves time, improves SEO, and ensures consistency in your online store.

🔗 Get started with ShopTag.ai today: [www.shoptag.ai](https://www.shoptag.ai)

💡 Want to learn more? Check out the full API documentation here: [www.shoptag.ai/api](https://www.shoptag.ai/api).
