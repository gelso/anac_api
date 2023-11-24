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

class CreaSchedaRequest(object):
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
        'scheda': 'SchedaPostPubblicazioneType'
    }

    attribute_map = {
        'id_appalto': 'idAppalto',
        'scheda': 'scheda'
    }

    def __init__(self, id_appalto=None, scheda=None):  # noqa: E501
        """CreaSchedaRequest - a model defined in Swagger"""  # noqa: E501
        self._id_appalto = None
        self._scheda = None
        self.discriminator = None
        self.id_appalto = id_appalto
        self.scheda = scheda

    @property
    def id_appalto(self):
        """Gets the id_appalto of this CreaSchedaRequest.  # noqa: E501

        identificativo univoco dell'Appalto generato da ANAC.  # noqa: E501

        :return: The id_appalto of this CreaSchedaRequest.  # noqa: E501
        :rtype: str
        """
        return self._id_appalto

    @id_appalto.setter
    def id_appalto(self, id_appalto):
        """Sets the id_appalto of this CreaSchedaRequest.

        identificativo univoco dell'Appalto generato da ANAC.  # noqa: E501

        :param id_appalto: The id_appalto of this CreaSchedaRequest.  # noqa: E501
        :type: str
        """
        if id_appalto is None:
            raise ValueError("Invalid value for `id_appalto`, must not be `None`")  # noqa: E501

        self._id_appalto = id_appalto

    @property
    def scheda(self):
        """Gets the scheda of this CreaSchedaRequest.  # noqa: E501


        :return: The scheda of this CreaSchedaRequest.  # noqa: E501
        :rtype: SchedaPostPubblicazioneType
        """
        return self._scheda

    @scheda.setter
    def scheda(self, scheda):
        """Sets the scheda of this CreaSchedaRequest.


        :param scheda: The scheda of this CreaSchedaRequest.  # noqa: E501
        :type: SchedaPostPubblicazioneType
        """
        if scheda is None:
            raise ValueError("Invalid value for `scheda`, must not be `None`")  # noqa: E501

        self._scheda = scheda

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
        if issubclass(CreaSchedaRequest, dict):
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
        if not isinstance(other, CreaSchedaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
