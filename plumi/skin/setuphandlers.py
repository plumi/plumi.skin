import logging
from Products.CMFCore.utils import getToolByName

def setupVarious(context):
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    portal = context.getSite()
    logger = logging.getLogger('plumi.skin')

    #create and publish the Projects folder if it is not already there
    wftool = getToolByName(portal,'portal_workflow')
    try:    
        projects = portal.invokeFactory("Folder", "Projects")
        wftool.doActionFor(portal[projects],action='publish')
    except:
        pass
