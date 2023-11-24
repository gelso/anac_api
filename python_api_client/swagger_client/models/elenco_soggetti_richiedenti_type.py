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

class ElencoSoggettiRichiedentiType(object):
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
        'cig': 'str',
        'soggetti_interessati': 'list[SoggettoType1]'
    }

    attribute_map = {
        'cig': 'cig',
        'soggetti_interessati': 'soggettiInteressati'
    }

    def __init__(self, cig=None, soggetti_interessati=None):  # noqa: E501
        """ElencoSoggettiRichiedentiType - a model defined in Swagger"""  # noqa: E501
        self._cig = None
        self._soggetti_interessati = None
        self.discriminator = None
        self.cig = cig
        self.soggetti_interessati = soggetti_interessati

    @property
    def cig(self):
        """Gets the cig of this ElencoSoggettiRichiedentiType.  # noqa: E501

        codice identificativo lotto  # noqa: E501

        :return: The cig of this ElencoSoggettiRichiedentiType.  # noqa: E501
        :rtype: str
        """
        return self._cig

    @cig.setter
    def cig(self, cig):
        """Sets the cig of this ElencoSoggettiRichiedentiType.

        codice identificativo lotto  # noqa: E501

        :param cig: The cig of this ElencoSoggettiRichiedentiType.  # noqa: E501
        :type: str
        """
        if cig is None:
            raise ValueError("Invalid value for `cig`, must not be `None`")  # noqa: E501

        self._cig = cig

    @property
    def soggetti_interessati(self):
        """Gets the soggetti_interessati of this ElencoSoggettiRichiedentiType.  # noqa: E501

        Dati relativi ai soggetti che hanno presentato manifestazione d'interesse  # noqa: E501

        :return: The soggetti_interessati of this ElencoSoggettiRichiedentiType.  # noqa: E501
        :rtype: list[SoggettoType1]
        """
        return self._soggetti_interessati

    @soggetti_interessati.setter
    def soggetti_interessati(self, soggetti_interessati):
        """Sets the soggetti_interessati of this ElencoSoggettiRichiedentiType.

        Dati relativi ai soggetti che hanno presentato manifestazione d'interesse  # noqa: E501

        :param soggetti_interessati: The soggetti_interessati of this ElencoSoggettiRichiedentiType.  # noqa: E501
        :type: list[SoggettoType1]
        """
        if soggetti_interessati is None:
            raise ValueError("Invalid value for `soggetti_interessati`, must not be `None`")  # noqa: E501

        self._soggetti_interessati = soggetti_interessati

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
        if issubclass(ElencoSoggettiRichiedentiType, dict):
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
        if not isinstance(other, ElencoSoggettiRichiedentiType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
