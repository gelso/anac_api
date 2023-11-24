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

class AppaltoBaseType(object):
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
        'id_appalto': 'str',
        'codice_appalto': 'str',
        'oggetto': 'str',
        'data_creazione': 'datetime',
        'stato': 'StatoAppaltoEnum'
    }

    attribute_map = {
        'id_appalto': 'idAppalto',
        'codice_appalto': 'codiceAppalto',
        'oggetto': 'oggetto',
        'data_creazione': 'dataCreazione',
        'stato': 'stato'
    }

    def __init__(self, id_appalto=None, codice_appalto=None, oggetto=None, data_creazione=None, stato=None):  # noqa: E501
        """AppaltoBaseType - a model defined in Swagger"""  # noqa: E501
        self._id_appalto = None
        self._codice_appalto = None
        self._oggetto = None
        self._data_creazione = None
        self._stato = None
        self.discriminator = None
        if id_appalto is not None:
            self.id_appalto = id_appalto
        if codice_appalto is not None:
            self.codice_appalto = codice_appalto
        if oggetto is not None:
            self.oggetto = oggetto
        if data_creazione is not None:
            self.data_creazione = data_creazione
        if stato is not None:
            self.stato = stato

    @property
    def id_appalto(self):
        """Gets the id_appalto of this AppaltoBaseType.  # noqa: E501

        identificativo univoco dell'Appalto definito da ANAC. Restituito dall'operazione di creazione Appalto. (A UUID specified by RFC4122)  # noqa: E501

        :return: The id_appalto of this AppaltoBaseType.  # noqa: E501
        :rtype: str
        """
        return self._id_appalto

    @id_appalto.setter
    def id_appalto(self, id_appalto):
        """Sets the id_appalto of this AppaltoBaseType.

        identificativo univoco dell'Appalto definito da ANAC. Restituito dall'operazione di creazione Appalto. (A UUID specified by RFC4122)  # noqa: E501

        :param id_appalto: The id_appalto of this AppaltoBaseType.  # noqa: E501
        :type: str
        """

        self._id_appalto = id_appalto

    @property
    def codice_appalto(self):
        """Gets the codice_appalto of this AppaltoBaseType.  # noqa: E501

        identificativo univoco dell'Appalto definito dal SA.  # noqa: E501

        :return: The codice_appalto of this AppaltoBaseType.  # noqa: E501
        :rtype: str
        """
        return self._codice_appalto

    @codice_appalto.setter
    def codice_appalto(self, codice_appalto):
        """Sets the codice_appalto of this AppaltoBaseType.

        identificativo univoco dell'Appalto definito dal SA.  # noqa: E501

        :param codice_appalto: The codice_appalto of this AppaltoBaseType.  # noqa: E501
        :type: str
        """

        self._codice_appalto = codice_appalto

    @property
    def oggetto(self):
        """Gets the oggetto of this AppaltoBaseType.  # noqa: E501

        descrizione dell'appalto  # noqa: E501

        :return: The oggetto of this AppaltoBaseType.  # noqa: E501
        :rtype: str
        """
        return self._oggetto

    @oggetto.setter
    def oggetto(self, oggetto):
        """Sets the oggetto of this AppaltoBaseType.

        descrizione dell'appalto  # noqa: E501

        :param oggetto: The oggetto of this AppaltoBaseType.  # noqa: E501
        :type: str
        """

        self._oggetto = oggetto

    @property
    def data_creazione(self):
        """Gets the data_creazione of this AppaltoBaseType.  # noqa: E501

        data creazione dell'appalto (A date-time specified by ISO 8601 as profiled by RFC 3339)  # noqa: E501

        :return: The data_creazione of this AppaltoBaseType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_creazione

    @data_creazione.setter
    def data_creazione(self, data_creazione):
        """Sets the data_creazione of this AppaltoBaseType.

        data creazione dell'appalto (A date-time specified by ISO 8601 as profiled by RFC 3339)  # noqa: E501

        :param data_creazione: The data_creazione of this AppaltoBaseType.  # noqa: E501
        :type: datetime
        """

        self._data_creazione = data_creazione

    @property
    def stato(self):
        """Gets the stato of this AppaltoBaseType.  # noqa: E501


        :return: The stato of this AppaltoBaseType.  # noqa: E501
        :rtype: StatoAppaltoEnum
        """
        return self._stato

    @stato.setter
    def stato(self, stato):
        """Sets the stato of this AppaltoBaseType.


        :param stato: The stato of this AppaltoBaseType.  # noqa: E501
        :type: StatoAppaltoEnum
        """

        self._stato = stato

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
        if issubclass(AppaltoBaseType, dict):
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
        if not isinstance(other, AppaltoBaseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
