"""
Used to transform data based on contents of the transformation configuration 
file.

"""
import json
import logging
import os.path

import constants

LOGGER = logging.getLogger(__name__)


def validateType(dataType):
    """ Transformation types are different CKAN object types that can be 
    configured for transformations.  They are referred to as strings.  This 
    method verifies that the strings line up with a valid type.
    
    
    :param dataType: [description]
    :type dataType: [type]
    """
    if dataType not in constants.VALID_TRANSFORM_TYPES:
        msg = (
            f"a transformation type of: {dataType} was specified however "
            + "this is not a valid transformation type.  Valid options are: "
            + f"{constants.VALID_TRANSFORM_TYPES}"
        )
        raise InValidTransformationTypeError(msg)

def getTransformationConfig(transformConfigFile=None):
    """Loads the transformation configuration information from the config file
    
    :return transConfData: the transformation configuration data loaded from 
        the transformation config file
    :rtype: dict
    """
    if transformConfigFile is None:
        transformConfigFile = os.path.join(
            os.path.dirname(__file__),
            "..",
            constants.TRANSFORM_CONFIG_DIR,
            constants.TRANSFORM_CONFIG_FILE_NAME,
        )
    with open(transformConfigFile) as json_file:
        transConfData = json.load(json_file)
    return transConfData

class TransformDataSet:
    def __init__(self, dataType, transformData, transformConfigFile=None):
        self.validateType(dataType)
        self.dataType = dataType
        self.transformData = transformData

        if not isinstance(self.transformData, list):
            msg = "transformation data needs to be a list data type, " + \
                  f"transformData provided is type: {type(transformData)}"
            raise InValidTransformationData(msg)



    def getComparisonData(self):
        """removed machine generated data from the data allowing for comparison
        between two instances.
        """
        comparisonData = []
        for datasetItem in self.transformData:




    # TODO: make an iterator that returns transform records

class TransformationConfig:
    """Reads the transformation config file and provides methods to help 
    retrieve the desired information from the configuration.
    """

    def __init__(self, transformationConfigFile=None):
        self.transConf = getTransformationConfig(transformConfigFile)

    def __getProperties(self, datatype, section, sectionValue):
        retData = None
        if datatype in self.transConf:
            if section in self.transConf[datatype]:
                properties = self.transConf[datatype][section]
                retData = []
                for field in properties:
                    if properties[field] == sectionValue:
                        retData.append(field)
        return retData

    def getUserPopulatedProperties(self, datatype):
        """If the user populated parameters are defined in the config file for 
        the given datatype they will be returned.  If they are not defined then
        will return None.
        
        :param datatype: [description]
        :type datatype: [type]
        :return: [description]
        :rtype: [type]
        """

        validateType(datatype)
        section = constants.TRANSFORM_PARAM_USER_POPULATED_PROPERTIES
        userPopulated = self.__getProperties(datatype, section, True)
        return userPopulated

    def getAutoPopulatedProperties(self, datatype):
        """retrieves from the transformation config file the fields that are 
        defined as auto / machine generated.  These are fields that cannot
        be populated directory.  Example of a autogenerated field could be
        "Modification Date"
        
        :param datatype: The datatype. Valid data types are defined in the
            constants file in the parameter VALID_TRANSFORM_TYPES
        :type datatype: str
        :return: a list of fields that are defined in the config file as auto / 
            machine populated.
        :rtype: list, str
        """
        validateType(datatype)
        section = constants.TRANSFORM_PARAM_USER_POPULATED_PROPERTIES
        userPopulated = self.__getProperties(datatype, section, False)
        return userPopulated


class TransformRecord:

    def __init__(self, datatype, record, transformationConfig):
        self.validateType(datatype)
        self.record = record
        self.transformationConfig = transformationConfig


    def getComparisonRecord(self):
        usrFields = self.transformationConfig.getUserPopulatedProperties(datatype)




    


class InValidTransformationTypeError(AttributeError):
    def __init__(self, message):
        self.message = message

class InValidTransformationData(AttributeError):
    def __init__(self, message):
        self.message = message

