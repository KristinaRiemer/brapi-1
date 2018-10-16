# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class VendorSpecificationReferenceSystem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uri: str=None, name: str=None, reference_system_name: str=None):  # noqa: E501
        """VendorSpecificationReferenceSystem - a model defined in Swagger

        :param uri: The uri of this VendorSpecificationReferenceSystem.  # noqa: E501
        :type uri: str
        :param name: The name of this VendorSpecificationReferenceSystem.  # noqa: E501
        :type name: str
        :param reference_system_name: The reference_system_name of this VendorSpecificationReferenceSystem.  # noqa: E501
        :type reference_system_name: str
        """
        self.swagger_types = {
            'uri': str,
            'name': str,
            'reference_system_name': str
        }

        self.attribute_map = {
            'uri': 'URI',
            'name': 'name',
            'reference_system_name': 'referenceSystemName'
        }

        self._uri = uri
        self._name = name
        self._reference_system_name = reference_system_name

    @classmethod
    def from_dict(cls, dikt) -> 'VendorSpecificationReferenceSystem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vendorSpecificationReferenceSystem of this VendorSpecificationReferenceSystem.  # noqa: E501
        :rtype: VendorSpecificationReferenceSystem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self) -> str:
        """Gets the uri of this VendorSpecificationReferenceSystem.

        The primary URI for this reference system  # noqa: E501

        :return: The uri of this VendorSpecificationReferenceSystem.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        """Sets the uri of this VendorSpecificationReferenceSystem.

        The primary URI for this reference system  # noqa: E501

        :param uri: The uri of this VendorSpecificationReferenceSystem.
        :type uri: str
        """

        self._uri = uri

    @property
    def name(self) -> str:
        """Gets the name of this VendorSpecificationReferenceSystem.

        DEPRECATED in v1.3 - Use \"referenceSystemName\"  # noqa: E501

        :return: The name of this VendorSpecificationReferenceSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this VendorSpecificationReferenceSystem.

        DEPRECATED in v1.3 - Use \"referenceSystemName\"  # noqa: E501

        :param name: The name of this VendorSpecificationReferenceSystem.
        :type name: str
        """

        self._name = name

    @property
    def reference_system_name(self) -> str:
        """Gets the reference_system_name of this VendorSpecificationReferenceSystem.

        The human readable name for this reference system  # noqa: E501

        :return: The reference_system_name of this VendorSpecificationReferenceSystem.
        :rtype: str
        """
        return self._reference_system_name

    @reference_system_name.setter
    def reference_system_name(self, reference_system_name: str):
        """Sets the reference_system_name of this VendorSpecificationReferenceSystem.

        The human readable name for this reference system  # noqa: E501

        :param reference_system_name: The reference_system_name of this VendorSpecificationReferenceSystem.
        :type reference_system_name: str
        """

        self._reference_system_name = reference_system_name