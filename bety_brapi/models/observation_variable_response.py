# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi.models.observation_variable import ObservationVariable  # noqa: F401,E501
from bety_brapi import util


class ObservationVariableResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: ObservationVariable=None):  # noqa: E501
        """ObservationVariableResponse - a model defined in Swagger

        :param metadata: The metadata of this ObservationVariableResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this ObservationVariableResponse.  # noqa: E501
        :type result: ObservationVariable
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': ObservationVariable
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'ObservationVariableResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The observationVariableResponse of this ObservationVariableResponse.  # noqa: E501
        :rtype: ObservationVariableResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this ObservationVariableResponse.


        :return: The metadata of this ObservationVariableResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this ObservationVariableResponse.


        :param metadata: The metadata of this ObservationVariableResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> ObservationVariable:
        """Gets the result of this ObservationVariableResponse.


        :return: The result of this ObservationVariableResponse.
        :rtype: ObservationVariable
        """
        return self._result

    @result.setter
    def result(self, result: ObservationVariable):
        """Sets the result of this ObservationVariableResponse.


        :param result: The result of this ObservationVariableResponse.
        :type result: ObservationVariable
        """

        self._result = result