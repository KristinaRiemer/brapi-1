# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.marker import Marker  # noqa: F401,E501
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi import util


class MarkerResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: Marker=None):  # noqa: E501
        """MarkerResponse - a model defined in Swagger

        :param metadata: The metadata of this MarkerResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this MarkerResponse.  # noqa: E501
        :type result: Marker
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': Marker
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'MarkerResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The markerResponse of this MarkerResponse.  # noqa: E501
        :rtype: MarkerResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this MarkerResponse.


        :return: The metadata of this MarkerResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this MarkerResponse.


        :param metadata: The metadata of this MarkerResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> Marker:
        """Gets the result of this MarkerResponse.


        :return: The result of this MarkerResponse.
        :rtype: Marker
        """
        return self._result

    @result.setter
    def result(self, result: Marker):
        """Sets the result of this MarkerResponse.


        :param result: The result of this MarkerResponse.
        :type result: Marker
        """

        self._result = result