# Basic Search Workflow

This workflow submits a search request, waits for the search job to complete, retrieves the results, and returns the discovered email addresses for use in your own automations.

## Features

- 🚀 Submit searches to the FindMyClient API
- ⏳ Automatically poll until the search completes
- 📧 Extract discovered email addresses
- 🔀 Split emails into individual workflow items
- 📊 Optional Google Sheets integration
- ✉️ Optional Gmail notifications
- 🔌 Easy to extend with CRMs, databases, Slack, webhooks, and more

## Requirements

- n8n
- A FindMyClient API token

## Setup

### 1. Import the workflow

Import the provided JSON file into your n8n instance.

### 2. Configure your API token

Open the **Start Search** HTTP Request node and replace:

```
YOUR-API-TOKEN
```

with your FindMyClient API token.

### 3. Configure your search

Open the **Input Query** node and change:

```
tokyo sushi
```

to your desired search query.

Examples:

- dentists london
- accounting firms singapore
- restaurants tokyo
- roofing companies texas

### 4. (Optional)

Enable and configure:

- Google Sheets
- Gmail

if you want to automatically save or notify when searches complete.

## Workflow

```text
Manual Trigger
      │
      ▼
 Input Query
      │
      ▼
 Start Search
      │
      ▼
 Receive Job ID
      │
      ▼
 Poll Result API
      │
      ▼
Completed?
 ├── No → Wait 30s → Retry
 └── Yes
        │
        ▼
 Extract Emails
        │
        ▼
 Split Emails
        │
        ├── Google Sheets (optional)
        └── Gmail (optional)
```

## API Endpoints

Start a search:

```
POST https://findmyclient.org/api/search
```

Retrieve results:

```
GET https://findmyclient.org/api/result/{job_id}
```

## Customization Ideas

- Push leads into HubSpot
- Send to Salesforce
- Save to Airtable
- Store in PostgreSQL
- Send Slack notifications
- Trigger AI enrichment
- Start automated outreach
