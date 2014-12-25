from django.template.defaulttags import register
import markdown


@register.filter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    return markdown.markdown(text, safe_mode='escape') 