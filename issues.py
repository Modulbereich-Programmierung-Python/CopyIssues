import time

from github import Github


def main():
    token = Github('YOURSECRET') # FIXME
    source_repo = token.get_repo('bzz-fgict/SOURCE') # FIXME
    target_repo = token.get_repo('bzz-fgict/TARGET') # FIXME
    source_issues = source_repo.get_issues(state='open', sort='created', direction='asc')
    target_issues = target_repo.get_issues(state='open', sort='created', direction='asc')
    for issue in source_issues:
        if not issue_exists(target_issues, issue.title):
            target_repo.create_issue(
                issue.title,
                issue.body
            )
            print(issue.title)
            time.sleep(5)


def issue_exists(target_issues, title):
    for issue in target_issues:
        if issue.title == title:
            return True
    return False


if __name__ == '__main__':
    main()
