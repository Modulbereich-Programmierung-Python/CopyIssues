Scripts to copy issues from one repository to a target repository.

**Stand alone**

The python file can be run directly with the settings in .env

**GitHub workflow**

In '/.github/workflows/copyissues.yml' you find a GitHub workflow. 
- Copy this workflow to the target repository
- Change the ''SOURCE_REPO'' to a public repo with the issues you want to copy

**Settings:**
- GHSECRET: personal access token
- SOURCE_REPO: the source repository 
- TARGET_REPO: the target repository

**Remarks:**
- The 'time.sleep(n)' avoids too many requests in too short a time. Otherwise GitHub would abort with an error.
