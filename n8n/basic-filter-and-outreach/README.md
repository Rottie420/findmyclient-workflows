# Basic Filter & Outreach

Send personalized outreach emails to verified leads while automatically preventing duplicate emails.

This workflow reads leads from an n8n Data Table, filters for verified contacts that have not yet been contacted, sends a personalized email, and updates each successfully contacted lead by marking its **`outreach`** status as **`sent`**.

> [!IMPORTANT]
> This workflow expects your Data Table to use the structure provided in **`leads-table-format.csv`**, including an **`outreach`** column. Before running the workflow, import the CSV and configure both the **Get Rows** and **Upsert row(s)** nodes to use your Data Table.

## Features

* 📥 Read leads from an n8n Data Table
* ✅ Filter only verified email addresses
* 🚫 Automatically skip leads that have already been contacted
* 📧 Send personalized outreach emails
* 📝 Mark successful emails as `sent`
* 🔄 Prevent duplicate outreach on future runs
* ⚡ Ready for any SMTP provider

## Requirements

* n8n
* An n8n Data Table
* SMTP credentials

## Setup

### 1. Import the workflow

Import the provided JSON workflow into your n8n instance.

### 2. Configure the Data Table

Open both the **Get Rows** and **Upsert row(s)** nodes and select your Data Table.

### 3. Configure SMTP

Open the **Send Email** node and configure your SMTP credentials.

Replace the sender address:

```text id="ej2cd9"
no-reply@yourdomain.com
```

with your own email address.

### 4. Customize your outreach

Edit the **Send Email** node to customize:

* Subject
* Email body
* Sender name
* Personalization

## Workflow

```text id="ey1ndg"
Manual Trigger
      │
      ▼
 Read Leads
      │
      ▼
 Filter Verified &
 Uncontacted Leads
      │
      ▼
 Send Email
      │
      ▼
 Mark Outreach = sent
```

## Filtering Logic

A lead is emailed only if:

* `verified = 1`
* An email address exists
* `outreach != "sent"`

After a successful email, the workflow automatically updates:

```text id="knu2m9"
outreach = sent
```

This prevents the same lead from receiving duplicate outreach during future executions.

## Customization Ideas

* Add HTML email templates
* Personalize using company name
* Add rate limiting
* Send follow-up sequences
* Record sent timestamps
* Connect Mailgun, SendGrid, Amazon SES, Gmail, or Microsoft 365
* Trigger CRM updates after successful delivery

