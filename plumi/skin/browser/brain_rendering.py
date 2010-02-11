# -*- coding: utf-8 -*-
from Acquisition import Explicit
from zope.interface import implements
from zope.component import adapts
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plumi.skin.browser.interfaces import IAbstractCatalogBrain
from interfaces import IPlumiVideoBrain, ITopicsProvider
from zope.component import getUtility
from Products.CMFCore.interfaces import IPropertiesTool

class PlumiVideoBrain( Explicit ):
    u"""Basic Plumi implementation of a video brain renderer.
    """
    
    implements(IPlumiVideoBrain)
    adapts(IAbstractCatalogBrain, ITopicsProvider)

    template = ViewPageTemplateFile('templates/video_brain.pt')
    __allow_access_to_unprotected_subobjects__ = True
    
    def __init__(self, context, provider):
        self.context = context
        self.video = context
        self.url = context.getURL()
        self.video_title = context.Title or context.id or 'Untitled'
        self.__parent__ = provider
        self.categories = provider.get_categories_info(context['getCategories'])
        self.countries = None
        pprop = getUtility(IPropertiesTool)
        self.config = getattr(pprop, 'plumi_properties', None)

    def render_listing(self):
        return self.template.__of__(self.context)(show_title=True,feature_video=False)
    
    def render(self):
        return self.template.__of__(self.context)(show_title=False,feature_video=False)

    def render_feature_video(self):
        return self.template.__of__(self.context)(show_title=False,feature_video=True)

    @property
    def country_dict(self):
        return self.__parent__.get_country_info(self.video['getCountries'])

    @property
    def post_date(self):
        date = self.video.created
        return self.context.toLocalizedTime(date)
        
    @property
    def videoserver(self):
        return self.config.videoserver_address        
        
