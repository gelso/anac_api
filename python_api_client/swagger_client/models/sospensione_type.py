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

class SospensioneType(object):
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
        'sospensione_parziale': 'bool',
        'data_verbale_sospensione': 'datetime',
        'motivo_sospensione': 'MotivoSospensioneEnum'
    }

    attribute_map = {
        'sospensione_parziale': 'sospensioneParziale',
        'data_verbale_sospensione': 'dataVerbaleSospensione',
        'motivo_sospensione': 'motivoSospensione'
    }

    def __init__(self, sospensione_parziale=None, data_verbale_sospensione=None, motivo_sospensione=None):  # noqa: E501
        """SospensioneType - a model defined in Swagger"""  # noqa: E501
        self._sospensione_parziale = None
        self._data_verbale_sospensione = None
        self._motivo_sospensione = None
        self.discriminator = None
        self.sospensione_parziale = sospensione_parziale
        self.data_verbale_sospensione = data_verbale_sospensione
        self.motivo_sospensione = motivo_sospensione

    @property
    def sospensione_parziale(self):
        """Gets the sospensione_parziale of this SospensioneType.  # noqa: E501

        La sospensione è parziale?  # noqa: E501

        :return: The sospensione_parziale of this SospensioneType.  # noqa: E501
        :rtype: bool
        """
        return self._sospensione_parziale

    @sospensione_parziale.setter
    def sospensione_parziale(self, sospensione_parziale):
        """Sets the sospensione_parziale of this SospensioneType.

        La sospensione è parziale?  # noqa: E501

        :param sospensione_parziale: The sospensione_parziale of this SospensioneType.  # noqa: E501
        :type: bool
        """
        if sospensione_parziale is None:
            raise ValueError("Invalid value for `sospensione_parziale`, must not be `None`")  # noqa: E501

        self._sospensione_parziale = sospensione_parziale

    @property
    def data_verbale_sospensione(self):
        """Gets the data_verbale_sospensione of this SospensioneType.  # noqa: E501

        Data del verbale di sospensione  # noqa: E501

        :return: The data_verbale_sospensione of this SospensioneType.  # noqa: E501
        :rtype: datetime
        """
        return self._data_verbale_sospensione

    @data_verbale_sospensione.setter
    def data_verbale_sospensione(self, data_verbale_sospensione):
        """Sets the data_verbale_sospensione of this SospensioneType.

        Data del verbale di sospensione  # noqa: E501

        :param data_verbale_sospensione: The data_verbale_sospensione of this SospensioneType.  # noqa: E501
        :type: datetime
        """
        if data_verbale_sospensione is None:
            raise ValueError("Invalid value for `data_verbale_sospensione`, must not be `None`")  # noqa: E501

        self._data_verbale_sospensione = data_verbale_sospensione

    @property
    def motivo_sospensione(self):
        """Gets the motivo_sospensione of this SospensioneType.  # noqa: E501


        :return: The motivo_sospensione of this SospensioneType.  # noqa: E501
        :rtype: MotivoSospensioneEnum
        """
        return self._motivo_sospensione

    @motivo_sospensione.setter
    def motivo_sospensione(self, motivo_sospensione):
        """Sets the motivo_sospensione of this SospensioneType.


        :param motivo_sospensione: The motivo_sospensione of this SospensioneType.  # noqa: E501
        :type: MotivoSospensioneEnum
        """
        if motivo_sospensione is None:
            raise ValueError("Invalid value for `motivo_sospensione`, must not be `None`")  # noqa: E501

        self._motivo_sospensione = motivo_sospensione

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
        if issubclass(SospensioneType, dict):
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
        if not isinstance(other, SospensioneType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
