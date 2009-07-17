# -*- coding: utf-8 -*-
from zope.component import queryMultiAdapter
from plumi.skin.browser.interfaces import IVideosProvider, IPlumiVideoBrain
from taxonomy import CategoriesProvider

class VideosListing( CategoriesProvider ):
    u"""This browser view is convenient to fetch videos informations
    necessary to the display of a videos provider.
    """    
    def __init__(self, context, request):
        super(VideosListing, self).__init__(context, request)
        self.videos = IVideosProvider(context).videos
        self.empty = bool(not self.videos)
 
    @property
    def renderers(self):
        """Batch prevents us to only returns a list of renderers.
        This list of renderers is the one to iterate if a rendering
        is wanted.
        """
        return [queryMultiAdapter((brain, self), IPlumiVideoBrain)
                for brain in self.videos]
     
    @property
    def parent_url(self):
        return self.context.navigationParent(self.context,
                                             "video_listing_view")

