from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, url_name):
    """Return classes for active/inactive nav items based on current URL name.

    Usage in template:
      {% load nav_active %}
      <a class="base-classes {% active 'my_url_name' %}" href="...">...

    The tag requires `request` in the template context (the project already includes
    `django.template.context_processors.request`).
    """
    request = context.get('request')
    if not request:
        return ''
    resolver = getattr(request, 'resolver_match', None)
    current = getattr(resolver, 'url_name', '') if resolver else ''
    if current == url_name:
        return 'bg-primary/20 text-primary'
    # default/inactive classes
    return 'text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-white/10'
