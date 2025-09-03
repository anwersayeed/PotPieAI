from fastapi import APIRouter
from app.tasks import fetch_latest_pr, fetch_pr_content
from app.celery_app import celery

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/latest-pr/analyze")
def analyze_latest_pr():
    """
    Start async task to fetch latest PR metadata.
    """
    task = fetch_latest_pr.delay()
    return {"task_id": task.id, "status": "started"}

@router.get("/pr/{pr_number}/analyze")
def analyze_pr(pr_number: int):
    """
    Start async task to fetch files for a given PR.
    """
    task = fetch_pr_content.delay(pr_number)
    return {"task_id": task.id, "status": "started"}

@router.get("/task/{task_id}")
def get_task_status(task_id: str):
    """
    Check task status and get results when complete.
    """
    task = celery.AsyncResult(task_id)
    if task.state == "PENDING":
        return {"task_id": task_id, "status": "pending"}
    elif task.state == "SUCCESS":
        return {"task_id": task_id, "status": "completed", "result": task.result}
    else:
        return {"task_id": task_id, "status": task.state}