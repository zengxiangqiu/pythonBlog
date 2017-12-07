from ..models import Post,Category,Tag
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
	
@register.simple_tag	
def archives():
    return Post.objects.dates('created_time','month',order= 'DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_count_of_category(category_pk):
    return Post.objects.filter(category = category_pk).count()

@register.simple_tag
def get_tags():
    return Tag.objects.all()