import requests
import datetime
import os
import zipfile
import io
import time
import base64

def get_domain_urls():
    """Get the URLs of domain files for the past 15 days"""
    base_url = "https://www.whoisds.com/whois-database/newly-registered-domains"
    urls = []
    
    for i in range(15):
        date = datetime.datetime.now() - datetime.timedelta(days=i)
        # Format date as YYYY-MM-DD and encode in base64
        date_str = date.strftime("%Y-%m-%d.zip")
        encoded_date = base64.b64encode(date_str.encode()).decode()
        urls.append(f"{base_url}/{encoded_date}/nrd")
    
    return urls

def download_and_process_domain_file(url):
    """Download and process a single domain file"""
    try:
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        
        # Save the ZIP file
        date_str = base64.b64decode(url.split('/')[-2]).decode()
        zip_file = f"domains_{date_str}"
        with open(zip_file, 'wb') as f:
            f.write(response.content)
        print(f"Saved ZIP file to {zip_file}")
        
        # Try to process as zip file
        try:
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
                # Look for the domain-names.txt file
                for file_name in zip_file.namelist():
                    if file_name == 'domain-names.txt':
                        with zip_file.open(file_name) as f:
                            content = f.read().decode('utf-8')
                            return set(content.splitlines())
        except zipfile.BadZipFile:
            print(f"Response is not a valid ZIP file. Content preview: {response.content[:200]}")
            return set()
        
        return set()
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return set()

def main():
    # Create output directory if it doesn't exist
    output_dir = "domain_data"
    os.makedirs(output_dir, exist_ok=True)
    
    # Get URLs for the past 15 days
    urls = get_domain_urls()
    
    # Process each domain file
    all_domains = set()
    for url in urls:
        print(f"\nProcessing {url}...")
        domains = download_and_process_domain_file(url)
        all_domains.update(domains)
        time.sleep(1)  # Be nice to the server
    
    # Save results to file
    output_file = os.path.join(output_dir, "new_domains.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        for domain in sorted(all_domains):
            f.write(f"{domain}\n")
    
    print(f"\nProcessed {len(all_domains)} domains")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
