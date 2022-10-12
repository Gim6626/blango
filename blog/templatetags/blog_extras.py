from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape
from django.utils.safestring import mark_safe
user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, user_model):
        return ""
    else:
        if author == current_user:
            name = 'me'
        elif author.first_name and author.last_name:
            name = f'{author.first_name} {author.last_name}'
        else:
            name = author.username
        if author.email:
            return mark_safe(f'<a href="mailto:{escape(author.email)}">{name}</a>')
            #prefix = format_html('<a href="mailto:{}">', author.email)
            #suffix = format_html("</a>")
        else:
            return name
