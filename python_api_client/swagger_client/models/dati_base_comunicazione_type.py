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

class DatiBaseComunicazioneType(object):
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
        'data_invio_inviti': 'datetime'
    }

    attribute_map = {
        'data_invio_inviti': 'dataInvioInviti'
    }

    def __init__(self, data_invio_inviti=None):  # noqa: E501
        """DatiBaseComunicazioneType - a model defined in Swagger"""  # noqa: E501
        self._data_invio_inviti = None
        self.discriminator = None
        if data_invio_inviti is not None:
            self.data_invio_inviti = data_invio_inviti

    @property
    def data_invio_inviti(self):
        """Gets the data_invio_inviti of this DatiBaseComunicazioneType.  # noqa: E501

        Data stimata dell'invio degli inviti a presentare le offerte - corrisponde al campo bt-130  - Dispatch Invitation Tender del TED  # noqa: E501

        :return: The data_invio_inviti of this DatiBaseComunicazioneType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_invio_inviti

    @data_invio_inviti.setter
    def data_invio_inviti(self, data_invio_inviti):
        """Sets the data_invio_inviti of this DatiBaseComunicazioneType.

        Data stimata dell'invio degli inviti a presentare le offerte - corrisponde al campo bt-130  - Dispatch Invitation Tender del TED  # noqa: E501

        :param data_invio_inviti: The data_invio_inviti of this DatiBaseComunicazioneType.  # noqa: E501
        :type: datetime
        """

        self._data_invio_inviti = data_invio_inviti

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
        if issubclass(DatiBaseComunicazioneType, dict):
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
        if not isinstance(other, DatiBaseComunicazioneType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
