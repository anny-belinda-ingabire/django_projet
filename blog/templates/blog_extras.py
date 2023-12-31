from django,template import library

register = Library()


@register.filter
def model_type(value):
    return type(value).__name__

@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'you'
    return user.username