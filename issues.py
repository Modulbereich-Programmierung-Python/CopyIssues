import time

from github import Github


def main():
    token = Github('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')
    source_repo = token.get_repo('bzz-fgict/LU12_A03_Lottery')
    target_repo = token.get_repo('bzz-fgict/gruppenaufgabe-m319_lu12_a03_lottery-test')
    source_issues = source_repo.get_issues(state='open', sort='created', direction='asc')
    target_issues = target_repo.get_issues(state='open', sort='created', direction='asc')
    for issue in source_issues:
        if not issue_exists(target_issues, issue.title):
            target_repo.create_issue(
                issue.title,
                issue.body
            )
            print(issue.title)
            time.sleep(1)


def issue_exists(target_issues, title):
    for issue in target_issues:
        if issue.title == title:
            return True
    return False
