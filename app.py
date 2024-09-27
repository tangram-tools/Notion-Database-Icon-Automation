import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

STATUS_EMOJI = {
    "Not started": "🔹",
    "In progress": "⏳",
    "Done": "✅"
}

def update_page_emoji(page_id, status, current_emoji):
    emoji = STATUS_EMOJI.get(status, "")
    
    # Only update if the emoji does not match the status
    if emoji != current_emoji:
        data = {
            "icon": {
                "type": "emoji",
                "emoji": emoji
            } if emoji else None
        }
        
        url = f"https://api.notion.com/v1/pages/{page_id}"
        response = requests.patch(url, headers=HEADERS, json=data)
        
        if response.status_code == 200:
            print(f"Page {page_id} updated with emoji {emoji}")
        else:
            print(f"Failed to update page: {response.status_code}, {response.text}")
    else:
        print(f"No update needed for page {page_id}, emoji is already correct.")

def get_database_items():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print(f"Failed to retrieve database items: {response.status_code}, {response.text}")
        return []

def main():
    pages = get_database_items()
    
    for page in pages:
        # Assuming status is stored in a property called 'Status'
        status = page["properties"]["Status"]["status"]["name"]
        page_id = page["id"]
        
        icon_info = page.get("icon")
        current_emoji = icon_info["emoji"] if icon_info and icon_info.get("type") == "emoji" else ""

        update_page_emoji(page_id, status, current_emoji)

if __name__ == "__main__":
    main()