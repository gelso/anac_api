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

class AvanzamentoType(object):
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
        'denominazione_avanzamento': 'str',
        'modalita_pagamento': 'ModalitaPagamentoEnum',
        'imp_anticipazione': 'float',
        'data_certificato_anticipazione': 'datetime',
        'data_avanzamento': 'datetime',
        'imp_sal': 'float',
        'data_certificato_mandato_pagamento': 'datetime',
        'imp_certificato_mandato_pagamento': 'float',
        'avanzamento': 'AvanzamentoEnum',
        'num_giorni_scostamento': 'float',
        'num_giorni_proroga': 'float'
    }

    attribute_map = {
        'denominazione_avanzamento': 'denominazioneAvanzamento',
        'modalita_pagamento': 'modalitaPagamento',
        'imp_anticipazione': 'impAnticipazione',
        'data_certificato_anticipazione': 'dataCertificatoAnticipazione',
        'data_avanzamento': 'dataAvanzamento',
        'imp_sal': 'impSal',
        'data_certificato_mandato_pagamento': 'dataCertificatoMandatoPagamento',
        'imp_certificato_mandato_pagamento': 'impCertificatoMandatoPagamento',
        'avanzamento': 'avanzamento',
        'num_giorni_scostamento': 'numGiorniScostamento',
        'num_giorni_proroga': 'numGiorniProroga'
    }

    def __init__(self, denominazione_avanzamento=None, modalita_pagamento=None, imp_anticipazione=None, data_certificato_anticipazione=None, data_avanzamento=None, imp_sal=None, data_certificato_mandato_pagamento=None, imp_certificato_mandato_pagamento=None, avanzamento=None, num_giorni_scostamento=None, num_giorni_proroga=None):  # noqa: E501
        """AvanzamentoType - a model defined in Swagger"""  # noqa: E501
        self._denominazione_avanzamento = None
        self._modalita_pagamento = None
        self._imp_anticipazione = None
        self._data_certificato_anticipazione = None
        self._data_avanzamento = None
        self._imp_sal = None
        self._data_certificato_mandato_pagamento = None
        self._imp_certificato_mandato_pagamento = None
        self._avanzamento = None
        self._num_giorni_scostamento = None
        self._num_giorni_proroga = None
        self.discriminator = None
        self.denominazione_avanzamento = denominazione_avanzamento
        self.modalita_pagamento = modalita_pagamento
        if imp_anticipazione is not None:
            self.imp_anticipazione = imp_anticipazione
        if data_certificato_anticipazione is not None:
            self.data_certificato_anticipazione = data_certificato_anticipazione
        self.data_avanzamento = data_avanzamento
        self.imp_sal = imp_sal
        if data_certificato_mandato_pagamento is not None:
            self.data_certificato_mandato_pagamento = data_certificato_mandato_pagamento
        if imp_certificato_mandato_pagamento is not None:
            self.imp_certificato_mandato_pagamento = imp_certificato_mandato_pagamento
        self.avanzamento = avanzamento
        if num_giorni_scostamento is not None:
            self.num_giorni_scostamento = num_giorni_scostamento
        if num_giorni_proroga is not None:
            self.num_giorni_proroga = num_giorni_proroga

    @property
    def denominazione_avanzamento(self):
        """Gets the denominazione_avanzamento of this AvanzamentoType.  # noqa: E501

        Denominazione dello stato di avanzamento  # noqa: E501

        :return: The denominazione_avanzamento of this AvanzamentoType.  # noqa: E501
        :rtype: str
        """
        return self._denominazione_avanzamento

    @denominazione_avanzamento.setter
    def denominazione_avanzamento(self, denominazione_avanzamento):
        """Sets the denominazione_avanzamento of this AvanzamentoType.

        Denominazione dello stato di avanzamento  # noqa: E501

        :param denominazione_avanzamento: The denominazione_avanzamento of this AvanzamentoType.  # noqa: E501
        :type: str
        """
        if denominazione_avanzamento is None:
            raise ValueError("Invalid value for `denominazione_avanzamento`, must not be `None`")  # noqa: E501

        self._denominazione_avanzamento = denominazione_avanzamento

    @property
    def modalita_pagamento(self):
        """Gets the modalita_pagamento of this AvanzamentoType.  # noqa: E501


        :return: The modalita_pagamento of this AvanzamentoType.  # noqa: E501
        :rtype: ModalitaPagamentoEnum
        """
        return self._modalita_pagamento

    @modalita_pagamento.setter
    def modalita_pagamento(self, modalita_pagamento):
        """Sets the modalita_pagamento of this AvanzamentoType.


        :param modalita_pagamento: The modalita_pagamento of this AvanzamentoType.  # noqa: E501
        :type: ModalitaPagamentoEnum
        """
        if modalita_pagamento is None:
            raise ValueError("Invalid value for `modalita_pagamento`, must not be `None`")  # noqa: E501

        self._modalita_pagamento = modalita_pagamento

    @property
    def imp_anticipazione(self):
        """Gets the imp_anticipazione of this AvanzamentoType.  # noqa: E501

        Eventuale anticipazione  # noqa: E501

        :return: The imp_anticipazione of this AvanzamentoType.  # noqa: E501
        :rtype: float
        """
        return self._imp_anticipazione

    @imp_anticipazione.setter
    def imp_anticipazione(self, imp_anticipazione):
        """Sets the imp_anticipazione of this AvanzamentoType.

        Eventuale anticipazione  # noqa: E501

        :param imp_anticipazione: The imp_anticipazione of this AvanzamentoType.  # noqa: E501
        :type: float
        """

        self._imp_anticipazione = imp_anticipazione

    @property
    def data_certificato_anticipazione(self):
        """Gets the data_certificato_anticipazione of this AvanzamentoType.  # noqa: E501

        Data del certificato di pagamento relativo all'anticipazione  # noqa: E501

        :return: The data_certificato_anticipazione of this AvanzamentoType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_certificato_anticipazione

    @data_certificato_anticipazione.setter
    def data_certificato_anticipazione(self, data_certificato_anticipazione):
        """Sets the data_certificato_anticipazione of this AvanzamentoType.

        Data del certificato di pagamento relativo all'anticipazione  # noqa: E501

        :param data_certificato_anticipazione: The data_certificato_anticipazione of this AvanzamentoType.  # noqa: E501
        :type: datetime
        """

        self._data_certificato_anticipazione = data_certificato_anticipazione

    @property
    def data_avanzamento(self):
        """Gets the data_avanzamento of this AvanzamentoType.  # noqa: E501

        Data Stato di avanzamento  # noqa: E501

        :return: The data_avanzamento of this AvanzamentoType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_avanzamento

    @data_avanzamento.setter
    def data_avanzamento(self, data_avanzamento):
        """Sets the data_avanzamento of this AvanzamentoType.

        Data Stato di avanzamento  # noqa: E501

        :param data_avanzamento: The data_avanzamento of this AvanzamentoType.  # noqa: E501
        :type: datetime
        """
        if data_avanzamento is None:
            raise ValueError("Invalid value for `data_avanzamento`, must not be `None`")  # noqa: E501

        self._data_avanzamento = data_avanzamento

    @property
    def imp_sal(self):
        """Gets the imp_sal of this AvanzamentoType.  # noqa: E501

        Importo stato avanzamento progressivo (cumulato)  # noqa: E501

        :return: The imp_sal of this AvanzamentoType.  # noqa: E501
        :rtype: float
        """
        return self._imp_sal

    @imp_sal.setter
    def imp_sal(self, imp_sal):
        """Sets the imp_sal of this AvanzamentoType.

        Importo stato avanzamento progressivo (cumulato)  # noqa: E501

        :param imp_sal: The imp_sal of this AvanzamentoType.  # noqa: E501
        :type: float
        """
        if imp_sal is None:
            raise ValueError("Invalid value for `imp_sal`, must not be `None`")  # noqa: E501

        self._imp_sal = imp_sal

    @property
    def data_certificato_mandato_pagamento(self):
        """Gets the data_certificato_mandato_pagamento of this AvanzamentoType.  # noqa: E501

        Data di emissione del certificato/mandato di pagamento. Per lavori, indicare la data del certificato. Per servizi e forniture, indicare la data del mandato  # noqa: E501

        :return: The data_certificato_mandato_pagamento of this AvanzamentoType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_certificato_mandato_pagamento

    @data_certificato_mandato_pagamento.setter
    def data_certificato_mandato_pagamento(self, data_certificato_mandato_pagamento):
        """Sets the data_certificato_mandato_pagamento of this AvanzamentoType.

        Data di emissione del certificato/mandato di pagamento. Per lavori, indicare la data del certificato. Per servizi e forniture, indicare la data del mandato  # noqa: E501

        :param data_certificato_mandato_pagamento: The data_certificato_mandato_pagamento of this AvanzamentoType.  # noqa: E501
        :type: datetime
        """

        self._data_certificato_mandato_pagamento = data_certificato_mandato_pagamento

    @property
    def imp_certificato_mandato_pagamento(self):
        """Gets the imp_certificato_mandato_pagamento of this AvanzamentoType.  # noqa: E501

        Importo del certificato/mandato di pagamento. Per lavori, indicare l’importo del certificato. Per servizi e forniture, indicare l’importo del mandato  # noqa: E501

        :return: The imp_certificato_mandato_pagamento of this AvanzamentoType.  # noqa: E501
        :rtype: float
        """
        return self._imp_certificato_mandato_pagamento

    @imp_certificato_mandato_pagamento.setter
    def imp_certificato_mandato_pagamento(self, imp_certificato_mandato_pagamento):
        """Sets the imp_certificato_mandato_pagamento of this AvanzamentoType.

        Importo del certificato/mandato di pagamento. Per lavori, indicare l’importo del certificato. Per servizi e forniture, indicare l’importo del mandato  # noqa: E501

        :param imp_certificato_mandato_pagamento: The imp_certificato_mandato_pagamento of this AvanzamentoType.  # noqa: E501
        :type: float
        """

        self._imp_certificato_mandato_pagamento = imp_certificato_mandato_pagamento

    @property
    def avanzamento(self):
        """Gets the avanzamento of this AvanzamentoType.  # noqa: E501


        :return: The avanzamento of this AvanzamentoType.  # noqa: E501
        :rtype: AvanzamentoEnum
        """
        return self._avanzamento

    @avanzamento.setter
    def avanzamento(self, avanzamento):
        """Sets the avanzamento of this AvanzamentoType.


        :param avanzamento: The avanzamento of this AvanzamentoType.  # noqa: E501
        :type: AvanzamentoEnum
        """
        if avanzamento is None:
            raise ValueError("Invalid value for `avanzamento`, must not be `None`")  # noqa: E501

        self._avanzamento = avanzamento

    @property
    def num_giorni_scostamento(self):
        """Gets the num_giorni_scostamento of this AvanzamentoType.  # noqa: E501

        Indicare lo scostamento registrato in numero di giorni  # noqa: E501

        :return: The num_giorni_scostamento of this AvanzamentoType.  # noqa: E501
        :rtype: float
        """
        return self._num_giorni_scostamento

    @num_giorni_scostamento.setter
    def num_giorni_scostamento(self, num_giorni_scostamento):
        """Sets the num_giorni_scostamento of this AvanzamentoType.

        Indicare lo scostamento registrato in numero di giorni  # noqa: E501

        :param num_giorni_scostamento: The num_giorni_scostamento of this AvanzamentoType.  # noqa: E501
        :type: float
        """

        self._num_giorni_scostamento = num_giorni_scostamento

    @property
    def num_giorni_proroga(self):
        """Gets the num_giorni_proroga of this AvanzamentoType.  # noqa: E501

        Indicare il numero di giorni di proroga concessi (non conseguenti a modifiche contrattuali)  # noqa: E501

        :return: The num_giorni_proroga of this AvanzamentoType.  # noqa: E501
        :rtype: float
        """
        return self._num_giorni_proroga

    @num_giorni_proroga.setter
    def num_giorni_proroga(self, num_giorni_proroga):
        """Sets the num_giorni_proroga of this AvanzamentoType.

        Indicare il numero di giorni di proroga concessi (non conseguenti a modifiche contrattuali)  # noqa: E501

        :param num_giorni_proroga: The num_giorni_proroga of this AvanzamentoType.  # noqa: E501
        :type: float
        """

        self._num_giorni_proroga = num_giorni_proroga

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
        if issubclass(AvanzamentoType, dict):
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
        if not isinstance(other, AvanzamentoType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
