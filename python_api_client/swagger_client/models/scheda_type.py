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

class SchedaType(object):
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
        'id_scheda': 'str',
        'codice': 'CodiceSchedaEnum',
        'versione': 'str',
        'stato': 'StatoSchedaEnum',
        'data_creazione': 'datetime'
    }

    attribute_map = {
        'id_scheda': '_idScheda',
        'codice': 'codice',
        'versione': 'versione',
        'stato': '_stato',
        'data_creazione': '_dataCreazione'
    }

    def __init__(self, id_scheda=None, codice=None, versione=None, stato=None, data_creazione=None):  # noqa: E501
        """SchedaType - a model defined in Swagger"""  # noqa: E501
        self._id_scheda = None
        self._codice = None
        self._versione = None
        self._stato = None
        self._data_creazione = None
        self.discriminator = None
        if id_scheda is not None:
            self.id_scheda = id_scheda
        self.codice = codice
        self.versione = versione
        if stato is not None:
            self.stato = stato
        if data_creazione is not None:
            self.data_creazione = data_creazione

    @property
    def id_scheda(self):
        """Gets the id_scheda of this SchedaType.  # noqa: E501

        Codice univoco della scheda. il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nella post.  # noqa: E501

        :return: The id_scheda of this SchedaType.  # noqa: E501
        :rtype: str
        """
        return self._id_scheda

    @id_scheda.setter
    def id_scheda(self, id_scheda):
        """Sets the id_scheda of this SchedaType.

        Codice univoco della scheda. il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nella post.  # noqa: E501

        :param id_scheda: The id_scheda of this SchedaType.  # noqa: E501
        :type: str
        """

        self._id_scheda = id_scheda

    @property
    def codice(self):
        """Gets the codice of this SchedaType.  # noqa: E501


        :return: The codice of this SchedaType.  # noqa: E501
        :rtype: CodiceSchedaEnum
        """
        return self._codice

    @codice.setter
    def codice(self, codice):
        """Sets the codice of this SchedaType.


        :param codice: The codice of this SchedaType.  # noqa: E501
        :type: CodiceSchedaEnum
        """
        if codice is None:
            raise ValueError("Invalid value for `codice`, must not be `None`")  # noqa: E501

        self._codice = codice

    @property
    def versione(self):
        """Gets the versione of this SchedaType.  # noqa: E501

        versione della scheda. necessaria al motore interno ANAC.  # noqa: E501

        :return: The versione of this SchedaType.  # noqa: E501
        :rtype: str
        """
        return self._versione

    @versione.setter
    def versione(self, versione):
        """Sets the versione of this SchedaType.

        versione della scheda. necessaria al motore interno ANAC.  # noqa: E501

        :param versione: The versione of this SchedaType.  # noqa: E501
        :type: str
        """
        if versione is None:
            raise ValueError("Invalid value for `versione`, must not be `None`")  # noqa: E501

        self._versione = versione

    @property
    def stato(self):
        """Gets the stato of this SchedaType.  # noqa: E501


        :return: The stato of this SchedaType.  # noqa: E501
        :rtype: StatoSchedaEnum
        """
        return self._stato

    @stato.setter
    def stato(self, stato):
        """Sets the stato of this SchedaType.


        :param stato: The stato of this SchedaType.  # noqa: E501
        :type: StatoSchedaEnum
        """

        self._stato = stato

    @property
    def data_creazione(self):
        """Gets the data_creazione of this SchedaType.  # noqa: E501

        data creazione della scheda (A date-time specified by ISO 8601 as profiled by RFC 3339)  # noqa: E501

        :return: The data_creazione of this SchedaType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_creazione

    @data_creazione.setter
    def data_creazione(self, data_creazione):
        """Sets the data_creazione of this SchedaType.

        data creazione della scheda (A date-time specified by ISO 8601 as profiled by RFC 3339)  # noqa: E501

        :param data_creazione: The data_creazione of this SchedaType.  # noqa: E501
        :type: datetime
        """

        self._data_creazione = data_creazione

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
        if issubclass(SchedaType, dict):
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
        if not isinstance(other, SchedaType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
