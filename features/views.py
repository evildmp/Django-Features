import django.http as http
import django.shortcuts as shortcuts
from models import Request, Comment
from django.template import RequestContext

def request(request, slug):
    """
    Responsible for the person pages
    """
    print " -------- views.person --------"
    # the straightforward person attributes:            
    feature_request = Request.objects.get(slug=slug)
    return shortcuts.render_to_response(
        "features/request.html",
        {
            "feature_request":feature_request,
        },
        RequestContext(request),
        )
