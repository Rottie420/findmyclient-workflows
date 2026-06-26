# Contributing to FindMyClient Workflow Templates

First off, thank you for considering contributing! 🎉

This repository is community-driven, and every contribution helps make FindMyClient workflows better for everyone.

Whether you're fixing a typo, improving documentation, or creating a brand-new workflow, your contribution is appreciated.

---

## Ways to Contribute

You can help by:

* ✨ Adding new workflow templates
* 🚀 Improving existing templates
* 🐛 Fixing bugs
* 📖 Improving documentation
* 💡 Sharing automation ideas
* 🧪 Testing workflows

---

## Before You Start

Please make sure your workflow:

* Works correctly
* Uses placeholder credentials (never commit secrets)
* Includes a `README.md`
* Has a clear folder name
* Is easy to understand
* Is documented with setup instructions

---

## Repository Structure

```text
templates/
├── n8n/
│   └── workflow-name/
│       ├── workflow.json
│       └── README.md
├── make/
├── zapier/
└── other/
```

---

## Template Requirements

Every template should include:

* Workflow file (`.json`, `.yaml`, etc.)
* `README.md`
* Description
* Requirements
* Setup instructions
* Example use cases
* Optional integrations (if applicable)

---

## README Template

Each workflow README should answer:

* What does this workflow do?
* What services are required?
* How do I configure it?
* How do I use it?
* What does the output look like?

---

## Workflow Guidelines

Please follow these best practices:

* Keep workflows simple and modular.
* Use descriptive node names.
* Add comments or sticky notes for complex logic.
* Remove any personal or sensitive data.
* Replace API keys, tokens, IDs, and credentials with placeholders.
* Test your workflow before submitting.

---

## Submitting a Pull Request

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/my-workflow
```

3. Commit your changes.

```bash
git commit -m "Add n8n HubSpot enrichment workflow"
```

4. Push your branch.

```bash
git push origin feature/my-workflow
```

5. Open a Pull Request.

Please describe:

* What the workflow does
* Why it's useful
* Any dependencies
* Screenshots (optional)

---

## Reporting Issues

If you've found a bug or have an idea for improvement:

* Open an Issue
* Include steps to reproduce
* Describe the expected behavior
* Include screenshots if helpful

---

## Code of Conduct

Please be respectful and constructive.

We welcome contributors of all experience levels and aim to maintain a friendly, inclusive community.

---

## Questions?

If you have questions or need help, feel free to open an Issue or start a discussion.

Happy automating! 🚀
