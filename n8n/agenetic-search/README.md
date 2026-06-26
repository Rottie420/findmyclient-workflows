# AI Agent Lead Generator

Automatically generate B2B search queries with AI, discover leads using the FindMyClient API, and store the results in an n8n Data Table.

This workflow uses Google Gemini to generate business search queries across different industries and countries, submits each query to the FindMyClient API, waits for every search to complete, retrieves the discovered leads, and stores them in an n8n Data Table for further automation.

> [!IMPORTANT]
> Before running this workflow, create a new **n8n Data Table** and import the provided **`leads-table-format.csv`** file. This creates the required table structure and columns used by the **Insert row** node. After importing, update the **Insert row** node to point to your newly created Data Table.

## Features

* 🤖 Generate B2B search queries with Google Gemini
* 🌍 Create searches across multiple countries and industries
* 🚀 Submit searches to the FindMyClient API
* ⏳ Automatically wait until each search completes
* 📋 Retrieve full lead records
* 🗂️ Store leads in an n8n Data Table
* 🔄 Process multiple searches automatically
* 🛡️ Skip searches with no results

## Requirements

* n8n
* FindMyClient API token
* Google Gemini API credentials
* An n8n Data Table

## Setup

### 1. Import the workflow

Import the provided JSON workflow into your n8n instance.

### 2. Create a Data Table

Create a new **n8n Data Table** and import the included **`leads-table-format.csv`** file.

After importing, open the **Insert row** node and select the Data Table you created.

### 3. Configure your FindMyClient API token

Open the **Start Search** node and replace:

```text
YOUR-API-TOKEN
```

with your FindMyClient API token.

### 4. Configure Google Gemini

Connect your Google Gemini credentials to the **Google Gemini Chat Model** node.

### 5. Customize the AI prompt (Optional)

Edit the **AI Agent** node to generate different industries, locations, or business types.

## Workflow

```text
Manual Trigger
      │
      ▼
 AI Agent (Generate Queries)
      │
      ▼
 Process Queries
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
 Split Results
      │
      ▼
 Insert into n8n Data Table
```

## Output

Each discovered lead is stored as an individual row containing fields such as:

* Query
* Domain
* Email
* Email Type
* Prefix
* Verification Status
* MX Status
* Risk Score
* Created Date

## Customization Ideas

* Generate queries for specific industries
* Focus on a single country or city
* Send leads to HubSpot or Salesforce
* Export to Google Sheets
* Store in PostgreSQL
* Trigger AI lead qualification
* Start automated email outreach
* Send Slack or Discord notifications

