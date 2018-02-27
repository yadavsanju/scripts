# This script is used to perform the tasks which a developer performs on daily basis before starting
# starting terminal with the code folders
# starting google chrome with gmail(for communication) and keep(for notes)
# rubymine editor


import os

os.system("gnome-terminal --tab -e 'bash -c \"cd codebase; rails server; exec bash\"' --tab -e 'bash -c \"cd codebase; rails console; exec bash\"'")

os.system("gnome-terminal -e 'google-chrome www.gmail.com https://keep.google.com/u/0/'")

os.system("gnome-terminal --tab -e '/opt/rubymine/bin/rubymine.sh'")
