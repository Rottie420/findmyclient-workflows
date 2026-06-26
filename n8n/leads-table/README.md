# Leads Table

Store discovered leads from the FindMyClient API directly into an n8n Data Table.

This workflow submits one or more search queries, waits for each search job to complete, retrieves the lead results, and inserts each discovered lead into an n8n Data Table for further processing and analysis.

> [!IMPORTANT]
> Before running this workflow, create a new **n8n Data Table** and import the provided **`leads-table-format.csv`** file. This creates the required table structure and columns used by the **Insert row** node. After importing, update the **Insert row** node to point to your newly created Data Table.

## Features

* 🚀 Submit searches to the FindMyClient API
* 🔄 Process multiple search queries in one workflow
* ⏳ Automatically wait until search jobs complete
* 📋 Retrieve full lead records
* 🗂️ Store leads in an n8n Data Table
* 🔀 Automatically split results into individual rows
* 🛡️ Handles searches with no results gracefully

## Requirements

* n8n
* FindMyClient API token
* An n8n Data Table

## Setup

### 1. Import the workflow

Import the provided JSON workflow into your n8n instance.

### 2. Create a Data Table

Create a new **n8n Data Table** and import the included **`leads-table-format.csv`** file.

After importing, open the **Insert row** node and select the Data Table you created.

### 3. Configure your API token

Open the **Start Search** node and replace:

```text
YOUR-API-TOKEN
```

with your FindMyClient API token.

### 4. Configure your search queries

Edit the **Input Query** node.

Example:

```json
{
  "items": [
    "Ottawa Ontario Businesses",
    "Restaurants Singapore",
    "Law Firms London"
  ]
}
```

Each query will be processed automatically.

## Workflow

```text
Manual Trigger
      │
      ▼
 Input Queries
      │
      ▼
 Process Each Query
      │
      ▼
 Start Search
      │
      ▼
 Poll Until Complete
      │
      ▼
 Retrieve Leads
      │
      ▼
 Split Rows
      │
      ▼
 Insert into n8n Data Table
```

## Output

Each discovered lead is stored as an individual row containing fields such as:

* Domain
* Email
* Email Type
* Verification Status
* MX Status
* Risk Score
* Prefix
* Query
* Created Date

## Customization Ideas

* Send leads to HubSpot
* Push into Salesforce
* Export to Google Sheets
* Save to PostgreSQL
* Trigger AI enrichment
* Start automated outreach
* Send Slack or Discord notifications
