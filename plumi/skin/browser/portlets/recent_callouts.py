from Products.CMFPlone.browser.interfaces import IRecentPortlet
from Products.CMFCore.utils import getToolByName

from zope.interface import implements
from Products.Five import BrowserView


class RecentCalloutsPortlet(BrowserView):
    implements(IRecentPortlet)

    def results(self):
        """ """
        context = utils.context(self)
        putils = getToolByName(context, 'plone_utils')
        portal_catalog = getToolByName(context, 'portal_catalog')
        typesToShow = 'Plumi Call Out'
        return self.request.get(
            'items',
            portal_catalog.searchResults(sort_on='effective',
	    				 review_state=['published','featured'],
                                         portal_type=typesToShow,
                                         sort_order='reverse',
                                         sort_limit=5)[:5])
