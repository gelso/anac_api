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

class AppaltoAD5Type(object):
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
        'codice_fiscale_sa': 'str',
        'denominazione_sa': 'str'
    }

    attribute_map = {
        'id_appalto': 'idAppalto',
        'codice_appalto': 'codiceAppalto',
        'codice_fiscale_sa': 'codiceFiscaleSA',
        'denominazione_sa': 'denominazioneSA'
    }

    def __init__(self, id_appalto=None, codice_appalto=None, codice_fiscale_sa=None, denominazione_sa=None):  # noqa: E501
        """AppaltoAD5Type - a model defined in Swagger"""  # noqa: E501
        self._id_appalto = None
        self._codice_appalto = None
        self._codice_fiscale_sa = None
        self._denominazione_sa = None
        self.discriminator = None
        if id_appalto is not None:
            self.id_appalto = id_appalto
        self.codice_appalto = codice_appalto
        self.codice_fiscale_sa = codice_fiscale_sa
        self.denominazione_sa = denominazione_sa

    @property
    def id_appalto(self):
        """Gets the id_appalto of this AppaltoAD5Type.  # noqa: E501

        Codice univoco dell'appalto. il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nelle put/post.  # noqa: E501

        :return: The id_appalto of this AppaltoAD5Type.  # noqa: E501
        :rtype: str
        """
        return self._id_appalto

    @id_appalto.setter
    def id_appalto(self, id_appalto):
        """Sets the id_appalto of this AppaltoAD5Type.

        Codice univoco dell'appalto. il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nelle put/post.  # noqa: E501

        :param id_appalto: The id_appalto of this AppaltoAD5Type.  # noqa: E501
        :type: str
        """

        self._id_appalto = id_appalto

    @property
    def codice_appalto(self):
        """Gets the codice_appalto of this AppaltoAD5Type.  # noqa: E501

        Identificativo univoco dell'appalto definito dalla Stazione Appaltante  # noqa: E501

        :return: The codice_appalto of this AppaltoAD5Type.  # noqa: E501
        :rtype: str
        """
        return self._codice_appalto

    @codice_appalto.setter
    def codice_appalto(self, codice_appalto):
        """Sets the codice_appalto of this AppaltoAD5Type.

        Identificativo univoco dell'appalto definito dalla Stazione Appaltante  # noqa: E501

        :param codice_appalto: The codice_appalto of this AppaltoAD5Type.  # noqa: E501
        :type: str
        """
        if codice_appalto is None:
            raise ValueError("Invalid value for `codice_appalto`, must not be `None`")  # noqa: E501

        self._codice_appalto = codice_appalto

    @property
    def codice_fiscale_sa(self):
        """Gets the codice_fiscale_sa of this AppaltoAD5Type.  # noqa: E501

        Codice fiscale SA  # noqa: E501

        :return: The codice_fiscale_sa of this AppaltoAD5Type.  # noqa: E501
        :rtype: str
        """
        return self._codice_fiscale_sa

    @codice_fiscale_sa.setter
    def codice_fiscale_sa(self, codice_fiscale_sa):
        """Sets the codice_fiscale_sa of this AppaltoAD5Type.

        Codice fiscale SA  # noqa: E501

        :param codice_fiscale_sa: The codice_fiscale_sa of this AppaltoAD5Type.  # noqa: E501
        :type: str
        """
        if codice_fiscale_sa is None:
            raise ValueError("Invalid value for `codice_fiscale_sa`, must not be `None`")  # noqa: E501

        self._codice_fiscale_sa = codice_fiscale_sa

    @property
    def denominazione_sa(self):
        """Gets the denominazione_sa of this AppaltoAD5Type.  # noqa: E501

        Denominazione SA  # noqa: E501

        :return: The denominazione_sa of this AppaltoAD5Type.  # noqa: E501
        :rtype: str
        """
        return self._denominazione_sa

    @denominazione_sa.setter
    def denominazione_sa(self, denominazione_sa):
        """Sets the denominazione_sa of this AppaltoAD5Type.

        Denominazione SA  # noqa: E501

        :param denominazione_sa: The denominazione_sa of this AppaltoAD5Type.  # noqa: E501
        :type: str
        """
        if denominazione_sa is None:
            raise ValueError("Invalid value for `denominazione_sa`, must not be `None`")  # noqa: E501

        self._denominazione_sa = denominazione_sa

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
        if issubclass(AppaltoAD5Type, dict):
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
        if not isinstance(other, AppaltoAD5Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
