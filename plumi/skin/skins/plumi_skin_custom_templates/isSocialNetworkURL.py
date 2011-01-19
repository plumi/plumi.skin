## Script (Python) "isSocialNetworkURL"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=url

"""
simple test of a link to see if it is a major social network url
"""
if 'facebook.com' in url:
    return 'facebook-link'
elif 'myspace.com' in url:
    return 'myspace-link'
elif 'twitter.com' in url:
    return 'twitter-link'
elif 'orkut.com' in url:
    return 'orkut-link'
elif 'delicious.com' in url:
    return 'delicious-link'
else:
    return 'homepage-link'
