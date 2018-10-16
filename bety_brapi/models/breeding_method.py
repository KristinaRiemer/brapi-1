# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class BreedingMethod(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, abbreviation: str=None, breeding_method_db_id: str=None, breeding_method_name: str=None, description: str=None, name: str=None):  # noqa: E501
        """BreedingMethod - a model defined in Swagger

        :param abbreviation: The abbreviation of this BreedingMethod.  # noqa: E501
        :type abbreviation: str
        :param breeding_method_db_id: The breeding_method_db_id of this BreedingMethod.  # noqa: E501
        :type breeding_method_db_id: str
        :param breeding_method_name: The breeding_method_name of this BreedingMethod.  # noqa: E501
        :type breeding_method_name: str
        :param description: The description of this BreedingMethod.  # noqa: E501
        :type description: str
        :param name: The name of this BreedingMethod.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'abbreviation': str,
            'breeding_method_db_id': str,
            'breeding_method_name': str,
            'description': str,
            'name': str
        }

        self.attribute_map = {
            'abbreviation': 'abbreviation',
            'breeding_method_db_id': 'breedingMethodDbId',
            'breeding_method_name': 'breedingMethodName',
            'description': 'description',
            'name': 'name'
        }

        self._abbreviation = abbreviation
        self._breeding_method_db_id = breeding_method_db_id
        self._breeding_method_name = breeding_method_name
        self._description = description
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'BreedingMethod':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The breedingMethod of this BreedingMethod.  # noqa: E501
        :rtype: BreedingMethod
        """
        return util.deserialize_model(dikt, cls)

    @property
    def abbreviation(self) -> str:
        """Gets the abbreviation of this BreedingMethod.

        an abbreviation for the name of this breeding method  # noqa: E501

        :return: The abbreviation of this BreedingMethod.
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation: str):
        """Sets the abbreviation of this BreedingMethod.

        an abbreviation for the name of this breeding method  # noqa: E501

        :param abbreviation: The abbreviation of this BreedingMethod.
        :type abbreviation: str
        """

        self._abbreviation = abbreviation

    @property
    def breeding_method_db_id(self) -> str:
        """Gets the breeding_method_db_id of this BreedingMethod.

        the unique identifier for this breeding method  # noqa: E501

        :return: The breeding_method_db_id of this BreedingMethod.
        :rtype: str
        """
        return self._breeding_method_db_id

    @breeding_method_db_id.setter
    def breeding_method_db_id(self, breeding_method_db_id: str):
        """Sets the breeding_method_db_id of this BreedingMethod.

        the unique identifier for this breeding method  # noqa: E501

        :param breeding_method_db_id: The breeding_method_db_id of this BreedingMethod.
        :type breeding_method_db_id: str
        """
        if breeding_method_db_id is None:
            raise ValueError("Invalid value for `breeding_method_db_id`, must not be `None`")  # noqa: E501

        self._breeding_method_db_id = breeding_method_db_id

    @property
    def breeding_method_name(self) -> str:
        """Gets the breeding_method_name of this BreedingMethod.

        human readable name of the breeding method  # noqa: E501

        :return: The breeding_method_name of this BreedingMethod.
        :rtype: str
        """
        return self._breeding_method_name

    @breeding_method_name.setter
    def breeding_method_name(self, breeding_method_name: str):
        """Sets the breeding_method_name of this BreedingMethod.

        human readable name of the breeding method  # noqa: E501

        :param breeding_method_name: The breeding_method_name of this BreedingMethod.
        :type breeding_method_name: str
        """

        self._breeding_method_name = breeding_method_name

    @property
    def description(self) -> str:
        """Gets the description of this BreedingMethod.

        human readable description of the breeding method  # noqa: E501

        :return: The description of this BreedingMethod.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this BreedingMethod.

        human readable description of the breeding method  # noqa: E501

        :param description: The description of this BreedingMethod.
        :type description: str
        """

        self._description = description

    @property
    def name(self) -> str:
        """Gets the name of this BreedingMethod.

        DEPRECATED in v1.3 - Use \"breedingMethodName\"  # noqa: E501

        :return: The name of this BreedingMethod.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BreedingMethod.

        DEPRECATED in v1.3 - Use \"breedingMethodName\"  # noqa: E501

        :param name: The name of this BreedingMethod.
        :type name: str
        """

        self._name = name