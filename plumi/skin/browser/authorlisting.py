from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class AuthorListing(BrowserView):
        
    def content_item_id(self):
        return self.context.getId()
    
    def user_agent(self):
        return self.request.get('HTTP_USER_AGENT','')

    def returnUserData(self,intype=None,invalue=None):
        """ returns a list of user data dictionaries """
                
        mtool = getToolByName(self.context, 'portal_membership')
        fieldDict = {'genre':'genre_interests',
                     'activities':'activities',
                     'mediaformats':'media_formats',
                     'location':'location',
                     'language':'language',
                    }
        resultList = []                    
        users = mtool.listMembers()
        for user in users:
            category = fieldDict[intype]
            if category == 'language':
                categoryValues = mtool.getMemberInfo(user.getId())['language']
            else:
                categoryValues = user.getProperty(category)
            if invalue in categoryValues:
                resultDict = {}
                user_id = user.getId()
                resultDict['userid'] = user_id
                resultDict['city'] = user.getProperty('city')
                resultDict['location'] = user.getProperty('location')           
                resultDict['home_folder'] = mtool.getHomeFolder(id=user_id).absolute_url()
                resultDict['user_portrait'] = mtool.getPersonalPortrait(user_id).absolute_url()
                resultList.append(resultDict)
        return resultList
