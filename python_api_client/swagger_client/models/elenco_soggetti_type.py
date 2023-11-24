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

class ElencoSoggettiType(object):
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
        'invitati_che_non_hanno_presentato_offerta': 'list[InvitatoType]',
        'partecipanti': 'list[PartecipanteType]',
        'data_invito': 'datetime',
        'data_scadenza_presentazione_offerta': 'datetime'
    }

    attribute_map = {
        'cig': 'cig',
        'invitati_che_non_hanno_presentato_offerta': 'invitatiCheNonHannoPresentatoOfferta',
        'partecipanti': 'partecipanti',
        'data_invito': 'dataInvito',
        'data_scadenza_presentazione_offerta': 'dataScadenzaPresentazioneOfferta'
    }

    def __init__(self, cig=None, invitati_che_non_hanno_presentato_offerta=None, partecipanti=None, data_invito=None, data_scadenza_presentazione_offerta=None):  # noqa: E501
        """ElencoSoggettiType - a model defined in Swagger"""  # noqa: E501
        self._cig = None
        self._invitati_che_non_hanno_presentato_offerta = None
        self._partecipanti = None
        self._data_invito = None
        self._data_scadenza_presentazione_offerta = None
        self.discriminator = None
        self.cig = cig
        if invitati_che_non_hanno_presentato_offerta is not None:
            self.invitati_che_non_hanno_presentato_offerta = invitati_che_non_hanno_presentato_offerta
        self.partecipanti = partecipanti
        if data_invito is not None:
            self.data_invito = data_invito
        self.data_scadenza_presentazione_offerta = data_scadenza_presentazione_offerta

    @property
    def cig(self):
        """Gets the cig of this ElencoSoggettiType.  # noqa: E501

        codice identificativo lotto  # noqa: E501

        :return: The cig of this ElencoSoggettiType.  # noqa: E501
        :rtype: str
        """
        return self._cig

    @cig.setter
    def cig(self, cig):
        """Sets the cig of this ElencoSoggettiType.

        codice identificativo lotto  # noqa: E501

        :param cig: The cig of this ElencoSoggettiType.  # noqa: E501
        :type: str
        """
        if cig is None:
            raise ValueError("Invalid value for `cig`, must not be `None`")  # noqa: E501

        self._cig = cig

    @property
    def invitati_che_non_hanno_presentato_offerta(self):
        """Gets the invitati_che_non_hanno_presentato_offerta of this ElencoSoggettiType.  # noqa: E501

        Dati relativi ai soggetti invitati che non hanno presentato offerta  # noqa: E501

        :return: The invitati_che_non_hanno_presentato_offerta of this ElencoSoggettiType.  # noqa: E501
        :rtype: list[InvitatoType]
        """
        return self._invitati_che_non_hanno_presentato_offerta

    @invitati_che_non_hanno_presentato_offerta.setter
    def invitati_che_non_hanno_presentato_offerta(self, invitati_che_non_hanno_presentato_offerta):
        """Sets the invitati_che_non_hanno_presentato_offerta of this ElencoSoggettiType.

        Dati relativi ai soggetti invitati che non hanno presentato offerta  # noqa: E501

        :param invitati_che_non_hanno_presentato_offerta: The invitati_che_non_hanno_presentato_offerta of this ElencoSoggettiType.  # noqa: E501
        :type: list[InvitatoType]
        """

        self._invitati_che_non_hanno_presentato_offerta = invitati_che_non_hanno_presentato_offerta

    @property
    def partecipanti(self):
        """Gets the partecipanti of this ElencoSoggettiType.  # noqa: E501

        Dati relativi ai partecipanti  # noqa: E501

        :return: The partecipanti of this ElencoSoggettiType.  # noqa: E501
        :rtype: list[PartecipanteType]
        """
        return self._partecipanti

    @partecipanti.setter
    def partecipanti(self, partecipanti):
        """Sets the partecipanti of this ElencoSoggettiType.

        Dati relativi ai partecipanti  # noqa: E501

        :param partecipanti: The partecipanti of this ElencoSoggettiType.  # noqa: E501
        :type: list[PartecipanteType]
        """
        if partecipanti is None:
            raise ValueError("Invalid value for `partecipanti`, must not be `None`")  # noqa: E501

        self._partecipanti = partecipanti

    @property
    def data_invito(self):
        """Gets the data_invito of this ElencoSoggettiType.  # noqa: E501

        Data della lettera di invito  # noqa: E501

        :return: The data_invito of this ElencoSoggettiType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_invito

    @data_invito.setter
    def data_invito(self, data_invito):
        """Sets the data_invito of this ElencoSoggettiType.

        Data della lettera di invito  # noqa: E501

        :param data_invito: The data_invito of this ElencoSoggettiType.  # noqa: E501
        :type: datetime
        """

        self._data_invito = data_invito

    @property
    def data_scadenza_presentazione_offerta(self):
        """Gets the data_scadenza_presentazione_offerta of this ElencoSoggettiType.  # noqa: E501

        Data della scadenza di presentazione dell'offerta  # noqa: E501

        :return: The data_scadenza_presentazione_offerta of this ElencoSoggettiType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_scadenza_presentazione_offerta

    @data_scadenza_presentazione_offerta.setter
    def data_scadenza_presentazione_offerta(self, data_scadenza_presentazione_offerta):
        """Sets the data_scadenza_presentazione_offerta of this ElencoSoggettiType.

        Data della scadenza di presentazione dell'offerta  # noqa: E501

        :param data_scadenza_presentazione_offerta: The data_scadenza_presentazione_offerta of this ElencoSoggettiType.  # noqa: E501
        :type: datetime
        """
        if data_scadenza_presentazione_offerta is None:
            raise ValueError("Invalid value for `data_scadenza_presentazione_offerta`, must not be `None`")  # noqa: E501

        self._data_scadenza_presentazione_offerta = data_scadenza_presentazione_offerta

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
        if issubclass(ElencoSoggettiType, dict):
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
        if not isinstance(other, ElencoSoggettiType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
