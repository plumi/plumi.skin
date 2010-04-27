# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.component import adapts
from Products.ATContentTypes.interface.topic import IATTopic
from Products.ATContentTypes.interface.folder import IATFolder
from interfaces import IVideosProvider
from Products.CMFCore.utils import getToolByName

# ported from PlumiSkin 0.2.x trunk - 17/7/09

class TopicVideosProvider( object ):
    adapts(IATTopic)
    implements(IVideosProvider)

    def __init__(self, context):
        """It would be much better not to count on the acquisition and
        old python script, and recode this part.
        """
        self.videos = context.queryCatalog(batch=True)


class OrderedFolderVideosProvider( object ):
    adapts(IATFolder)
    implements(IVideosProvider)

    def __init__(self, context):
        """It would be much better not to count on the acquisition and
        old python script, and recode this part.
        """
	if context.portal_type == 'PlumiVideoFolder':
		path = "/".join(context.getPhysicalPath())
	
		content_filter = dict()	
		content_filter['path'] = path 
		content_filter['portal_type']='PlumiVideo'
		content_filter['sort_on'] = 'created'
		content_filter['sort_order'] = 'reverse'
		self.videos = context.getFolderContents(batch=True,contentFilter=content_filter)

	else:
        	self.videos = context.getFolderContents(batch=True)
        

