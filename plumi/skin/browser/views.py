from zope.interface import implements 
from zope.publisher.interfaces import IPublishTraverse
from ZPublisher import NotFound

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName


class Taxonomy(BrowserView):
    """A taxonomy view for countries, genres, etc"""
    implements(IPublishTraverse)
    template = ViewPageTemplateFile('templates/taxonomy.pt')
    
    def __init__(self, context, request): 
        self.context = context 
        self.request = request 
        self.traverse_subpath = []   
         
    def __call__(self, request=None, response=None):
        if not self.traverse_subpath:
            raise NotFound()
        
        if self.traverse_subpath[0] == 'genre':
            self.index = 'getGenre'
            self.name = 'genre'
            voc_name = 'video_genre'
        elif self.traverse_subpath[0] == 'countries':
            self.index = 'getCountries'
            self.name = 'country'
            voc_name = 'video_countries'
        elif self.traverse_subpath[0] == 'topic':
            self.index = 'getCategories'
            self.name = 'category'
            voc_name = 'video_categories'
        elif self.traverse_subpath[0] == 'lingua':
            self.name = 'language'
            self.index = 'getVideoLanguage'
            voc_name = 'video_languages'
        else:
            raise NotFound()
        
        pv = getToolByName(self.context, 'portal_vocabularies')
        self.voc = pv.getVocabularyByName(voc_name)
        
        if self.voc:
            items = self.voc.getDisplayList(self.context).items()
            self.results = []
            for i in items:
                self.results.append({'id':i[0], 'title':i[1]})
            return self.template()
        else:
            raise NotFound()
        
    def publishTraverse(self, request, name): 
        self.traverse_subpath.append(name) 
        return self   


class PublishView(BrowserView):
    """ View for /publish/type that redirects to the right URL """
    implements(IPublishTraverse)

    def __init__(self, context, request): 
        self.context = context 
        self.request = request 
        self.traverse_subpath = []
    
    def __call__(self, request=None, response=None):
        pm = getToolByName(self.context, 'portal_membership')
        home = pm.getHomeFolder()
        if 'news' in self.traverse_subpath:
            target = home.absolute_url()+'/news/createObject?type_name=News%20Item'
        elif 'event' in self.traverse_subpath:
            target = home.absolute_url()+'/events/createObject?type_name=Event'
        else:
            target = home.absolute_url()+'/videos/@@publish_video'

        self.request.response.redirect(target)

    def publishTraverse(self, request, name): 
        self.traverse_subpath.append(name) 
        return self    