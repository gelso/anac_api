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

class AnacFormP35Type(object):
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
        'appalto': 'AppaltoP35Type',
        'lotti': 'list[LottoP35Type]',
        'stazioni_appaltanti': 'list[StazioneAppaltanteType]'
    }

    attribute_map = {
        'appalto': 'appalto',
        'lotti': 'lotti',
        'stazioni_appaltanti': 'stazioniAppaltanti'
    }

    def __init__(self, appalto=None, lotti=None, stazioni_appaltanti=None):  # noqa: E501
        """AnacFormP35Type - a model defined in Swagger"""  # noqa: E501
        self._appalto = None
        self._lotti = None
        self._stazioni_appaltanti = None
        self.discriminator = None
        self.appalto = appalto
        self.lotti = lotti
        if stazioni_appaltanti is not None:
            self.stazioni_appaltanti = stazioni_appaltanti

    @property
    def appalto(self):
        """Gets the appalto of this AnacFormP35Type.  # noqa: E501


        :return: The appalto of this AnacFormP35Type.  # noqa: E501
        :rtype: AppaltoP35Type
        """
        return self._appalto

    @appalto.setter
    def appalto(self, appalto):
        """Sets the appalto of this AnacFormP35Type.


        :param appalto: The appalto of this AnacFormP35Type.  # noqa: E501
        :type: AppaltoP35Type
        """
        if appalto is None:
            raise ValueError("Invalid value for `appalto`, must not be `None`")  # noqa: E501

        self._appalto = appalto

    @property
    def lotti(self):
        """Gets the lotti of this AnacFormP35Type.  # noqa: E501

        Dati relativi ai lotti  # noqa: E501

        :return: The lotti of this AnacFormP35Type.  # noqa: E501
        :rtype: list[LottoP35Type]
        """
        return self._lotti

    @lotti.setter
    def lotti(self, lotti):
        """Sets the lotti of this AnacFormP35Type.

        Dati relativi ai lotti  # noqa: E501

        :param lotti: The lotti of this AnacFormP35Type.  # noqa: E501
        :type: list[LottoP35Type]
        """
        if lotti is None:
            raise ValueError("Invalid value for `lotti`, must not be `None`")  # noqa: E501

        self._lotti = lotti

    @property
    def stazioni_appaltanti(self):
        """Gets the stazioni_appaltanti of this AnacFormP35Type.  # noqa: E501

        Dati relativi alle stazioni appaltanti  # noqa: E501

        :return: The stazioni_appaltanti of this AnacFormP35Type.  # noqa: E501
        :rtype: list[StazioneAppaltanteType]
        """
        return self._stazioni_appaltanti

    @stazioni_appaltanti.setter
    def stazioni_appaltanti(self, stazioni_appaltanti):
        """Sets the stazioni_appaltanti of this AnacFormP35Type.

        Dati relativi alle stazioni appaltanti  # noqa: E501

        :param stazioni_appaltanti: The stazioni_appaltanti of this AnacFormP35Type.  # noqa: E501
        :type: list[StazioneAppaltanteType]
        """

        self._stazioni_appaltanti = stazioni_appaltanti

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
        if issubclass(AnacFormP35Type, dict):
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
        if not isinstance(other, AnacFormP35Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
