# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.common_crop_names_response_result import CommonCropNamesResponseResult  # noqa: F401,E501
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi import util


class CommonCropNamesResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: CommonCropNamesResponseResult=None):  # noqa: E501
        """CommonCropNamesResponse - a model defined in Swagger

        :param metadata: The metadata of this CommonCropNamesResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this CommonCropNamesResponse.  # noqa: E501
        :type result: CommonCropNamesResponseResult
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': CommonCropNamesResponseResult
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'CommonCropNamesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The commonCropNamesResponse of this CommonCropNamesResponse.  # noqa: E501
        :rtype: CommonCropNamesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this CommonCropNamesResponse.


        :return: The metadata of this CommonCropNamesResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this CommonCropNamesResponse.


        :param metadata: The metadata of this CommonCropNamesResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> CommonCropNamesResponseResult:
        """Gets the result of this CommonCropNamesResponse.


        :return: The result of this CommonCropNamesResponse.
        :rtype: CommonCropNamesResponseResult
        """
        return self._result

    @result.setter
    def result(self, result: CommonCropNamesResponseResult):
        """Sets the result of this CommonCropNamesResponse.


        :param result: The result of this CommonCropNamesResponse.
        :type result: CommonCropNamesResponseResult
        """

        self._result = result