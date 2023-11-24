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

class ConclusioneType1(object):
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
        'data_inizio': 'datetime',
        'data_ultimazione': 'datetime',
        'importo': 'float'
    }

    attribute_map = {
        'data_inizio': 'dataInizio',
        'data_ultimazione': 'dataUltimazione',
        'importo': 'importo'
    }

    def __init__(self, data_inizio=None, data_ultimazione=None, importo=None):  # noqa: E501
        """ConclusioneType1 - a model defined in Swagger"""  # noqa: E501
        self._data_inizio = None
        self._data_ultimazione = None
        self._importo = None
        self.discriminator = None
        self.data_inizio = data_inizio
        self.data_ultimazione = data_ultimazione
        self.importo = importo

    @property
    def data_inizio(self):
        """Gets the data_inizio of this ConclusioneType1.  # noqa: E501

        Data di inizio  # noqa: E501

        :return: The data_inizio of this ConclusioneType1.  # noqa: E501
        :rtype: datetime
        """
        return self._data_inizio

    @data_inizio.setter
    def data_inizio(self, data_inizio):
        """Sets the data_inizio of this ConclusioneType1.

        Data di inizio  # noqa: E501

        :param data_inizio: The data_inizio of this ConclusioneType1.  # noqa: E501
        :type: datetime
        """
        if data_inizio is None:
            raise ValueError("Invalid value for `data_inizio`, must not be `None`")  # noqa: E501

        self._data_inizio = data_inizio

    @property
    def data_ultimazione(self):
        """Gets the data_ultimazione of this ConclusioneType1.  # noqa: E501

        Data di ultimazione  # noqa: E501

        :return: The data_ultimazione of this ConclusioneType1.  # noqa: E501
        :rtype: datetime
        """
        return self._data_ultimazione

    @data_ultimazione.setter
    def data_ultimazione(self, data_ultimazione):
        """Sets the data_ultimazione of this ConclusioneType1.

        Data di ultimazione  # noqa: E501

        :param data_ultimazione: The data_ultimazione of this ConclusioneType1.  # noqa: E501
        :type: datetime
        """
        if data_ultimazione is None:
            raise ValueError("Invalid value for `data_ultimazione`, must not be `None`")  # noqa: E501

        self._data_ultimazione = data_ultimazione

    @property
    def importo(self):
        """Gets the importo of this ConclusioneType1.  # noqa: E501

        Importo delle somme liquidate  # noqa: E501

        :return: The importo of this ConclusioneType1.  # noqa: E501
        :rtype: float
        """
        return self._importo

    @importo.setter
    def importo(self, importo):
        """Sets the importo of this ConclusioneType1.

        Importo delle somme liquidate  # noqa: E501

        :param importo: The importo of this ConclusioneType1.  # noqa: E501
        :type: float
        """
        if importo is None:
            raise ValueError("Invalid value for `importo`, must not be `None`")  # noqa: E501

        self._importo = importo

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
        if issubclass(ConclusioneType1, dict):
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
        if not isinstance(other, ConclusioneType1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
