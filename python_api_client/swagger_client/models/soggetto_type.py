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

class SoggettoType(object):
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
        'codice_fiscale': 'str',
        'ruolo': 'TipoRuoloEnum',
        'servizio': 'TipoServizioSoggettoEnum',
        'operazione': 'TipoOperazioneSoggettoEnum',
        'data_inizio': 'datetime',
        'data_fine': 'datetime'
    }

    attribute_map = {
        'codice_fiscale': 'codiceFiscale',
        'ruolo': 'ruolo',
        'servizio': 'servizio',
        'operazione': 'operazione',
        'data_inizio': 'dataInizio',
        'data_fine': 'dataFine'
    }

    def __init__(self, codice_fiscale=None, ruolo=None, servizio=None, operazione=None, data_inizio=None, data_fine=None):  # noqa: E501
        """SoggettoType - a model defined in Swagger"""  # noqa: E501
        self._codice_fiscale = None
        self._ruolo = None
        self._servizio = None
        self._operazione = None
        self._data_inizio = None
        self._data_fine = None
        self.discriminator = None
        if codice_fiscale is not None:
            self.codice_fiscale = codice_fiscale
        if ruolo is not None:
            self.ruolo = ruolo
        if servizio is not None:
            self.servizio = servizio
        if operazione is not None:
            self.operazione = operazione
        if data_inizio is not None:
            self.data_inizio = data_inizio
        if data_fine is not None:
            self.data_fine = data_fine

    @property
    def codice_fiscale(self):
        """Gets the codice_fiscale of this SoggettoType.  # noqa: E501

        Codice fiscale del soggetto  # noqa: E501

        :return: The codice_fiscale of this SoggettoType.  # noqa: E501
        :rtype: str
        """
        return self._codice_fiscale

    @codice_fiscale.setter
    def codice_fiscale(self, codice_fiscale):
        """Sets the codice_fiscale of this SoggettoType.

        Codice fiscale del soggetto  # noqa: E501

        :param codice_fiscale: The codice_fiscale of this SoggettoType.  # noqa: E501
        :type: str
        """

        self._codice_fiscale = codice_fiscale

    @property
    def ruolo(self):
        """Gets the ruolo of this SoggettoType.  # noqa: E501


        :return: The ruolo of this SoggettoType.  # noqa: E501
        :rtype: TipoRuoloEnum
        """
        return self._ruolo

    @ruolo.setter
    def ruolo(self, ruolo):
        """Sets the ruolo of this SoggettoType.


        :param ruolo: The ruolo of this SoggettoType.  # noqa: E501
        :type: TipoRuoloEnum
        """

        self._ruolo = ruolo

    @property
    def servizio(self):
        """Gets the servizio of this SoggettoType.  # noqa: E501


        :return: The servizio of this SoggettoType.  # noqa: E501
        :rtype: TipoServizioSoggettoEnum
        """
        return self._servizio

    @servizio.setter
    def servizio(self, servizio):
        """Sets the servizio of this SoggettoType.


        :param servizio: The servizio of this SoggettoType.  # noqa: E501
        :type: TipoServizioSoggettoEnum
        """

        self._servizio = servizio

    @property
    def operazione(self):
        """Gets the operazione of this SoggettoType.  # noqa: E501


        :return: The operazione of this SoggettoType.  # noqa: E501
        :rtype: TipoOperazioneSoggettoEnum
        """
        return self._operazione

    @operazione.setter
    def operazione(self, operazione):
        """Sets the operazione of this SoggettoType.


        :param operazione: The operazione of this SoggettoType.  # noqa: E501
        :type: TipoOperazioneSoggettoEnum
        """

        self._operazione = operazione

    @property
    def data_inizio(self):
        """Gets the data_inizio of this SoggettoType.  # noqa: E501

        data inizio incarico soggetto (A date-time specified by ISO 8601 as profiled by RFC 3339)  # noqa: E501

        :return: The data_inizio of this SoggettoType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_inizio

    @data_inizio.setter
    def data_inizio(self, data_inizio):
        """Sets the data_inizio of this SoggettoType.

        data inizio incarico soggetto (A date-time specified by ISO 8601 as profiled by RFC 3339)  # noqa: E501

        :param data_inizio: The data_inizio of this SoggettoType.  # noqa: E501
        :type: datetime
        """

        self._data_inizio = data_inizio

    @property
    def data_fine(self):
        """Gets the data_fine of this SoggettoType.  # noqa: E501

        data fine incarico soggetto (A date-time specified by ISO 8601 as profiled by RFC 3339)  # noqa: E501

        :return: The data_fine of this SoggettoType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_fine

    @data_fine.setter
    def data_fine(self, data_fine):
        """Sets the data_fine of this SoggettoType.

        data fine incarico soggetto (A date-time specified by ISO 8601 as profiled by RFC 3339)  # noqa: E501

        :param data_fine: The data_fine of this SoggettoType.  # noqa: E501
        :type: datetime
        """

        self._data_fine = data_fine

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
        if issubclass(SoggettoType, dict):
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
        if not isinstance(other, SoggettoType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
