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

class ContentDocumentType(object):
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
        'nomefile': 'str',
        'estensione': 'str',
        'dimensione': 'int',
        'contenuto': 'str'
    }

    attribute_map = {
        'nomefile': 'nomefile',
        'estensione': 'estensione',
        'dimensione': 'dimensione',
        'contenuto': 'contenuto'
    }

    def __init__(self, nomefile=None, estensione=None, dimensione=None, contenuto=None):  # noqa: E501
        """ContentDocumentType - a model defined in Swagger"""  # noqa: E501
        self._nomefile = None
        self._estensione = None
        self._dimensione = None
        self._contenuto = None
        self.discriminator = None
        if nomefile is not None:
            self.nomefile = nomefile
        if estensione is not None:
            self.estensione = estensione
        if dimensione is not None:
            self.dimensione = dimensione
        if contenuto is not None:
            self.contenuto = contenuto

    @property
    def nomefile(self):
        """Gets the nomefile of this ContentDocumentType.  # noqa: E501

        nomeFile originale  # noqa: E501

        :return: The nomefile of this ContentDocumentType.  # noqa: E501
        :rtype: str
        """
        return self._nomefile

    @nomefile.setter
    def nomefile(self, nomefile):
        """Sets the nomefile of this ContentDocumentType.

        nomeFile originale  # noqa: E501

        :param nomefile: The nomefile of this ContentDocumentType.  # noqa: E501
        :type: str
        """

        self._nomefile = nomefile

    @property
    def estensione(self):
        """Gets the estensione of this ContentDocumentType.  # noqa: E501

        estensione file  # noqa: E501

        :return: The estensione of this ContentDocumentType.  # noqa: E501
        :rtype: str
        """
        return self._estensione

    @estensione.setter
    def estensione(self, estensione):
        """Sets the estensione of this ContentDocumentType.

        estensione file  # noqa: E501

        :param estensione: The estensione of this ContentDocumentType.  # noqa: E501
        :type: str
        """

        self._estensione = estensione

    @property
    def dimensione(self):
        """Gets the dimensione of this ContentDocumentType.  # noqa: E501

        grandezza del documento  # noqa: E501

        :return: The dimensione of this ContentDocumentType.  # noqa: E501
        :rtype: int
        """
        return self._dimensione

    @dimensione.setter
    def dimensione(self, dimensione):
        """Sets the dimensione of this ContentDocumentType.

        grandezza del documento  # noqa: E501

        :param dimensione: The dimensione of this ContentDocumentType.  # noqa: E501
        :type: int
        """

        self._dimensione = dimensione

    @property
    def contenuto(self):
        """Gets the contenuto of this ContentDocumentType.  # noqa: E501

        Contenuto in formato Binario del documento  # noqa: E501

        :return: The contenuto of this ContentDocumentType.  # noqa: E501
        :rtype: str
        """
        return self._contenuto

    @contenuto.setter
    def contenuto(self, contenuto):
        """Sets the contenuto of this ContentDocumentType.

        Contenuto in formato Binario del documento  # noqa: E501

        :param contenuto: The contenuto of this ContentDocumentType.  # noqa: E501
        :type: str
        """

        self._contenuto = contenuto

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
        if issubclass(ContentDocumentType, dict):
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
        if not isinstance(other, ContentDocumentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
