# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi.models.vendor_plate import VendorPlate  # noqa: F401,E501
from bety_brapi import util


class VendorPlateResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: VendorPlate=None):  # noqa: E501
        """VendorPlateResponse - a model defined in Swagger

        :param metadata: The metadata of this VendorPlateResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this VendorPlateResponse.  # noqa: E501
        :type result: VendorPlate
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': VendorPlate
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'VendorPlateResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vendorPlateResponse of this VendorPlateResponse.  # noqa: E501
        :rtype: VendorPlateResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this VendorPlateResponse.


        :return: The metadata of this VendorPlateResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this VendorPlateResponse.


        :param metadata: The metadata of this VendorPlateResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> VendorPlate:
        """Gets the result of this VendorPlateResponse.


        :return: The result of this VendorPlateResponse.
        :rtype: VendorPlate
        """
        return self._result

    @result.setter
    def result(self, result: VendorPlate):
        """Sets the result of this VendorPlateResponse.


        :param result: The result of this VendorPlateResponse.
        :type result: VendorPlate
        """

        self._result = result