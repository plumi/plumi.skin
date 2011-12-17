"""This package adds extensions to portal_catalog.
"""
import logging
from Products.ATContentTypes.interface.news import IATNewsItem
from plone.indexer.decorator import indexer

@indexer(IATNewsItem)
def hasImageAndCaptionForNews(object,**kw):
    logger=logging.getLogger('plumi.skin.indexes')
    logger.info('hasImageAndCaptionForNews - have %s ' % object )
    
    img = object.getImage()
    #check that the image is set
    if img is not None and img is not '':
        caption = object.getImageCaption() or u''
        md = {'image': True, 'caption': caption }
    else:
        md = {'image': False, 'caption': u''}

    logger.info(' hasImageAndCaptionForNews returning %s  . thumbnail object is %s' % (md, object.getImage()))
    return md
