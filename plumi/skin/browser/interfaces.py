# -*- coding: utf-8 -*-
from zope.interface import Interface, Attribute
from zope.publisher.interfaces.browser import IBrowserView
from plone.theme.interfaces import IDefaultPloneLayer
 
class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""

class IAbstractCatalogBrain( Interface ):
    u"""Marker interface
    """

class IVideoView( Interface ):
    u"""Gathers useful properties from the video and format them for
    display purposes. The lists are all made the same way. They are
    lists of dicts. The dict has 3 keys : title, url and id. Values
    are strings.
    """
    categories = Attribute("The list of categories linked to the video.")
    genres = Attribute("The list of genres linked to the video.")
    subjects = Attribute("The list of subjects linked to the video.")
    language = Attribute("The language of the video. Returns a dict if "
                         "the language exists. None otherwise.")
    country = Attribute("The country where the video is from. "
                        "Returns a dict if country exists. None otherwise.")
    use_vpip = Attribute("Boolean.")
    enclosure = Attribute("Boolean determining if the video enclosure has a "
                          "length. See ATMediaFile.content.mediafile for more "
                          "info.")

    transcoding_rights = Attribute("Boolean representing the right to see "
                                   "transcoding information.")
    transcoding_status = Attribute("Status of the video transcoding.")
    transcoding_result = Attribute("Boolean representing the transcoding "
                                   "results.")

    bt_availability = Attribute("A dict giving info about the BT status of the"
                                " file. It's a dict with two keys.")

class IVideosProvider( Interface ):
    u"""This interface defines a content types able to generate a list of
    videos.
    """
    videos = Attribute("""An iterable of Video Brain Renderers""")


class ITopicsProvider( Interface ):
    u"""The browser views implementing this interface have for mission
    to retrieve a list of categories with all the linked infos from the
    adapted object.
    """
    def get_categories_info(categories):
        u"""Returns a list of dict representing a category.
        The dict contains 3 strings : title, url and id.
        @params : iterable of category ids
        """

    def get_country_info(countries):
        u"""Returns a list of dict representing a country.
        The dict contains 3 strings : title, url and id.
        @params : iterable of country ids
        """

    __parent__ = Attribute(
        """The view the provider appears in.

        The view is the third discriminator of the content provider. It allows
        that the content can be controlled for different views.

        Having it stored as the parent is also very important for the security
        context to be kept.
        """)

class IFeaturedVideosRetriever( IBrowserView, ITopicsProvider ):
    u"""This interface defines a featured videos retriever.
    It will fetch the lastest reviewed video, the news and
    the list of the latest videos on the site.
    """
    portal_url = Attribute(u"The url of the portal root.")
    
    featured_items = Attribute(u"The current highlighted items.")
    
    news_and_events = Attribute(u"A list of events and news to display.")
    
    latest_videos = Attribute(u"A list of the latest videos to display.")
    
    featured_video_url = Attribute(u"The url of the page for the featured "
                                   u"videos.")
    
    listing_video_url = Attribute(u"The url of the page listing all the "
                                  u"videos.")
        
class IAuthorPage( Interface ):
    u"""This interface defines a page that is meant to grab an author's
    items and infos out of the catalog and membership tool.
    """
    author = Attribute(u"The id of the author.")
    videos = Attribute(u"A list of the author's videos to display.")
    portrait = Attribute(u"The portrait of the author")
    member_info = Attribute(u"The full infos about the author.")
    homefolder = Attribute(u"The homefolder, if it exists, of the author.")
    # custom attributes
    author_url = Attribute(u" ")
    author_street = Attribute(u" ")
    author_phone = Attribute(u" ")
    author_city = Attribute(u" ")
    author_postcode = Attribute(u" ")
    author_genre_interests = Attribute(u" ")
    author_activities = Attribute(u" ")
    author_media_formats = Attribute(u" ")
    author_userbio = Attribute(u" ")


class IPlumiVideoBrain( Interface ):
    u"""Video Brain Renderer. This multiadapter takes care of rendering a brain
    representing a video, in its context. The context has to be category-aware.
    There are two ways of rendering the brain. See below.
    """
    video = Attribute(u"The video being rendered.")
    video_title = Attribute(u"the title of the video.")
    url = Attribute(u"the url of the video.")
    categories = Attribute(u"A list of the video categories. "
                           u"See ITopicsProvider for more details")
    country = Attribute(u"A list of the video country. "
                           u"See ITopicsProvider for more details")


    def render():
        u"""Renders the video brain using the template. Calling this
        method will render the template passing the option 'show_title'
        as False, so the title of the video won't be rendered.
        """

    def render_feature_video():
        u"""Renders the video brain using the template. Calling this
        method will render the template passing the option 'show_title'
        as False, so the title of the video won't be rendered, and with 'feature_video' 
	set True to enable the flash video player, or whatever needs to be conditionally pulled in.
        """

    def render_listing():
        u"""Renders the video brain using the template. Calling this
        method will render the template passing the option 'show_title'
        as True, so the title of the video will be rendered. It is mainly
        used in listings, as the name suggest.
        """
