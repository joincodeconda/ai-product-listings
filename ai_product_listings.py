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
