# -*- coding: utf-8 -*-

# Five & zope3 thingies
from zope import i18n
from zope.interface import implements
from Products.Five.browser  import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility

# CMF
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.utils import getToolByName

# plumi 0.3 
from interfaces import ICalloutView, ITopicsProvider

from plumi.app.config import TOPLEVEL_TAXONOMY_FOLDER, SUBMISSIONS_FOLDER
 

# Internationalization
_ = i18n.MessageFactory("plumi.skin")

class CalloutView( BrowserView ):
    u"""This browser view is used as utility for the callout view
    """
    implements( ICalloutView, ITopicsProvider )

    def __init__(self, context, request):
        super(CalloutView, self).__init__(context, request)
        self.context = context
        self.request = request
        self.portal_url = getToolByName(self.context, "portal_url")()
        self.vocab_tool = getToolByName(self.context, "portal_vocabularies")

        pprop = getUtility(IPropertiesTool)
        self.config = getattr(pprop, 'plumi_properties', None)
               #deprecated. will be removed 
        self.use_vpip = "vpip" in context.Subject()
        self.enclosure = None

    @property
    def categories(self):
        categories = self.context.getSubmissionCategories()
        if categories:
            return self.get_categories_dict(categories)
        return tuple()

    @property
    def review_state(self):
        wtool = getToolByName(self.context, "portal_workflow")
        return wtool.getInfoFor(self.context, 'review_state', None)

    @property
    def closing_date(self):
        date = self.context.closingDate
        return self.context.toLocalizedTime(date)

    def hasThumbnailImage(self):
        if getattr(self.context,'calloutImage',None) is None:
                return False
        imgfield = self.context.getField('calloutImage')
        #XXX test if the field is ok
        if imgfield is None or imgfield is '' or imgfield.getSize(self.context) == (0, 0):
                return False
        return True

    def get_categories_dict(self, cats):
        """Uses the portal vocabularies to retrieve the callout categories
        """
        voc = self.vocab_tool.getVocabularyByName('submission_categories')
        url = "%s/%s/%s/" % (self.portal_url,
                             TOPLEVEL_TAXONOMY_FOLDER, SUBMISSIONS_FOLDER)
        return (dict(id = cat_id,
                     url = url + cat_id,
                     title = voc[cat_id].Title()) for cat_id in cats)

