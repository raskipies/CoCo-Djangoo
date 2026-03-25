from django import template

register = template.Library();

@register.simple_tag
def get_links():
    return [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'Features',
        'href': '/features/',
        'icon': 'fa-star',
    }, {
        'name': 'Cars',
        'href': '/cars',
        'icon': 'fa-car',
    }, {
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
    },{
        'name': 'Bug Forum',
        'href': '/news/',
        'icon': 'fa-newspaper',
    },{
        'name': 'Add Your Bug!',
        'href': '/news/create',
        'icon': 'fa-plus',
    },{
        'name': 'Forum',
        'href': '/forum',
        'icon': 'fa-comment', #look for your icon here https://fontawesome.com/search?ic=free
    },{
        'name': 'Request Game',
        'href': '/request-game/',
        'icon': 'fa-gamepad',
    }]
    