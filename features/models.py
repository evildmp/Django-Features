from django.db import models
from django.contrib.auth.models import User
from cms.models.fields import PlaceholderField

class Request(models.Model):
    """A new request for the system"""
    title = models.CharField(max_length=50)
    slug = models.SlugField(help_text=u"Please leave blank/amend only if required", max_length=50, unique=True,)
    suggested_by = models.ForeignKey(User, related_name = 'suggested_request', verbose_name='Arkestra User')
    summary =  models.TextField(
        verbose_name = "Summary",
        max_length=256, 
        help_text = "A very short description of this request (maximum two lines)",)
    description = PlaceholderField('body',)
    suggested = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    STATUSES = (
        (0, 'Suggested'),
        (20, 'Under consideration'),
        (30, 'Started'),
        (40, 'Stalled'),
        (50, 'Completed'),
        )
    status = models.IntegerField(choices = STATUSES, default = 0)
    percent_complete = models.IntegerField(default=0)
    likely_cost = models.IntegerField(null = True, blank = True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/request/%s/" % self.slug

class Comment(models.Model):
    on = models.ForeignKey(Request, related_name = 'comment')
    by = models.ForeignKey(User, related_name = 'comment', verbose_name='Arkestra User')
    comment_text =  models.TextField(
        verbose_name = "Comment",
        max_length=256,)
    slug = models.SlugField(help_text=u"Please leave blank/amend only if required", max_length=50, unique=True,)
    suggested = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    PRIORITIES = (
        (-10, 'Bad idea'),
        (None, 'No particular priority'),
        (30, 'Low'),
        (40, 'Medium'),
        (50, 'High'),
        (50, 'Highest'),
        )
   
    priority = models.IntegerField(blank = True, null = True, choices = PRIORITIES)
    required_by = models.DateTimeField(null = True, blank = True)
    could_contribute = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.comment_text