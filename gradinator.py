import git
import requests

class Gradinator:
    """ class for grading github """
    def __init__(self, username, repo):
        self.username = username
        self.repo = repo
        api_for_commits = "https://api.github.com/repos/{}/{}/commits"
        self.github_repo = "git@github.com:{}/{}.git"
        self.commit_url = api_for_commits.format(username,repo)


    def clone_repo(self):
        repo_url = self.github_repo.format(self.username,self.repo)
        git.Git().clone(repo_url)
   
    def commits(self):
        r = requests.get(self.commit_url)
        commits = r.json()
        #Filter data by username
        return [commit for commit in commits 
                 if self.extract_username(commit) 
                                  == self.username]

    def commit_count(self):
        return len(self.commits())

    def extract_username(self,commit):
        """ extract username from commits in json message """
        if commit['author']:
            return commit['author']['login']
        return ""

    
if __name__ == "__main__":
    # this is just a test
    g = Gradinator("pigeonflight","gradinator")
    g.clone_repo()
    print "{} commits".format(g.commit_count())
    


