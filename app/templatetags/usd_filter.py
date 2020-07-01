from django import template

register=template.Library()


@register.filter()
def rep(value,arg):
    return value.replace(arg,'f')



#register.filter('replacing',rep)

# represent data in lower case

def lower(value):
    return value.lower()

register.filter('lowerr',lower)


@register.filter(name='pre')
def prefix(value):
    return 'Mr/Ms '+value

@register.filter(name='counting')
def count(value,arg):
    c=0
    for i in range(len(value)-len(arg)+1):
        if value[i:i+len(arg)]==arg:
            c+=1
    return c



























