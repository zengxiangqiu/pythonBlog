from django.contrib.syndication.views import Feed
from .models import Post

class LastestPostsFeed(Feed):
    title = "zengxiangqiu's blog"
    link = '/'
    description = 'Update Posts to blog'
    
    def items(self):
        return Post.objects.all()[:5]
    
    def item_title(self, item):
        return '[%s] %s | %s' % (item.category,item.title,item.created_time)
    
    def item_description(self, item):
        return item.body
    

    
    