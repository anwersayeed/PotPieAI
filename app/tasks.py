from app.celery_app import celery
import httpx
from app.config import settings

GITHUB_API = "https://api.github.com"
headers = {
    "Authorization": f"token {settings.github_token}",
    "Accept": "application/vnd.github.v3+json"
}

@celery.task
def fetch_latest_pr():
    url = f"{GITHUB_API}/repos/{settings.github_repo}/pulls?state=open&sort=created&direction=desc&per_page=1"
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    prs = response.json()
    return prs[0] if prs else None

@celery.task
def fetch_pr_content(pr_number: int):
    url = f"{GITHUB_API}/repos/{settings.github_repo}/pulls/{pr_number}/files"
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    return response.json()