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
from swagger_client.models.appalto_p6_base_type import AppaltoP6BaseType  # noqa: F401,E501

class AppaltoP62Type(AppaltoP6BaseType):
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
        'dati_base': 'DatiBaseAppaltoOptionalType'
    }
    if hasattr(AppaltoP6BaseType, "swagger_types"):
        swagger_types.update(AppaltoP6BaseType.swagger_types)

    attribute_map = {
        'dati_base': 'datiBase'
    }
    if hasattr(AppaltoP6BaseType, "attribute_map"):
        attribute_map.update(AppaltoP6BaseType.attribute_map)

    def __init__(self, dati_base=None, *args, **kwargs):  # noqa: E501
        """AppaltoP62Type - a model defined in Swagger"""  # noqa: E501
        self._dati_base = None
        self.discriminator = None
        if dati_base is not None:
            self.dati_base = dati_base
        AppaltoP6BaseType.__init__(self, *args, **kwargs)

    @property
    def dati_base(self):
        """Gets the dati_base of this AppaltoP62Type.  # noqa: E501


        :return: The dati_base of this AppaltoP62Type.  # noqa: E501
        :rtype: DatiBaseAppaltoOptionalType
        """
        return self._dati_base

    @dati_base.setter
    def dati_base(self, dati_base):
        """Sets the dati_base of this AppaltoP62Type.


        :param dati_base: The dati_base of this AppaltoP62Type.  # noqa: E501
        :type: DatiBaseAppaltoOptionalType
        """

        self._dati_base = dati_base

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
        if issubclass(AppaltoP62Type, dict):
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
        if not isinstance(other, AppaltoP62Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
