# -*- coding: utf-8 -*-

# Five & zope3 thingies
from zope.interface import implements
from plumi.content.browser.taxonomy import CategoriesProvider
from zope.component import queryMultiAdapter
from Products.CMFCore.utils import getToolByName
from plumi.content.browser.interfaces import IAuthorPage, IPlumiVideoBrain
import logging
from zope.location.interfaces import LocationError


class AuthorPage(CategoriesProvider):
    u"""This browser view is used to gather informations about
    the items posted by a particular author.
    """

    implements(IAuthorPage)

    def __init__(self, context, request):
        super(AuthorPage, self).__init__(context, request)
        self.catalog = getToolByName(self.context, "portal_catalog")
        self.mtool = getToolByName(self.context, 'portal_membership')
        #old way
        self.author = (len(request.traverse_subpath) > 0 and
                       request.traverse_subpath[0] or
                       request.get('author', None))
        """new way. XXX
        self.author = (len(request.traverse_subpath) > 0 and
                       url_unquote_plus(request.traverse_subpath[0])) or
                       request.get('author', None)
        """
        self.logging = logging.getLogger('plumi.content.browser.author')
        self.member = self.context['acl_users'].getUserById(self.author)

    @property
    def author_url(self):
        url = self.member.getProperty('url')
        if len(url) > 0 and not url[:7] == 'http://':
            return 'http://' + url
        else:
            return url

    @property
    def author_homepages_display(self):
        u""" this should contain logic for working out popular
        social network URL's for later enhancements
        """
        full_urls = []
        for url in self.member.getProperty('homepages'):
            #XXX we do > 1 to remove possible empty first field from display
            # this should be cleaner
            if len(url) > 1 and not url[:7] == 'http://':
                full_urls.append('http://' + url)
            else:
                full_urls.append(url)
        return full_urls

    @property
    def author_homepages(self):
        for url in self.member.getProperty('homepages'):
            if len(url) > 0 and not url[:7] == 'http://':
                return 'http://' + url
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
    def author_paypal(self):
        return self.member.getProperty('author_paypal')

    @property
    def videos(self):
        try:
            homeurl = '/'.join(self.mtool.getHomeFolder(id=self.author).getPhysicalPath())
            query = dict(portal_type='PlumiVideo',
                         path={'query': homeurl},
                         sort_on='effective',
                         sort_order='reverse',
                         review_state=['published', 'featured'])
            brains = self.catalog(**query)[:20]
            return [queryMultiAdapter((brain, self), IPlumiVideoBrain)
                    for brain in brains]
        except LocationError:
            return []

    @property
    def callouts(self):
        try:
            homeurl = '/'.join(self.mtool.getHomeFolder(id=self.author).getPhysicalPath())
            query = dict(portal_type='PlumiCallOut',
                         path={'query': homeurl},
                         sort_on='effective',
                         sort_order='reverse',
                         review_state=['published', 'featured'])
            brains = self.catalog(**query)[:5]
            return brains
        except LocationError:
            return []

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
        homeurl = '/'.join(self.mtool.getHomeFolder(id=self.author).getPhysicalPath())
        query = dict(portal_type='News Item',
                     path={'query': homeurl},
                     sort_on='effective',
                     sort_order='reverse',
                     review_state=['published', 'featured'])
        brains = self.catalog(**query)[:5]
        return brains

    @property
    def events(self):
        try:
            homeurl = '/'.join(self.mtool.getHomeFolder(id=self.author).getPhysicalPath())
            query = dict(portal_type='Event',
                         path={'query': homeurl},
                         sort_on='effective',
                         sort_order='reverse',
                         review_state=['published', 'featured'])
            brains = self.catalog(**query)[:5]
            return brains
        except LocationError:
            return []
