# Python Web Scraping System

A Python-based web scraping system designed to discover, collect, filter, and extract articles from multiple websites using RSS feeds and XML sitemaps.

The system automates the complete article extraction workflow, from URL discovery to structured JSON data storage.

**Project Achievement: Successfully extracted approximately 10,000 articles.**

## Key Features

- **RSS Feed Parsing:** Automatically collects article URLs from configured RSS feeds.
- **XML Sitemap Parsing:** Discovers additional article URLs through website sitemaps.
- **Multi-Website Support:** Supports article collection from multiple websites.
- **URL Filtering:** Filters collected URLs according to the selected website.
- **Website Validation:** Checks website URLs before processing.
- **Article Extraction:** Extracts article content from filtered URLs.
- **Multithreading:** Uses Python's `ThreadPoolExecutor` for concurrent processing.
- **JSON Storage:** Saves extracted article data in structured JSON files.
- **Jupyter Notebook Interface:** Provides a centralized execution workflow through `main.ipynb`.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- XML Parsing
- RSS Feed Parsing
- JSON
- Concurrent Futures (ThreadPoolExecutor)
- Jupyter Notebook

## Project Structure

```text
Project_02 WEB scriping/
│
├── all_urls/
│
├── Extracted_Data/
│
├── Filter_system/
│
├── Filtered_urls/
│
├── filter.py
├── main.ipynb
├── PossibleArticleContentClasses.py
├── rss_parser.py
├── rssLinksOfWebsites.py
├── scraper.py
├── sitemapLink_parser.py
├── Sitemaps.py
├── WebChecker.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: Generated data directories are excluded from the GitHub repository.*

## How to Use

The entire scraping workflow is controlled through `main.ipynb`.

Users can execute different notebook cells to perform URL discovery, filtering, and article extraction.

### Step 1: Import Modules

Run the first cell of `main.ipynb`.

This cell imports all required project modules and dependencies.

It prepares the scraping environment for subsequent operations.

### Step 2: Collect Article URLs Using RSS Feeds

Run the second cell to collect article URLs from configured RSS feeds.

The project maintains a dictionary named `Channels_With_RSS` inside `rssLinksOfWebsites.py`.

This dictionary contains website names and their corresponding RSS feed URLs.

The notebook automatically iterates through the configured RSS feeds and passes them to the RSS parser.

Article URLs are collected and organized according to their respective websites.

**Users do not need to manually provide RSS URLs if the website is already configured.**

### Step 3: Collect Additional URLs Using XML Sitemaps (Optional)

If additional article URLs are required, users can use the sitemap parsing functionality.

The project maintains sitemap information in `Sitemaps.py`.

Users can process the available sitemap URLs or directly provide a specific sitemap URL along with its website name.

Example:

```python
sitemapLink_parcer.parse_sitemap(
    "https://example.com/sitemap.xml",
    "Example Website"
)
```

This step allows users to discover additional URLs beyond those collected through RSS feeds.

### Step 4: Filter Article URLs

After collecting URLs, execute the filtering cell.

Users only need to specify the correct website name in the filtering function.

The filtering system processes the collected URLs and identifies relevant article pages.

`ThreadPoolExecutor` is used to perform filtering tasks concurrently.

The resulting filtered URLs are saved in the `Filtered_urls/` directory.

### Step 5: Extract Article Content

The final cell handles article extraction.

Users need to specify the JSON filename containing the filtered URLs from the `Filtered_urls/` directory.

The file already contains the URLs collected and filtered during the previous stages.

Users can also apply slicing if they want to extract articles from a specific range of URLs.

The extraction process is executed through the scraper module.

Extracted article data is automatically saved in the `Extracted_Data/` directory in JSON format.

## Complete Workflow

```text
        RSS Feed URLs
              |
              v
        RSS Feed Parser
              |
              v
        Article URLs
              |
              |
      XML Sitemap Parser
              |
              v
       Additional URLs
              |
              v
       URL Collection
              |
              v
       URL Filtering
              |
              v
        Filtered_urls/
              |
              v
       Article Extraction
              |
              v
        Extracted_Data/
              |
              v
        Structured JSON
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd Project_02_WEB_Scraping
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

1. Open the project in Visual Studio Code.
2. Open `main.ipynb`.
3. Execute the notebook cells in sequence.
4. Collect URLs through RSS feeds.
5. Optionally collect additional URLs through XML sitemaps.
6. Filter URLs for the required website.
7. Extract article content.
8. Find the extracted JSON files inside `Extracted_Data/`.

## Output

The extracted article data is stored in JSON format.

This data can be used for:

- Natural Language Processing (NLP).
- Machine Learning datasets.
- News analysis.
- Text processing.
- Further data analysis and research.

## Future Improvements

- Improve article content detection across different website structures.
- Expand support for additional websites.
- Optimize concurrent scraping performance.
- Improve error handling and retry mechanisms.
- Implement automated scraping schedules.

## Author

**Syed Muhammad Haleem**

BS Software Engineering Student  
University of Sargodha

---

*Developed as a Python Web Scraping Project.*