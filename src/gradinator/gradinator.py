import argparse
import textwrap
import git
import requests
import tempfile
import time

 
def RateLimited(maxPerSecond):
    """ rate limit function, borrowed from https://gist.github.com/gregburek/1441055 """
    minInterval = 1.0 / float(maxPerSecond)
    def decorate(func):
        lastTimeCalled = [0.0]
        def rateLimitedFunction(*args,**kargs):
            elapsed = time.clock() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.clock()
            return ret
        return rateLimitedFunction
    return decorate
 

class Gradinator:
    """ class for grading github """
    def __init__(self, fullrepourl="", username="", repo="", token=""):
        self.username = username
        self.repo = repo
        self.fullrepourl = fullrepourl
        api_for_commits = "https://api.github.com/repos/{}/{}/commits"
        self.github_repo = "git@github.com:{}/{}.git"

        if self.fullrepourl != "":
           reposplit = self.fullrepourl.split('/')
           if len(reposplit) < 2:
               print "something is wrong with the url: {}".format(fullrepourl)
           else:
               username = reposplit[3]
               repo = reposplit[4].split('.')[0]

        self.commit_url = api_for_commits.format(username,repo)
        self.token = token
        self.headers = {'Authorization': 'token %s' % self.token}

    #def login(self)

    def clone_repo(self):
        repo_url = self.github_repo.format(self.username,self.repo)
        if self.fullrepourl != "":
            repo_url = self.fullrepourl
        #git.Git().clone(repo_url)

        repo_dir = tempfile.mkdtemp(prefix='gradinator_')
        git.Repo.clone_from(repo_url, repo_dir)
   
    def commits(self):
        r = requests.get(self.commit_url,headers=self.headers)
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
    description = """\
    Import the session data from a CSV file, given the path.
    """
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(description)
    )
    parser.add_argument('github_token')
    token = parser.parse_args().github_token
    g = Gradinator("pigeonflight","gradinator",token)
    g.clone_repo()
    print "{} commits".format(g.commit_count())
