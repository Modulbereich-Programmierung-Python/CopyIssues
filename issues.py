import time

from github import Github
token = Github('YOURTOKEN')  # FIXME
source_repo = token.get_repo('bzz-fgict/SOURCE')  # FIXME
target_repo = token.get_repo('bzz-fgict/TARGET')  # FIXME
issues = source_repo.get_issues(state='open', sort='created', direction='asc')
for issue in issues:
    '''target_repo.create_issue(
        issue.title,
        issue.body
    )'''
    print(issue.title)
    time.sleep(3)
