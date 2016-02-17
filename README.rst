Gradinator
==============
The beginnings of an auto grading system
The idea is to measure quantity of commits
using the github api and quality of commits
using unit tests that can be "fed" to the 
Gradinator object

Currently it assumes that the code being assessed is written in Python.


Usage
===========
Install requirements::

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Test it out (where XXXXXXXXXXXXXXXX must be replaced with your custom github token)::

    python gradinator.py XXXXXXXXXXXXXXXXXXXX

Using in a script::

    from gradinator import Gradinator
    # Gradinator object expects a github user name
    # and a github repo name (just the basename)
    # the example below runs against 
    # http://github.com/pigeonflight/gradinator
    # You need to pass a github token to the Gradinator object
    from gradinator import Gradinator
    import os
    token = os.getenv('GIT_TOKEN')
    username = pigeonflight # username can also be an organization name
    repo = gradinator
    g = Gradinator(username,repo,token=token)
    g.clone_repo()
    print "{} commits".format(g.commit_count())

Using in a script with fullrepourl::

    from gradinator import Gradinator
    # Gradinator object expects a github user name
    # and a github repo name (just the basename)
    # the example below runs against 
    # http://github.com/pigeonflight/gradinator
    # You need to pass a github token to the Gradinator object
    import os
    token = os.getenv('GIT_TOKEN')
    fullrepourl = "https://github.com/pigeonflight/gradinator"
    g = Gradinator(fullrepourl=fullrepourl,token=token)
    g.clone_repo()
    print "{} commits".format(g.commit_count())

If you need to generate a token visit: https://github.com/settings/tokens
    
See the scripts in the `examples` folder
The scripts assume that an env variable has been set called ``GIT_TOKEN``
You can set it with the following command:

    export GIT_TOKEN=xxxxxxxxxxxxxxxxx
    
replace the placeholder with your generated token
