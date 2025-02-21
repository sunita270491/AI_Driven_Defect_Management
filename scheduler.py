import schedule
import time
import requests

def fetch_defects():
    # Fetch defect data from management tool (e.g., Jira, Azure DevOps)
    defects = []
    # Example: Fetching defects from a mocked endpoint
    response = requests.get("https://api.mocked_defect_tool.com/defects")
    if response.status_code == 200:
        defects = response.json()
    return defects

def analyze_defects():
    defects = fetch_defects()
    if defects:
        response = requests.post("http://localhost:8000/analyze", json=defects)
        if response.status_code == 200:
            analysis_results = response.json()
            for defect_id, result in analysis_results.items():
                if result == "Update Required":
                    notify_developer(defect_id)

def notify_developer(defect_id):
    # Send notification to developer
    print(f"Notification sent for defect ID: {defect_id}")

schedule.every(10).minutes.do(analyze_defects)

while True:
    schedule.run_pending()
    time.sleep(1)