Gradinator
==============
The beginnings of an auto grading system

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
    
