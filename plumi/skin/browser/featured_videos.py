# -*- coding: utf-8 -*-

# Five & zope3 thingies
from zope.interface import implements
from zope.component import queryMultiAdapter
from taxonomy import CategoriesProvider

# CMF
from Products.CMFCore.utils import getToolByName

# Locally
from interfaces import IFeaturedVideosRetriever, IPlumiVideoBrain
#from plumi.app.config import *


class FeaturedVideosPage( CategoriesProvider ):
    u"""This browser view is used to gather informations about
    the existing videos and latest addition. It gets the infos
    out of the portal catalog.
    """
    implements( IFeaturedVideosRetriever )

    limit_latest  = 7
    limit_featured = 1
    target = "featured"

    def __init__(self, context, request):
        super(FeaturedVideosPage, self).__init__(context, request)
        # General utils
        portal = context.portal_url.getPortalObject()
        self.catalog = getToolByName(context, "portal_catalog")
        self.target_exists = (self.target in portal.contentIds()
                              and True or False)

    @property
    def featured_video_url(self):
        if self.target_exists:
            return "%s/%s" % (self.portal_url, self.target)
        return "%s/%s" % (self.portal_url, "featured-videos")

    @property
    def listing_video_url(self):
        if self.target_exists:
            return "%s/%s" % (self.portal_url, "latest")
        return "%s/%s" % (self.portal_url, "latestvideos")
    
    @property
    def featured_items(self):
        filtering = dict(portal_type='PlumiVideo',
                         Subject='featured',
                         sort_on='created',
                         sort_order='reverse',
                         review_state='published',
                         limit=self.limit_featured)
        brains = self.catalog(filtering)[:self.limit_featured]
        return [queryMultiAdapter((brain, self), IPlumiVideoBrain)
                for brain in brains]

    @property
    def news_and_events(self):
        filtering = dict(portal_type=['News Item','Event'],
                         sort_on='Date',
                         Subject='featured',
                         sort_order='reverse',
                         review_state='published',
                         limit=1)
        return self.catalog(filtering)[:1]

    @property
    def latest_videos(self):
        filtering = dict(portal_type='PlumiVideo',
                         sort_on='created',
                         sort_order='reverse',
                         review_state='published',
                         limit=self.limit_latest)
        brains = self.catalog(filtering)[:self.limit_latest]
        return [queryMultiAdapter((brain, self), IPlumiVideoBrain)
                for brain in brains]
