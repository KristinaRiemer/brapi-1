# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class Ontology(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, authors: str=None, copyright: str=None, description: str=None, licence: str=None, ontology_db_id: str=None, ontology_name: str=None, version: str=None):  # noqa: E501
        """Ontology - a model defined in Swagger

        :param authors: The authors of this Ontology.  # noqa: E501
        :type authors: str
        :param copyright: The copyright of this Ontology.  # noqa: E501
        :type copyright: str
        :param description: The description of this Ontology.  # noqa: E501
        :type description: str
        :param licence: The licence of this Ontology.  # noqa: E501
        :type licence: str
        :param ontology_db_id: The ontology_db_id of this Ontology.  # noqa: E501
        :type ontology_db_id: str
        :param ontology_name: The ontology_name of this Ontology.  # noqa: E501
        :type ontology_name: str
        :param version: The version of this Ontology.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'authors': str,
            'copyright': str,
            'description': str,
            'licence': str,
            'ontology_db_id': str,
            'ontology_name': str,
            'version': str
        }

        self.attribute_map = {
            'authors': 'authors',
            'copyright': 'copyright',
            'description': 'description',
            'licence': 'licence',
            'ontology_db_id': 'ontologyDbId',
            'ontology_name': 'ontologyName',
            'version': 'version'
        }

        self._authors = authors
        self._copyright = copyright
        self._description = description
        self._licence = licence
        self._ontology_db_id = ontology_db_id
        self._ontology_name = ontology_name
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'Ontology':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ontology of this Ontology.  # noqa: E501
        :rtype: Ontology
        """
        return util.deserialize_model(dikt, cls)

    @property
    def authors(self) -> str:
        """Gets the authors of this Ontology.

        Ontology's list of authors (no specific format)  # noqa: E501

        :return: The authors of this Ontology.
        :rtype: str
        """
        return self._authors

    @authors.setter
    def authors(self, authors: str):
        """Sets the authors of this Ontology.

        Ontology's list of authors (no specific format)  # noqa: E501

        :param authors: The authors of this Ontology.
        :type authors: str
        """

        self._authors = authors

    @property
    def copyright(self) -> str:
        """Gets the copyright of this Ontology.

        Ontology copyright  # noqa: E501

        :return: The copyright of this Ontology.
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright: str):
        """Sets the copyright of this Ontology.

        Ontology copyright  # noqa: E501

        :param copyright: The copyright of this Ontology.
        :type copyright: str
        """

        self._copyright = copyright

    @property
    def description(self) -> str:
        """Gets the description of this Ontology.

        Human readable description of Ontology  # noqa: E501

        :return: The description of this Ontology.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Ontology.

        Human readable description of Ontology  # noqa: E501

        :param description: The description of this Ontology.
        :type description: str
        """

        self._description = description

    @property
    def licence(self) -> str:
        """Gets the licence of this Ontology.

        Ontology licence  # noqa: E501

        :return: The licence of this Ontology.
        :rtype: str
        """
        return self._licence

    @licence.setter
    def licence(self, licence: str):
        """Sets the licence of this Ontology.

        Ontology licence  # noqa: E501

        :param licence: The licence of this Ontology.
        :type licence: str
        """

        self._licence = licence

    @property
    def ontology_db_id(self) -> str:
        """Gets the ontology_db_id of this Ontology.

        Ontology database unique identifier  # noqa: E501

        :return: The ontology_db_id of this Ontology.
        :rtype: str
        """
        return self._ontology_db_id

    @ontology_db_id.setter
    def ontology_db_id(self, ontology_db_id: str):
        """Sets the ontology_db_id of this Ontology.

        Ontology database unique identifier  # noqa: E501

        :param ontology_db_id: The ontology_db_id of this Ontology.
        :type ontology_db_id: str
        """
        if ontology_db_id is None:
            raise ValueError("Invalid value for `ontology_db_id`, must not be `None`")  # noqa: E501

        self._ontology_db_id = ontology_db_id

    @property
    def ontology_name(self) -> str:
        """Gets the ontology_name of this Ontology.

        Ontology name  # noqa: E501

        :return: The ontology_name of this Ontology.
        :rtype: str
        """
        return self._ontology_name

    @ontology_name.setter
    def ontology_name(self, ontology_name: str):
        """Sets the ontology_name of this Ontology.

        Ontology name  # noqa: E501

        :param ontology_name: The ontology_name of this Ontology.
        :type ontology_name: str
        """
        if ontology_name is None:
            raise ValueError("Invalid value for `ontology_name`, must not be `None`")  # noqa: E501

        self._ontology_name = ontology_name

    @property
    def version(self) -> str:
        """Gets the version of this Ontology.

        Ontology version (no specific format)  # noqa: E501

        :return: The version of this Ontology.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this Ontology.

        Ontology version (no specific format)  # noqa: E501

        :param version: The version of this Ontology.
        :type version: str
        """

        self._version = version