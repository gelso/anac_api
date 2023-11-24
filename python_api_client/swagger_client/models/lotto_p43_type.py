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
from swagger_client.models.lotto_p4_base_type import LottoP4BaseType  # noqa: F401,E501

class LottoP43Type(LottoP4BaseType):
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
        'strumenti_elettronici_specifici': 'bool'
    }
    if hasattr(LottoP4BaseType, "swagger_types"):
        swagger_types.update(LottoP4BaseType.swagger_types)

    attribute_map = {
        'strumenti_elettronici_specifici': 'strumentiElettroniciSpecifici'
    }
    if hasattr(LottoP4BaseType, "attribute_map"):
        attribute_map.update(LottoP4BaseType.attribute_map)

    def __init__(self, strumenti_elettronici_specifici=None, *args, **kwargs):  # noqa: E501
        """LottoP43Type - a model defined in Swagger"""  # noqa: E501
        self._strumenti_elettronici_specifici = None
        self.discriminator = None
        if strumenti_elettronici_specifici is not None:
            self.strumenti_elettronici_specifici = strumenti_elettronici_specifici
        LottoP4BaseType.__init__(self, *args, **kwargs)

    @property
    def strumenti_elettronici_specifici(self):
        """Gets the strumenti_elettronici_specifici of this LottoP43Type.  # noqa: E501

        Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche  # noqa: E501

        :return: The strumenti_elettronici_specifici of this LottoP43Type.  # noqa: E501
        :rtype: bool
        """
        return self._strumenti_elettronici_specifici

    @strumenti_elettronici_specifici.setter
    def strumenti_elettronici_specifici(self, strumenti_elettronici_specifici):
        """Sets the strumenti_elettronici_specifici of this LottoP43Type.

        Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche  # noqa: E501

        :param strumenti_elettronici_specifici: The strumenti_elettronici_specifici of this LottoP43Type.  # noqa: E501
        :type: bool
        """

        self._strumenti_elettronici_specifici = strumenti_elettronici_specifici

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
        if issubclass(LottoP43Type, dict):
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
        if not isinstance(other, LottoP43Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
