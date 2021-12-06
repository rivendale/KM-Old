import os
from django import template
from ..models import Files
from datetime import datetime
from django.utils.html import format_html 
register = template.Library()

@register.simple_tag
def model(post):
    if len(Files.objects.filter(post=post)) != 0:
        return Files.objects.filter(post=post)
    else:
        return ''


@register.simple_tag
def timestamp(created_at):
    time = datetime.now()
    if created_at.day == time.day:
        return str(time.hour - created_at.hour) + " hours ago"
    else:
        if created_at.month == time.month:
            return str(time.day - created_at.day) + " days ago"
        else:
            if created_at.year == time.year:
                return str(time.month - created_at.month) + " months ago"
    return created_at


@register.simple_tag
def file_type(file):
    fileName, fileExtension = os.path.splitext(file.name)
    video_list = ['.ogm','.wmv', '.mpg', '.webm','.ogv','.mov','.asx', '.mpeg', '.mp4', '.m4v', '.avi']
    image_list = ['.tiff', '.pjp', '.fif', '.gif', '.svg', '.bmp', '.png', '.jpeg', '.svgz', '.jpg', '.webp', '.ico', '.xbm', '.dib','.tif','.pjpegavif']
    if fileExtension in image_list:
        return 'image'
    elif fileExtension in video_list:
        return 'video'

