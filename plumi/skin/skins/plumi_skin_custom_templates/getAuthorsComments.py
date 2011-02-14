## Script (Python) "getAuthorsComments"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=author
##title=Get a listing of the Authors last 10 comments
##

from Products.CMFCore.utils import getToolByName
catalog = getToolByName(context, 'portal_catalog')

results = catalog.searchResults(sort_on='modified',
                                portal_type='Discussion Item',
                                Creator=author,
                                sort_order='reverse',
                                sort_limit=10)[:10]

return results


