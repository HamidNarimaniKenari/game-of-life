
import os
import sys

def pushUpdatedRevisionToGithub(revision):
    print revision     
    os.system('git add test1.xml')
    os.system('git commit -m "Update revision  number to' + str(revision) + '"')
    os.system('git tag ' + str(revision))
    os.system('git push --tags')

newRev=10
print newRev
pushUpdatedRevisionToGithub(newRev)

