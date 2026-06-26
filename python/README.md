# Python Example

A simple Python example for searching the FindMyClient API, waiting for the search to complete, and retrieving discovered leads.

## Features

* 🚀 Start a new search job
* ⏳ Poll until the search is complete
* 📋 Retrieve discovered leads
* 🐍 Lightweight example using the `requests` library
* ⚡ Easy to integrate into your own applications

## Requirements

* Python 3.9+
* `requests`

Install dependencies:

```bash
pip install requests
```

## Configuration

Update the following values in the script:

```python
API_TOKEN = "YOUR-API-TOKEN"
```

You can also customize the search limits:

```python
max_pages = 10
max_websites = 10
max_results = 10
```

## Running

Execute the script:

```bash
python main.py
```

Example output:

```text
Job started: 12345678
Status: pending
Status: running
Status: completed

{'domain': 'example.com', 'email': 'contact@example.com', ...}
```

## How It Works

```text
Start Search
      │
      ▼
Receive Job ID
      │
      ▼
Poll Status Every 30 Seconds
      │
      ▼
Search Completed
      │
      ▼
Retrieve Leads
      │
      ▼
Print Results
```

## Customization Ideas

* Export results to CSV
* Save leads to a database
* Send leads to a CRM
* Build a Flask or FastAPI application
* Integrate with AI workflows
* Start automated outreach
