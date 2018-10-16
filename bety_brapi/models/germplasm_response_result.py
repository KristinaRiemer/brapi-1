# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.germplasm import Germplasm  # noqa: F401,E501
from bety_brapi import util


class GermplasmResponseResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data: List[Germplasm]=None):  # noqa: E501
        """GermplasmResponseResult - a model defined in Swagger

        :param data: The data of this GermplasmResponseResult.  # noqa: E501
        :type data: List[Germplasm]
        """
        self.swagger_types = {
            'data': List[Germplasm]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'GermplasmResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The germplasmResponse_result of this GermplasmResponseResult.  # noqa: E501
        :rtype: GermplasmResponseResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[Germplasm]:
        """Gets the data of this GermplasmResponseResult.


        :return: The data of this GermplasmResponseResult.
        :rtype: List[Germplasm]
        """
        return self._data

    @data.setter
    def data(self, data: List[Germplasm]):
        """Sets the data of this GermplasmResponseResult.


        :param data: The data of this GermplasmResponseResult.
        :type data: List[Germplasm]
        """

        self._data = data