# Multiple Outreach

Scale your cold outreach by sending personalized emails across multiple parallel workflows while automatically preventing duplicate emails.

This workflow reads verified leads from an n8n Data Table, splits them into multiple processing pipelines, sends personalized emails with configurable delays, and marks each successfully contacted lead as **`sent`** to prevent future duplicate outreach.

> [!IMPORTANT]
> This workflow expects your Data Table to use the structure provided in **`leads-table-format.csv`**, including an **`outreach`** column. Before running the workflow, import the CSV and configure all **Get Rows** and **Upsert row(s)** nodes to use your Data Table.

## Features

* 🚀 Parallel outreach pipelines for higher throughput
* 📥 Read leads from an n8n Data Table
* ✅ Filter verified email addresses only
* 🚫 Skip contacts that have already been emailed
* 📧 Send personalized outreach emails
* ⏱️ Configurable delays between emails
* 📝 Automatically mark contacted leads as `sent`
* 🔄 Safe to run repeatedly without duplicate outreach

## Requirements

* n8n
* An n8n Data Table
* SMTP credentials

## Setup

### 1. Import the workflow

Import the provided JSON workflow into your n8n instance.

### 2. Configure the Data Table

Open every **Get Rows** and **Upsert row(s)** node and select your Data Table.

### 3. Configure SMTP

Open each **Send Email** node and configure your SMTP credentials.

Replace:

```text
no-reply@yourdomain.com
```

with your own sender email.

### 4. Customize your outreach

Edit the **Send Email** nodes to customize:

* Subject
* Email body
* Sender name
* Personalization

### 5. Adjust sending speed (Optional)

Modify the **Wait** nodes to control the delay between emails based on your provider's sending limits.

## Workflow

```text
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
 Split into Multiple
 Outreach Pipelines
      │
      ▼
 Wait Between Emails
      │
      ▼
 Send Personalized Emails
      │
      ▼
 Mark Outreach = sent
```

## Filtering Logic

A lead is emailed only if:

* `verified = 1`
* An email address exists
* `outreach != "sent"`

After each successful delivery, the workflow automatically updates:

```text
outreach = sent
```

This ensures future executions skip previously contacted leads.

## Customization Ideas

* Increase or decrease the number of parallel outreach pipelines
* Add randomized delays between emails
* Rotate sender accounts
* Send HTML email templates
* Add follow-up sequences
* Record timestamps for each outreach
* Connect Mailgun, SendGrid, Amazon SES, Gmail, or Microsoft 365
* Trigger CRM updates after successful delivery
