""" from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from website.models import Contact


class RssContactFeeds(Feed):
    title = "Contact Message"
    link = "/contact/"
    description = "User Messages"

    def items(self):
        return Contact.objects.all()

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.message

    def item_lastupdated(self, item):
        return item.created_date
    
    def item_link (self,item):
        return'/contact/' """