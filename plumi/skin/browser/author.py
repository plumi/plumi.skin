# -*- coding: utf-8 -*-

# Five & zope3 thingies
from zope.interface import implements
from taxonomy import CategoriesProvider
from zope.component import queryMultiAdapter
from Products.CMFCore.utils import getToolByName
from interfaces import IAuthorPage, IPlumiVideoBrain
import logging


class AuthorPage( CategoriesProvider ):
    u"""This browser view is used to gather informations about
    the items posted by a particular author.
    """
    implements(IAuthorPage)
    
    def __init__(self, context, request):
        super(AuthorPage, self).__init__(context, request)
        self.catalog = getToolByName(self.context, "portal_catalog")
        self.mtool = getToolByName(self.context, 'portal_membership')
	#old way
        self.author = (len(request.traverse_subpath) > 0 and request.traverse_subpath[0] or request.get('author', None))
	#new way
	#self.author = (len(request.traverse_subpath) > 0 and url_unquote_plus(request.traverse_subpath[0])) or request.get('author', None)	
	self.logging = logging.getLogger('plumi.skin.browser.author')

    @property
    def author_city(self):
	self.logging.info('author_city , %s ' % self.author)
	self.member = self.context['acl_users'].getUserById(self.author)
	return self.member.getProperty('city')

    @property
    def videos(self):
        query = dict(portal_type='PlumiVideo',
                     sort_on='getFirstPublishedTransitionTime',
                     sort_order='reverse',
                     Creator=self.author,
                     review_state='published')
        brains = self.catalog(**query)
        return [queryMultiAdapter((brain, self), IPlumiVideoBrain)
                for brain in brains]

    @property
    def portrait(self):
        return self.mtool.getPersonalPortrait(self.author)

    @property
    def member_info(self):
        return self.mtool.getMemberInfo(self.author)

    @property
    def homefolder(self):
        return self.mtool.getHomeFolder(id=self.author)
