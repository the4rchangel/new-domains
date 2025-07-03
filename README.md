# Domain Scraper

A Python tool that automatically scrapes newly registered domains from WHOIS DS (Whois Database Service) for the past 15 days. This tool downloads domain lists, processes them, and creates a consolidated file of all newly registered domains.

## 🚀 Features

- **Automated Domain Collection**: Downloads domain lists for the past 15 days
- **Base64 URL Encoding**: Handles the required URL encoding for WHOIS DS endpoints
- **ZIP File Processing**: Automatically extracts domain lists from downloaded ZIP files
- **Deduplication**: Removes duplicate domains across multiple days
- **Professional Headers**: Uses realistic browser headers to avoid blocking
- **Rate Limiting**: Includes delays between requests to be respectful to the server

## 📋 Prerequisites

- Python 3.6 or higher
- Internet connection
- Required Python packages (see `requirements.txt`)

## 🛠️ Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd domains
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 Usage

Run the domain scraper:

```bash
python domain_scraper.py
```

The script will:
1. Create a `domain_data` directory if it doesn't exist
2. Download domain lists for the past 15 days from WHOIS DS
3. Process and extract domain names from ZIP files
4. Save all unique domains to `domain_data/new_domains.txt`

## 📁 Output

After running the script, you'll find:

- **`domain_data/new_domains.txt`**: The main output file containing all unique newly registered domains
- **`domains_YYYY-MM-DD.zip`**: Individual ZIP files downloaded for each date (temporary files)

## 🔍 Searching for Company Names

Once the domain list is complete, you can search for specific company names or keywords using various methods:

### 🖥️ For Windows Users (No Technical Knowledge Required)

#### Method 1: Using Notepad (Easiest)
1. Open the `domain_data` folder
2. Right-click on `new_domains.txt` and select "Open with" → "Notepad"
3. Press `Ctrl + F` to open the search box
4. Type the company name you want to search for (e.g., "google", "facebook")
5. Press `Enter` to find the first match
6. Press `F3` to find the next match

#### Method 2: Using Windows Search
1. Open File Explorer
2. Navigate to the `domain_data` folder
3. In the search box (top right), type: `content:"google"` (replace "google" with your search term)
4. This will show files containing that text

#### Method 3: Using PowerShell (Advanced)
1. Right-click the Start button and select "Windows PowerShell" or "Terminal"
2. Navigate to your project folder: `cd "C:\path\to\your\domains\folder"`
3. Run one of these commands:
   ```powershell
   # Search for domains containing "google"
   Get-Content "domain_data/new_domains.txt" | Select-String "google"

   # Search for domains containing "facebook" (case insensitive)
   Get-Content "domain_data/new_domains.txt" | Select-String -Pattern "facebook" -CaseSensitive:$false

   # Search for multiple companies
   Get-Content "domain_data/new_domains.txt" | Select-String -Pattern "google|facebook|microsoft|apple"
   ```

### 🍎 For Mac Users (No Technical Knowledge Required)

#### Method 1: Using TextEdit (Easiest)
1. Open the `domain_data` folder in Finder
2. Right-click on `new_domains.txt` and select "Open with" → "TextEdit"
3. Press `Cmd + F` to open the search box
4. Type the company name you want to search for (e.g., "google", "facebook")
5. Press `Enter` to find matches
6. Use the arrow buttons to navigate between matches

#### Method 2: Using Finder Search
1. Open Finder
2. Navigate to the `domain_data` folder
3. In the search box (top right), type: `content:"google"` (replace "google" with your search term)
4. This will show files containing that text

#### Method 3: Using Terminal (Advanced)
1. Open Terminal (Applications → Utilities → Terminal)
2. Navigate to your project folder: `cd "/path/to/your/domains/folder"`
3. Run one of these commands:
   ```bash
   # Search for domains containing "google"
   grep -i "google" domain_data/new_domains.txt

   # Search for domains containing "facebook"
   grep -i "facebook" domain_data/new_domains.txt

   # Search for multiple companies
   grep -i -E "google|facebook|microsoft|apple" domain_data/new_domains.txt
   ```

### 💻 For Linux Users
```bash
# Search for domains containing "google"
grep -i "google" domain_data/new_domains.txt

# Search for domains containing "facebook"
grep -i "facebook" domain_data/new_domains.txt

# Search for multiple companies
grep -i -E "google|facebook|microsoft|apple" domain_data/new_domains.txt
```

### 🐍 Using Python (For All Platforms)
```python
# Search for specific company names
def search_domains(company_name):
    with open('domain_data/new_domains.txt', 'r') as f:
        domains = f.read().splitlines()
    
    matching_domains = [domain for domain in domains if company_name.lower() in domain.lower()]
    return matching_domains

# Example usage
google_domains = search_domains('google')
facebook_domains = search_domains('facebook')

print(f"Found {len(google_domains)} domains containing 'google':")
for domain in google_domains:
    print(f"  - {domain}")
```

### 📝 Quick Search Tips
- **Case doesn't matter**: Searching for "Google", "google", or "GOOGLE" will find the same results
- **Partial matches work**: Searching for "face" will find domains containing "facebook", "faceapp", etc.
- **Multiple terms**: You can search for multiple companies by running separate searches
- **Save results**: You can copy and paste search results into a new text file for later reference

## 📊 Example Output

The `new_domains.txt` file will contain one domain per line:
```
example123.com
newstartup.io
techcompany.net
brandname.org
...
```

## ⚠️ Important Notes

- **Rate Limiting**: The script includes a 1-second delay between requests to be respectful to the WHOIS DS servers
- **Data Source**: This tool scrapes data from WHOIS DS, which provides newly registered domain information
- **File Size**: The output file can be quite large depending on the number of domains registered in the past 15 days
- **Temporary Files**: ZIP files are saved locally during processing but can be cleaned up after use

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⚖️ Disclaimer

This tool is for educational and research purposes. Please ensure you comply with the terms of service of WHOIS DS and respect rate limits when using this tool. 