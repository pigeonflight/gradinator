from gradinator import Gradinator
import csv
import os
with open('lab1.csv', 'rb') as csvfile:
    submissions = csv.reader(csvfile, delimiter=',',quotechar='"')
    for submission in submissions:
        fullrepourl = submission[4].strip()
 

token = os.getenv('GIT_TOKEN')
# generate token at https://github.com/settings/tokens
g = Gradinator(fullrepourl=fullrepourl,token=token)
g.clone_repo()
print "{} commits".format(g.commit_count())
