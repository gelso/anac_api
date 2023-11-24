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
from swagger_client.models.appalto_p23_type import AppaltoP23Type  # noqa: F401,E501

class AppaltoP223Type(AppaltoP23Type):
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
        'dati_base': 'AllOfAppaltoP223TypeDatiBase',
        'dati_base_procedura': 'AllOfAppaltoP223TypeDatiBaseProcedura'
    }
    if hasattr(AppaltoP23Type, "swagger_types"):
        swagger_types.update(AppaltoP23Type.swagger_types)

    attribute_map = {
        'dati_base': 'datiBase',
        'dati_base_procedura': 'datiBaseProcedura'
    }
    if hasattr(AppaltoP23Type, "attribute_map"):
        attribute_map.update(AppaltoP23Type.attribute_map)

    def __init__(self, dati_base=None, dati_base_procedura=None, *args, **kwargs):  # noqa: E501
        """AppaltoP223Type - a model defined in Swagger"""  # noqa: E501
        self._dati_base = None
        self._dati_base_procedura = None
        self.discriminator = None
        if dati_base is not None:
            self.dati_base = dati_base
        if dati_base_procedura is not None:
            self.dati_base_procedura = dati_base_procedura
        AppaltoP23Type.__init__(self, *args, **kwargs)

    @property
    def dati_base(self):
        """Gets the dati_base of this AppaltoP223Type.  # noqa: E501


        :return: The dati_base of this AppaltoP223Type.  # noqa: E501
        :rtype: AllOfAppaltoP223TypeDatiBase
        """
        return self._dati_base

    @dati_base.setter
    def dati_base(self, dati_base):
        """Sets the dati_base of this AppaltoP223Type.


        :param dati_base: The dati_base of this AppaltoP223Type.  # noqa: E501
        :type: AllOfAppaltoP223TypeDatiBase
        """

        self._dati_base = dati_base

    @property
    def dati_base_procedura(self):
        """Gets the dati_base_procedura of this AppaltoP223Type.  # noqa: E501


        :return: The dati_base_procedura of this AppaltoP223Type.  # noqa: E501
        :rtype: AllOfAppaltoP223TypeDatiBaseProcedura
        """
        return self._dati_base_procedura

    @dati_base_procedura.setter
    def dati_base_procedura(self, dati_base_procedura):
        """Sets the dati_base_procedura of this AppaltoP223Type.


        :param dati_base_procedura: The dati_base_procedura of this AppaltoP223Type.  # noqa: E501
        :type: AllOfAppaltoP223TypeDatiBaseProcedura
        """

        self._dati_base_procedura = dati_base_procedura

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
        if issubclass(AppaltoP223Type, dict):
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
        if not isinstance(other, AppaltoP223Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
