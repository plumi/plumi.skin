# -*- coding: utf-8 -*-

# Five & zope3 thingies
from zope import i18n
from zope.interface import implements
from Products.Five  import BrowserView

# CMF
from Products.CMFCore.utils import getToolByName

# plumi 0.3 
from interfaces import IVideoView, ITopicsProvider

from plumi.app.config import TOPLEVEL_TAXONOMY_FOLDER, COUNTRIES_FOLDER, GENRE_FOLDER, CATEGORIES_FOLDER
 

# Internationalization
_ = i18n.MessageFactory("plumi.skin")

class VideoView( BrowserView ):
    u"""This browser view is used as utility for the atvideo view
    """
    implements( IVideoView, ITopicsProvider )


    def __init__(self, context, request):
        super(VideoView, self).__init__(context, request)
        self.portal_url = getToolByName(self.context, "portal_url")()
        self.vocab_tool = getToolByName(self.context, "portal_vocabularies")
        self.use_vpip = "vpip" in context.Subject()
        
	# XXX port to plumi.app.blob
        #media_info = context.getFileAttribs()
        #self.enclosure = media_info[1] > 0
	self.enclosure = None
        
        (self.transcoding_ready,
         self.transcoding_status) = self.get_transcoding_status()


    @property
    def categories(self):
        categories = self.context.getCategories()
        if categories:
            return self.get_categories_dict(categories)
        return tuple()

    @property
    def genres(self):
        """Actually, the genre is unique. We masquarade that.
        We might want the genre to be multivalued.
        """
        genres = self.context.getGenre()
        if genres:
            return self.get_genres_info((genres,))
        return tuple()

    @property
    def subjects(self):
        subjects = self.context.Subject()
        if subjects:
            return self.get_subjects_info(subjects)
        return tuple()

    @property
    def country(self):
        country_id = self.context.getCountry()
        if country_id:
            return self.get_country_info(country_id)
        return None

    @property
    def language(self):
        lang_id = self.context.Language()
        if lang_id:
            return self.get_country_info(lang_id)
        return None

    @property
    def review_state(self):
        wtool = getToolByName(self.context, "portal_workflow")
        return wtool.getInfoFor(self.context, 'review_state', None)

    @property
    def transcoding_rights(self):
        mtool  = getToolByName(self.context, "portal_membership")
        member = mtool.getAuthenticatedMember()
        mb_id  = member.getUserName()
        
        is_manager = 'Manager' in member.getRoles()
        is_owner   = mb_id in self.context.users_with_local_role('Owner')
	#return is_manager or is_owner
	#XXX make this an configurable option, ie settable thru a configelet whether or not owner can see 
	#this template
	#but for now just make it is_manager
	return is_manager

    @property
    def bt_availability(self):
	#XXX fix bittorrent functionality 

        #media_tool = getToolByName(self.context, "portal_atmediafiletool")
        #enabled_bt = media_tool.getEnable_bittorrent()
        #enable_ext_bt = media_tool.getEnable_remote_bittorrent()
        #bt_url = self.context.getTorrentURL()
	bt_url = ''
        
        #available = self.enclosure and (enabled_bt or enable_ext_bt)
	available = False
        return dict(available = available,
                    url = bt_url)


    def get_transcoding_status(self):
	# XXX fix transcoding support

        #statuses = TRANSCODING_STATUSES
        #status = str(self.context.getIndyTubeStatus())
        #if status in statuses:
        #    return statuses.get(status, (False, u""))
        return (False, u"")
   
    def get_categories_dict(self, cats):
        """Uses the portal vocabularies to retrieve the video categories
        """
        voc = self.vocab_tool.getVocabularyByName('video_categories')
        url = "%s/%s/%s/" % (self.portal_url,
                             TOPLEVEL_TAXONOMY_FOLDER, CATEGORIES_FOLDER)
        return (dict(id = cat_id,
                     url = url + cat_id,
                     title = voc[cat_id].Title()) for cat_id in cats)

    
    def get_genres_info(self, genres):
        """Uses the portal vocabularies to retrieve the video genres
        """
        voc = self.vocab_tool.getVocabularyByName('video_genre')
        url = "%s/%s/%s/" % (self.portal_url,
                             TOPLEVEL_TAXONOMY_FOLDER, GENRE_FOLDER)
        return (dict(id = genre_id,
                     url = url + genre_id,
                     title = voc[genre_id].Title()) for genre_id in genres)


    def get_subjects_info(self, subjects):
        """Fake the genres/categories process to return keywords infos
        """
        url = "%s/search?Subject=" % (self.portal_url)
        return (dict(id = kw,
                     url = url + kw,
                     title = kw) for kw in subjects)


    def get_country_info(self, country_id):
        """Fake the genres/categories process to return the country infos
        """
        country_tool = getToolByName(self.context, "portal_countryutils")
        country = country_tool.getCountryByIsoCode(country_id)
        url = "%s/%s/%s/" % (self.portal_url,
                             TOPLEVEL_TAXONOMY_FOLDER, COUNTRIES_FOLDER)
        return dict(id = country_id,
                    url = url + country_id,
                    title = country.name)


    def get_language_info(self, lang_id):
        """Fake the genres/categories process to return the language infos
        """
        voc = self.vocab_tool.getVocabularyByName('video_language')
        language = voc[lang_id].Title()
        return dict(id = lang_id,
                    url = None,
                    title = language)

    @property
    def post_date(self):
	date = self.context.created
        return self.context.toLocalizedTime(date)

    def hasThumbnailImage(self):
	if getattr(self.context,'thumbnailImage',None) is None:
		return False
	imgfield = self.context.getField('thumbnailImage')
	#XXX test if the field is ok
	return True
