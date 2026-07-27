from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from blog.models import Post


class RssPostsFeeds(Feed):
    title = "posts"
    link = "/posts/"
    description = "newest posts"

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content , 20)

    def item_lastupdated(self, item):
        return item.updated_at