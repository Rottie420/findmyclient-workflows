import time
import requests

BASE_URL = "https://findmyclient.org/api"
API_TOKEN = "YOUR-API-TOKEN"


def search(query: str):
    # 1. Start job
    res = requests.post(
        f"{BASE_URL}/search",
        params={
            "query": query,
            "token": API_TOKEN,
            "max_pages": 10,
            "max_websites": 10,
            "max_results": 10,
        },
        timeout=30,
    )
    res.raise_for_status()
    job_id = res.json()["job_id"]

    print("Job started:", job_id)

    # 2. Poll status
    while True:
        res = requests.get(f"{BASE_URL}/result/{job_id}", timeout=30)
        res.raise_for_status()
        data = res.json()

        print("Status:", data.get("status"))

        if data.get("status") == "completed":
            if data.get("error"):
                raise Exception(data["error"])
            break

        if data.get("status") == "failed":
            raise Exception(data.get("error", "Job failed"))

        # waiting for response to avoid rate-limit.
        time.sleep(30)  

    # 3. Get results
    res = requests.get(f"{BASE_URL}/result/leads/{job_id}", timeout=30)
    res.raise_for_status()

    return res.json()


if __name__ == "__main__":
    result = search("singapore cafe")

    for row in result.get("rows", []):
        print(row)