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
	#new way. XXX
	#self.author = (len(request.traverse_subpath) > 0 and url_unquote_plus(request.traverse_subpath[0])) or request.get('author', None)	
	self.logging = logging.getLogger('plumi.skin.browser.author')
	self.member = self.context['acl_users'].getUserById(self.author)

    @property
    def author_url(self):
    	url=self.member.getProperty('url')
        if len(url)> 0 and not url[:7]=='http://':
                return 'http://'+url
        else:
                return url
    @property
    def author_street(self):
	return self.member.getProperty('street')

    @property
    def author_phone(self):
	return self.member.getProperty('phone')

    @property
    def author_userbio(self):
	    return self.member.getProperty('userbio')

    @property
    def author_city(self):
	return self.member.getProperty('city')

    @property
    def author_postcode(self):
	return self.member.getProperty('postcode')

    @property
    def author_genre_interests(self):
	#XXX make sure its ALWAYS a list
	return self.member.getProperty('genre_interests')

    @property
    def author_activities(self):
	#XXX make sure its ALWAYS a list
	return self.member.getProperty('activities')

    @property
    def author_media_formats(self):
	#XXX make sure its ALWAYS a list
	return self.member.getProperty('media_formats')

    @property
    def author_userbio(self):
	return self.member.getProperty('userbio')

    @property
    def videos(self):
        query = dict(portal_type='PlumiVideo',
                     sort_on='effective',
                     sort_order='reverse',
                     Creator=self.author,
                     review_state='published')
        brains = self.catalog(**query)[:5]
        return [queryMultiAdapter((brain, self), IPlumiVideoBrain)
                for brain in brains]

    @property
    def callouts(self):
        query = dict(portal_type='PlumiCallOut',
                     sort_on='effective',
                     sort_order='reverse',
                     Creator=self.author,
                     review_state='published')
        brains = self.catalog(**query)[:5]
        return brains
        
    @property
    def portrait(self):
        return self.mtool.getPersonalPortrait(self.author)

    @property
    def member_info(self):
        return self.mtool.getMemberInfo(self.author)

    @property
    def homefolder(self):
        return self.mtool.getHomeFolder(id=self.author)

    @property
    def news(self):
        query = dict(portal_type='News Item',
                     sort_on='effective',
                     sort_order='reverse',
                     Creator=self.author,
                     review_state='published')
        brains = self.catalog(**query)[:5]
        return brains

    @property
    def events(self):
        query = dict(portal_type='Event',
                     sort_on='effective',
                     sort_order='reverse',
                     Creator=self.author,
                     review_state='published')
        brains = self.catalog(**query)[:5]
        return brains

