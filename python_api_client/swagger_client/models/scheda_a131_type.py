# coding: utf-8

"""
    Specifiche Servizi Appalto - OpenAPI 3.0

    Sono descritte le specifiche dei servizi esposti dalla Piattaforma Contratti Pubblici (PCP), richiamabili dalle Stazioni Appaltanti, per la gestione e la raccolta delle informazioni rilevanti nei processi che compongono l’intero ciclo di vita degli appalti.    #### Documentazione   La documentazione a supporto delle specifiche di interfaccia con i sistemi che interoperano con il nuovo sistema di digitalizzazione è redatta con il linguaggio di markup Markdown ed è presente al segunete url:     [documento-specifiche-servizi-npa](https://github.com/anticorruzione/npa/blob/main/docs/specifiche-interfacce/documento-specifiche-servizi-npa.md) ```  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ufficio.uscp@anticorruzione.it
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SchedaA131Type(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'anac_form': 'AnacFormA131Type',
        'eform': 'EformType'
    }

    attribute_map = {
        'anac_form': 'anacForm',
        'eform': 'eform'
    }

    def __init__(self, anac_form=None, eform=None):  # noqa: E501
        """SchedaA131Type - a model defined in Swagger"""  # noqa: E501
        self._anac_form = None
        self._eform = None
        self.discriminator = None
        self.anac_form = anac_form
        self.eform = eform

    @property
    def anac_form(self):
        """Gets the anac_form of this SchedaA131Type.  # noqa: E501


        :return: The anac_form of this SchedaA131Type.  # noqa: E501
        :rtype: AnacFormA131Type
        """
        return self._anac_form

    @anac_form.setter
    def anac_form(self, anac_form):
        """Sets the anac_form of this SchedaA131Type.


        :param anac_form: The anac_form of this SchedaA131Type.  # noqa: E501
        :type: AnacFormA131Type
        """
        if anac_form is None:
            raise ValueError("Invalid value for `anac_form`, must not be `None`")  # noqa: E501

        self._anac_form = anac_form

    @property
    def eform(self):
        """Gets the eform of this SchedaA131Type.  # noqa: E501


        :return: The eform of this SchedaA131Type.  # noqa: E501
        :rtype: EformType
        """
        return self._eform

    @eform.setter
    def eform(self, eform):
        """Sets the eform of this SchedaA131Type.


        :param eform: The eform of this SchedaA131Type.  # noqa: E501
        :type: EformType
        """
        if eform is None:
            raise ValueError("Invalid value for `eform`, must not be `None`")  # noqa: E501

        self._eform = eform

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SchedaA131Type, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SchedaA131Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
