# Notion Status Emoji Updater

This project uses the Notion API to update the emoji on database items based on the status field.

## Setup

1. Create a `.env` file with your Notion API key and database ID:
   ```
   NOTION_API_KEY=your-notion-api-key
   DATABASE_ID=your-database-id
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the script:
   ```
   python your_script.py
   ```

## GitHub Actions Automation

The project is configured to run automatically every 4 hours using GitHub Actions. The workflow file is located in `.github/workflows/run-script.yml`.
