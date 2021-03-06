"""tests the actual api calls to CKAN.

"""

import CKAN
import logging
import pprint

LOGGER = logging.getLogger(__name__)

''' 
---------------------------------------------------------  
Because you cannot actually delete a user it is impossible to test
adding a user. 
---------------------------------------------------------
def test_addUser(CKANData_Test_User_Data_Raw, CKAN_Dest_fixture):
    """Tests ability to add new users to the CKAN instance through the 
    API. 

    Uses a bunch of test data.  Fixtures should clean this up. after the test
    through additional api calls.
    
    :param CKANData_User_Data_Raw: [description]
    :type CKANData_User_Data_Raw: [type]
    :param CKAN_Dest_fixture: [description]
    :type CKAN_Dest_fixture: [type]
    """
    LOGGER.debug("user data: %s", pprint.pformat(CKANData_Test_User_Data_Raw))
    # because users cannot be deleted, there is no real way to test adding 
    # a user.  The logic used so far has worked.
    retVal = CKAN_Dest_fixture.addUser(CKANData_Test_User_Data_Raw)
    LOGGER.debug("return value from user add: %s", retVal)
'''
def test_getUser(CKAN_Dest_fixture, CKANData_Test_User_Data_Raw, CKANAddTestUser):
    """Tests the ability to retrieve a user
    """
    user = CKAN_Dest_fixture.getUser(CKANData_Test_User_Data_Raw['name'])
    LOGGER.debug("users: %s", user)
    assert user['name'] == CKANData_Test_User_Data_Raw['name']

def test_updateUser(CKAN_Dest_fixture, CKANData_Test_User_Data_Raw,
                    CKANAddTestUser, CKANDeleteTestUser):
    """ Will test an update of a field associated with a user.  

    fixture: CKANAddTestUser
      - makes sure the user exists and calls delete after yield

    The fixture CKANDeleteTestUser will:
      - ensure the user exists
      - also calls delete after yield
      
    """
    LOGGER.info("user data: %s", CKANData_Test_User_Data_Raw)
    updateValue = CKAN_Dest_fixture.updateUser(CKANData_Test_User_Data_Raw)
    LOGGER.info("updateValue: %s", updateValue)

def test_userExists(CKAN_Dest_fixture, CKANData_Test_User_Data_Raw, CKANDeleteTestUser):
    LOGGER.debug("CKANData_Test_User_Data_Raw: %s", CKANData_Test_User_Data_Raw)
    assert not CKAN_Dest_fixture.userExists("does not exist user")
    assert CKAN_Dest_fixture.userExists(CKANData_Test_User_Data_Raw['name'])

