from gradinator import Gradinator
import csv
import os
with open('lab1.csv', 'rb') as csvfile:
    submissions = csv.reader(csvfile)
    for submission in submissions:
        fullrepourl = submission[0]

#username=pigeonflight
#repo=gradinator
#token = "XXXXXXXXX" # generate token at https://github.com/settings/tokens
token = os.getenv('GIT_TOKEN')
g = Gradinator(fullrepourl=fullrepourl,token=token)
g.clone_repo()
print "{} commits".format(g.commit_count())
