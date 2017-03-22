from django.shortcuts import render
from .utils import *

def story_list(request):
    rally = initRally()
    response = rally.get('UserStory', fetch =True)
    stories= {}
    if not response.errors:
        for story in response:
            for task in story.Tasks:
                stories['id'] = task.oid
                stories['name'] = task.Name
    else:
        stories = response.errors
    return render(request, 'blog/story_list.html',{'stories':stories})
