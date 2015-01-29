import requests
import git
class Gradinator:
    """ class for grading github """
    def __init__(self, username, repo):
        self.username = username
        self.repo = repo
        api_for_commits = "https://api.github.com/repos/{}/{}/commits"
        self.github_repo = "git@github.com:{}/{}.git"
        self.commit_url = api_for_commits.format(username,repo)

    def extract_username(self,commit):
        """ extract username from commits in json message """
        if commit['author']:
            return commit['author']['login']
        return ""
   
    def commits(self):
        r = requests.get(self.commit_url)
        commits = r.json()
        #Filter data by username
        return [commit for commit in commits 
                 if self.extract_username(commit) 
                                  == self.username]
       
    def count(self):
        return len(self.commits())

    def clone_repo(self):
        repo_url = self.github_repo.format(self.username,self.repo)
        git.Git().clone(repo_url)
    
if __name__ == "__main__":
    g = Gradinator("pigeonflight","gradinator")
    g.clone_repo()
    print "{} commits".format(g.count())
    


