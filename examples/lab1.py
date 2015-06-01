username=pigeonflight
repo=gradinator
token = "XXXXXXXXX"
g = Gradinator(username,repo,token=token)
g.clone_repo()
print "{} commits".format(g.commit_count())
