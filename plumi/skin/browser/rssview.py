##################################################################################
#
#    Copyright (C) 2007-2009 Andy Nicholson, EngageMedia Collective Inc., All rights reserved.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
##################################################################################

__author__  = '''Andy Nicholson'''
__docformat__ = 'plaintext'
__version__   = '$ Revision 0.0 $'[11:-2]

try:
    from Products.Five.browser import BrowserView
except ImportError:
    from zope.app.publisher.browser import BrowserView
from collective.contentlicensing.browser import RSSView as DefaultRSSView
from Products.CMFCore.utils import getToolByName
import types

class RSSView(DefaultRSSView):
    """ Implements ATVideo RSS view """

    def getRSSObjects(self):
        """ Get RSS objects. """
        portal_catalog = getToolByName( self, 'portal_catalog' )
        #constrain the videos selected to be the path of the view context
        if self.aq_parent.portal_type == 'Plumi Video Folder':
            path = "/".join(self.aq_parent.getPhysicalPath())
            #brains = portal_catalog.searchResults(path=path, portal_type='PlumiVideo', sort_on='getFirstPublishedTransitionTime', sort_order='reverse' )
            brains = portal_catalog.searchResults(path=path, portal_type='PlumiVideo', sort_order='reverse' )
        else:
            syn_tool = getToolByName( self, 'portal_syndication' )
            #assume its a topic, self.aq_parent
            if self.aq_parent.portal_type == 'Topic':
                #limit = int(syn_tool.getMaxItems(self))
                #use qRSS2Syndication.utils to get the 'syndication_information' tool, for now, since we
                #have set this up for all the folders/topics in the ATVideo installer
                syinfo = getattr(self.aq_parent, 'syndication_information', None)
                if syinfo is not None:
                    limit = syinfo.max_items
                else:
                    limit = 10
                brains = self.aq_parent.queryCatalog(sort_limit=limit)[:limit]
            else:
                #XXX what other containers do we support for RSS views?
                brains = []
        #ONLY RETURN BRAINS!!
        bb = []
        for b in brains: 
            #check the custom catalog attribute (see catalog_extension.py)
            # we return the dict attached to the custom metadata, for use in the RSSView
            x=getattr(b,'isPublishableATEngageVideoObj',None)
            if x is not None and type(x)==types.DictType and x['published'] is True:
                bb.append(b)
            if x is None:
                #we are not dealing with ATVideo objects, so just add them into the results
                #
                bb.append(b)
        return bb
        
    def defaultLicense(self):
        """ get default site license """
        pprops = getToolByName(self, 'portal_properties')
        return pprops.content_licensing_properties.getProperty('DefaultSiteLicense', None)

    def emailFromAdress(self):        
        urltool = getToolByName(self.context, 'portal_url')
        portal = urltool.getPortalObject()
        return portal.getProperty('email_from_address', None)        
        
    def videoserver(self):
        pprops = getToolByName(self, 'portal_properties')
        config = getattr(pprops, 'plumi_properties', None)
        if config:
            return config.videoserver_address            
        return None
