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

class AnacFormA33Type(object):
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
        'appalto': 'AppaltoA33Type',
        'aggiudicazioni': 'list[AggiudicazioneA33Type]'
    }

    attribute_map = {
        'appalto': 'appalto',
        'aggiudicazioni': 'aggiudicazioni'
    }

    def __init__(self, appalto=None, aggiudicazioni=None):  # noqa: E501
        """AnacFormA33Type - a model defined in Swagger"""  # noqa: E501
        self._appalto = None
        self._aggiudicazioni = None
        self.discriminator = None
        self.appalto = appalto
        self.aggiudicazioni = aggiudicazioni

    @property
    def appalto(self):
        """Gets the appalto of this AnacFormA33Type.  # noqa: E501


        :return: The appalto of this AnacFormA33Type.  # noqa: E501
        :rtype: AppaltoA33Type
        """
        return self._appalto

    @appalto.setter
    def appalto(self, appalto):
        """Sets the appalto of this AnacFormA33Type.


        :param appalto: The appalto of this AnacFormA33Type.  # noqa: E501
        :type: AppaltoA33Type
        """
        if appalto is None:
            raise ValueError("Invalid value for `appalto`, must not be `None`")  # noqa: E501

        self._appalto = appalto

    @property
    def aggiudicazioni(self):
        """Gets the aggiudicazioni of this AnacFormA33Type.  # noqa: E501

        Dati relativi alle aggiudicazioni  # noqa: E501

        :return: The aggiudicazioni of this AnacFormA33Type.  # noqa: E501
        :rtype: list[AggiudicazioneA33Type]
        """
        return self._aggiudicazioni

    @aggiudicazioni.setter
    def aggiudicazioni(self, aggiudicazioni):
        """Sets the aggiudicazioni of this AnacFormA33Type.

        Dati relativi alle aggiudicazioni  # noqa: E501

        :param aggiudicazioni: The aggiudicazioni of this AnacFormA33Type.  # noqa: E501
        :type: list[AggiudicazioneA33Type]
        """
        if aggiudicazioni is None:
            raise ValueError("Invalid value for `aggiudicazioni`, must not be `None`")  # noqa: E501

        self._aggiudicazioni = aggiudicazioni

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
        if issubclass(AnacFormA33Type, dict):
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
        if not isinstance(other, AnacFormA33Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
