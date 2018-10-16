# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi.models.observation_unit_positions_response_result import ObservationUnitPositionsResponseResult  # noqa: F401,E501
from bety_brapi import util


class ObservationUnitPositionsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: ObservationUnitPositionsResponseResult=None):  # noqa: E501
        """ObservationUnitPositionsResponse - a model defined in Swagger

        :param metadata: The metadata of this ObservationUnitPositionsResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this ObservationUnitPositionsResponse.  # noqa: E501
        :type result: ObservationUnitPositionsResponseResult
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': ObservationUnitPositionsResponseResult
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'ObservationUnitPositionsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The observationUnitPositionsResponse of this ObservationUnitPositionsResponse.  # noqa: E501
        :rtype: ObservationUnitPositionsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this ObservationUnitPositionsResponse.


        :return: The metadata of this ObservationUnitPositionsResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this ObservationUnitPositionsResponse.


        :param metadata: The metadata of this ObservationUnitPositionsResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> ObservationUnitPositionsResponseResult:
        """Gets the result of this ObservationUnitPositionsResponse.


        :return: The result of this ObservationUnitPositionsResponse.
        :rtype: ObservationUnitPositionsResponseResult
        """
        return self._result

    @result.setter
    def result(self, result: ObservationUnitPositionsResponseResult):
        """Sets the result of this ObservationUnitPositionsResponse.


        :param result: The result of this ObservationUnitPositionsResponse.
        :type result: ObservationUnitPositionsResponseResult
        """

        self._result = result