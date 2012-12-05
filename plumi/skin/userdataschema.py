from zope.interface import Interface, implements
from zope import schema

from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from Products.CMFCore.utils import getToolByName
from five import grok

@grok.provider(IContextSourceBinder)
def genres(context):
    pv = getToolByName(context.context, 'portal_vocabularies')
    voc_genres = pv.getVocabularyByName('video_genre')
    terms = []
    voc_terms = voc_genres.getDisplayList(context).items()
    terms = [SimpleTerm(value=term[0], token=term[0], title=term[1])
                     for term in voc_terms]
    return SimpleVocabulary(terms)

@grok.provider(IContextSourceBinder)
def activities(context):
    pv = getToolByName(context.context, 'portal_vocabularies')
    voc_activities = pv.getVocabularyByName('video_categories')
    terms = []
    voc_terms = voc_activities.getDisplayList(context).items()
    terms = [SimpleTerm(value=term[0], token=term[0], title=term[1])
                     for term in voc_terms]
    return SimpleVocabulary(terms)

@grok.provider(IContextSourceBinder)
def formats(context):
    pv = getToolByName(context.context, 'portal_vocabularies')
    voc_formats = pv.getVocabularyByName('submission_categories')
    terms = []
    voc_terms = voc_formats.getDisplayList(context).items()
    terms = [SimpleTerm(value=term[0], token=term[0], title=term[1])
                     for term in voc_terms]
    return SimpleVocabulary(terms)

@grok.provider(IContextSourceBinder)
def homepages(context):
    mt = getToolByName(context.context, 'portal_membership')
    member = mt.getMemberById(context.context.getId())
    voc_homepages = member.getProperty('homepages')
    return SimpleVocabulary(voc_homepages)

class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    author_paypal = schema.TextLine(
        title=u'Paypal Id',
        required=False,
    )

    genre_interests = schema.List(
        title=u'Interests',
        value_type=schema.Choice(source=genres),
        required=False,
    )

    activities = schema.List(
        title=u'Activities',
        value_type=schema.Choice(source = activities),
        required=False,
    )

    media_formats = schema.List(
        title=u'Media Formats',
        value_type=schema.Choice(source = formats),
        required=False,
    )

    homepages = schema.List(
        title=u'Social Media links',
        value_type=schema.URI(),
        required=False,
    )
