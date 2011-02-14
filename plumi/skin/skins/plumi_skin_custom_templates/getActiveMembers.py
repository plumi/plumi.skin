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

def pastmonthdate(d):
    year, month= d.year(), d.month()
    if month == 1:
        year-= 1; month= 12
    else:
        month-= 1
    try:
        return d.replace(year=year, month=month)
    except ValueError:
        return d.replace(day=1) - DateTime.timedelta(1)

now = context.ZopeTime()
portal_catalog = getToolByName(context,'portal_catalog')
brains = portal_catalog.uniqueValuesFor('Creator')
results = portal_catalog(created={ 'query' : [now - 30, now], 'range':'minmax'}
                         )
creators = []
thelist = []
for creator in results:
    creators.append(creator.Creator)
for item in brains:
   thelist.append((creators.count(item), item))
adict = dict(thelist)
return sortedDictValues(adict)[:20]

