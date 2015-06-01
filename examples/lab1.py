from gradinator import Gradinator
import csv
import os
token = os.getenv('GIT_TOKEN')
# you need a token to use the github api
# generate token at https://github.com/settings/tokens

with open('lab1.csv', 'rb') as csvfile:
    submissions = csv.reader(csvfile, delimiter=',',quotechar='"')
    next(submissions, None)  # skip the headers
    for submission in submissions:
        fullrepourl = submission[4].strip()
        timestamp = submission[0].strip()
        first = submission[1].strip()
        last = submission[2].strip()

        g = Gradinator(fullrepourl=fullrepourl,token=token)
        g.clone_repo()
        print "{} {} {} {} commits".format(timestamp,first,last,g.commit_count())

# To use this script run "python lab1.py"
# currently assumes that dependencies are installed and that gradinator.py 
# is in the same directory as lab1.py
