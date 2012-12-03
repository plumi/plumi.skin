from zope.interface import implements 
from zope.component import getMultiAdapter
from zope.publisher.interfaces import IPublishTraverse

from ZPublisher import NotFound

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

try:
    import simplejson as json
except:
    import json

from plumi.content.browser.video import VideoView

class JSONResults(BrowserView):
    def __call__(self, request=None, response=None):
        brains = self.context.queryCatalog(self.request, batch=True)
        results = []
        for brain in brains:
            date = brain.effective.year() > 1000 and brain.effective or brain.created
            try:
                countries = VideoView(self.context, self.request).get_country_info(brain.getCountries)
            except:
                countries = False

            results.append({
                'id': brain.getId,
                'uid': brain.UID,
                'url': brain.getURL(),
                'portal_type': brain.portal_type,
                'title': brain.Title == "" and brain.id or brain.Title,
                'description': brain.Description,
                'duration': brain.videoDuration,
                'countries': countries,
                'date': self.context.toLocalizedTime(date),
                'is_folderish': brain.is_folderish,
                })
        # return results in JSON format
        self.context.REQUEST.response.setHeader("Content-type",
                                                "application/json")            
        return json.dumps(results)

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
            self.name = ''
            self.results = [{'id': 'genre','title': 'Genre'},
                            {'id': 'topic','title': 'Topic'},
                            {'id': 'countries','title': 'Countries'},
                            {'id': 'lingua','title': 'Language'},
                            ]
            return self.template()
        
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
        portal_state = getMultiAdapter((self.context, self.request), 
                                       name="plone_portal_state")
        home = portal_state.member().getHomeFolder()
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
