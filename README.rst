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

Test it out::

    python gradinator.py

Using in a script::

    from gradinator import Gradinator
    # Gradinator object expects a gituser name
    # and a git repo name, for example
    g = Gradinator("pigeonflight","gradinator")
    g.clone_repo()
    print "{} commits".format(g.commit_count())
    
