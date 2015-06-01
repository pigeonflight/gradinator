from gradinator import Gradinator
username=pigeonflight
repo=gradinator
token = "XXXXXXXXX" # generate token at https://github.com/pigeonflight/gradinator
g = Gradinator(username,repo,token=token)
g.clone_repo()
print "{} commits".format(g.commit_count())
