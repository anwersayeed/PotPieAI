import httpx
from app.config import settings

GITHUB_API = "https://api.github.com"

headers = {
    "Authorization": f"token {settings.github_token}",
    "Accept": "application/vnd.github.v3+json"
}

async def get_latest_pr():
    url = f"{GITHUB_API}/repos/{settings.github_repo}/pulls?state=open&sort=created&direction=desc&per_page=1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        prs = response.json()
        return prs[0] if prs else None

async def get_pr_files(pr_number: int):
    url = f"{GITHUB_API}/repos/{settings.github_repo}/pulls/{pr_number}/files"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()