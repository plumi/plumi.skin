import logging

def setupHome(portal, out):
    """ set default homepage 
    """
    portal.setLayout('featured_videos_homepage')

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('plumi.skin_various.txt') is None:
        return

    portal = context.getSite()
    logger = logging.getLogger('plumi.skin')

    setupHome(portal, logger)
    # Add additional setup code here
