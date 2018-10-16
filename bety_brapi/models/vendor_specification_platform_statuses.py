# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class VendorSpecificationPlatformStatuses(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, status_description: str=None, status_name: str=None):  # noqa: E501
        """VendorSpecificationPlatformStatuses - a model defined in Swagger

        :param status_description: The status_description of this VendorSpecificationPlatformStatuses.  # noqa: E501
        :type status_description: str
        :param status_name: The status_name of this VendorSpecificationPlatformStatuses.  # noqa: E501
        :type status_name: str
        """
        self.swagger_types = {
            'status_description': str,
            'status_name': str
        }

        self.attribute_map = {
            'status_description': 'statusDescription',
            'status_name': 'statusName'
        }

        self._status_description = status_description
        self._status_name = status_name

    @classmethod
    def from_dict(cls, dikt) -> 'VendorSpecificationPlatformStatuses':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vendorSpecificationPlatform_statuses of this VendorSpecificationPlatformStatuses.  # noqa: E501
        :rtype: VendorSpecificationPlatformStatuses
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status_description(self) -> str:
        """Gets the status_description of this VendorSpecificationPlatformStatuses.


        :return: The status_description of this VendorSpecificationPlatformStatuses.
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description: str):
        """Sets the status_description of this VendorSpecificationPlatformStatuses.


        :param status_description: The status_description of this VendorSpecificationPlatformStatuses.
        :type status_description: str
        """

        self._status_description = status_description

    @property
    def status_name(self) -> str:
        """Gets the status_name of this VendorSpecificationPlatformStatuses.


        :return: The status_name of this VendorSpecificationPlatformStatuses.
        :rtype: str
        """
        return self._status_name

    @status_name.setter
    def status_name(self, status_name: str):
        """Sets the status_name of this VendorSpecificationPlatformStatuses.


        :param status_name: The status_name of this VendorSpecificationPlatformStatuses.
        :type status_name: str
        """

        self._status_name = status_name