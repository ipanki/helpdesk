from celery import shared_task

from issues.models import Issue


@shared_task
def pause_issue(issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.pause()
    issue.save()
    return True


@shared_task
def resolve_issue(issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.resolve()
    issue.save()
    return True


@shared_task
def reopen_issue(issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.reopen()
    issue.save()
    return True
