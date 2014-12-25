from django.template.defaulttags import register


@register.filter
def real_name(user):
    if user.first_name and user.last_name:
        return "{} {}".format(user.first_name, user.last_name)
    else:
        return user.username