from django import template

register = template.Library();

@register.simple_tag(takes_context=True)
def get_links(context):
    request = context['request']
    links = [
        {
            'name': 'Store',
            'href': '/store/',
            'icon': 'fa-store',
            'desc': 'Featured Games'
        },
        {
            'name': 'My Library',
            'href': '/library/',
            'icon': 'fa-book',
            'desc': 'Your Game Collection'
        },
        {
            'name': 'Community',
            'href': '/forum',
            'icon': 'fa-users',
            'desc': 'Forum & Discussion'
        },
        {
            'name': 'Report Bug',
            'href': '/news/',
            'icon': 'fa-triangle-exclamation',
            'desc': 'Report Issues'
        },
        {
            'name': 'Request Game',
            'href': '/request-game/',
            'icon': 'fa-gamepad',
            'desc': 'Suggest a Game'
        },
        {
            'name': 'About',
            'href': '/about',
            'icon': 'fa-circle-info',
            'desc': 'About CoCo'
        },
    ]
    
    # Add admin panel link if user is authenticated and is staff
    if request.user.is_authenticated and request.user.is_staff:
        links.append({
            'name': 'Admin Panel',
            'href': '/admin-panel/',
            'icon': 'fa-sliders',
            'desc': 'Admin Dashboard'
        })
    
    return links
    