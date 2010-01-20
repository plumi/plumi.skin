# -*- coding: utf-8 -*-
from zope.interface import implements
from Products.Five.browser  import BrowserView
from Products.CMFCore.utils import getToolByName
from plumi.app.config import TOPLEVEL_TAXONOMY_FOLDER, CATEGORIES_FOLDER, COUNTRIES_FOLDER
from interfaces import ITopicsProvider

import types

class CategoriesProvider( BrowserView ):
    """A basic implementation of a category provider
    """
    implements( ITopicsProvider )
    
    def __init__(self, context, request):
        super(CategoriesProvider, self).__init__(context, request)
        purl = getToolByName(context, "portal_url")
        self.portal_url = purl()
        
        # Categories and genres utils
        vocabulary_tool = getToolByName(context, "portal_vocabularies")
        self.cats_voc = vocabulary_tool.getVocabularyByName('video_categories')
        self.cats_url = "%s/%s/%s/" % (self.portal_url, TOPLEVEL_TAXONOMY_FOLDER, 
                                       CATEGORIES_FOLDER)

        self.country_tool = getToolByName(context, "portal_countryutils")

    def get_categories_info(self, cats):
        #make a check its a tuple        
        if type(cats) is types.TupleType:
            return (dict(id = cat_id,
                    url = self.cats_url + cat_id,
                    title = self.cats_voc[cat_id].Title()) for cat_id in cats)
        return dict()

    def get_country_info(self, country_id):
        """Fake the genres/categories process to return the country infos
        """
        if not country_id or len(country_id.strip())==0:
            return None
        country = self.country_tool.getCountryByIsoCode(country_id)
        url = "%s/%s/%s/" % (self.portal_url, TOPLEVEL_TAXONOMY_FOLDER, COUNTRIES_FOLDER)
        return dict(id = country_id, url = url + country_id, 
                    title = country.name)
