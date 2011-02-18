## Script (Python) "getActiveMembers"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Get a listing of the Active Members
##

from DateTime import DateTime
from Products.CMFCore.utils import getToolByName

def sortedDictValues(adict):
    """Helper function for the renderer
    """
    keys = adict.keys()
    keys.sort()
    keys.reverse()
    return map(adict.get, keys)

now = context.ZopeTime()
portal_catalog = getToolByName(context,'portal_catalog')
mtool = getToolByName(context,'portal_membership')
members = [member for member in mtool.listMembers() if not member.has_role(['Manager','Reviewer',])]
results = portal_catalog(created={ 'query' : [now - 30, now], 'range':'minmax'}
                         )
creators = []
thelist = []
for creator in results:
    creators.append(creator.Creator)
for item in members:
   thelist.append((creators.count(item), item))
adict = dict(thelist)
return sortedDictValues(adict)[:20]

