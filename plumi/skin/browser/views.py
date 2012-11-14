from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from AccessControl import getSecurityManager
from collective.transcode.star.interfaces import ITranscodeTool
from zope.component import getUtility

class Taxonomy(BrowserView):
    """A taxonomy view for countries, genres, etc"""

