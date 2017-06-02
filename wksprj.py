import sys
from pyral import Rally, rallyWorkset

workspaces = Rally.getWorkspaces()
for wksp in workspaces:
    print ("%s %s" % (wksp.oid, wksp.Name))
    projects = Rally.getProjects(workspace=wksp.Name)
    for proj in projects:
        print ("    %12.12s  %s" % (proj.oid, proj.Name))
