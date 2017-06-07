# puppy-shelter-db

Use python and SQLAlchemy to set up and populate a database for adopting puppies, and perform queries on the database.

**This project makes use of the Linux-based virtual machine (VM), you'll need VirtualBox, Vagrant installed in advance.**

## Start Guide:
* Put all files into a folder "puppy-shelter" inside vagrant subdirectory
* From your terminal, inside the vagrant subdirectory, run the command vagrant up
* When vagrant up is finished running, run vagrant ssh to log in to your Linux VM
* Inside the VM, change directory to \vagrant (cd \vagrant), and then cd puppy-shelter
* Download and run command python puppypopulator.py to populate database with puppies and shelters
* Run command python puppy_query.py
