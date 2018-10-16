# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class GermplasmDonors(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, donor_accession_number: str=None, donor_institute_code: str=None, germplasm_pui: str=None):  # noqa: E501
        """GermplasmDonors - a model defined in Swagger

        :param donor_accession_number: The donor_accession_number of this GermplasmDonors.  # noqa: E501
        :type donor_accession_number: str
        :param donor_institute_code: The donor_institute_code of this GermplasmDonors.  # noqa: E501
        :type donor_institute_code: str
        :param germplasm_pui: The germplasm_pui of this GermplasmDonors.  # noqa: E501
        :type germplasm_pui: str
        """
        self.swagger_types = {
            'donor_accession_number': str,
            'donor_institute_code': str,
            'germplasm_pui': str
        }

        self.attribute_map = {
            'donor_accession_number': 'donorAccessionNumber',
            'donor_institute_code': 'donorInstituteCode',
            'germplasm_pui': 'germplasmPUI'
        }

        self._donor_accession_number = donor_accession_number
        self._donor_institute_code = donor_institute_code
        self._germplasm_pui = germplasm_pui

    @classmethod
    def from_dict(cls, dikt) -> 'GermplasmDonors':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The germplasm_donors of this GermplasmDonors.  # noqa: E501
        :rtype: GermplasmDonors
        """
        return util.deserialize_model(dikt, cls)

    @property
    def donor_accession_number(self) -> str:
        """Gets the donor_accession_number of this GermplasmDonors.


        :return: The donor_accession_number of this GermplasmDonors.
        :rtype: str
        """
        return self._donor_accession_number

    @donor_accession_number.setter
    def donor_accession_number(self, donor_accession_number: str):
        """Sets the donor_accession_number of this GermplasmDonors.


        :param donor_accession_number: The donor_accession_number of this GermplasmDonors.
        :type donor_accession_number: str
        """

        self._donor_accession_number = donor_accession_number

    @property
    def donor_institute_code(self) -> str:
        """Gets the donor_institute_code of this GermplasmDonors.


        :return: The donor_institute_code of this GermplasmDonors.
        :rtype: str
        """
        return self._donor_institute_code

    @donor_institute_code.setter
    def donor_institute_code(self, donor_institute_code: str):
        """Sets the donor_institute_code of this GermplasmDonors.


        :param donor_institute_code: The donor_institute_code of this GermplasmDonors.
        :type donor_institute_code: str
        """

        self._donor_institute_code = donor_institute_code

    @property
    def germplasm_pui(self) -> str:
        """Gets the germplasm_pui of this GermplasmDonors.


        :return: The germplasm_pui of this GermplasmDonors.
        :rtype: str
        """
        return self._germplasm_pui

    @germplasm_pui.setter
    def germplasm_pui(self, germplasm_pui: str):
        """Sets the germplasm_pui of this GermplasmDonors.


        :param germplasm_pui: The germplasm_pui of this GermplasmDonors.
        :type germplasm_pui: str
        """

        self._germplasm_pui = germplasm_pui