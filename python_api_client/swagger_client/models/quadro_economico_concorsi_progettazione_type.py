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

class QuadroEconomicoConcorsiProgettazioneType(object):
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
        'imp_totale_premi': 'float',
        'imp_stimato_prog_successiva': 'float'
    }

    attribute_map = {
        'imp_totale_premi': 'impTotalePremi',
        'imp_stimato_prog_successiva': 'impStimatoProgSuccessiva'
    }

    def __init__(self, imp_totale_premi=None, imp_stimato_prog_successiva=None):  # noqa: E501
        """QuadroEconomicoConcorsiProgettazioneType - a model defined in Swagger"""  # noqa: E501
        self._imp_totale_premi = None
        self._imp_stimato_prog_successiva = None
        self.discriminator = None
        self.imp_totale_premi = imp_totale_premi
        if imp_stimato_prog_successiva is not None:
            self.imp_stimato_prog_successiva = imp_stimato_prog_successiva

    @property
    def imp_totale_premi(self):
        """Gets the imp_totale_premi of this QuadroEconomicoConcorsiProgettazioneType.  # noqa: E501

        Importo totale dei premi  # noqa: E501

        :return: The imp_totale_premi of this QuadroEconomicoConcorsiProgettazioneType.  # noqa: E501
        :rtype: float
        """
        return self._imp_totale_premi

    @imp_totale_premi.setter
    def imp_totale_premi(self, imp_totale_premi):
        """Sets the imp_totale_premi of this QuadroEconomicoConcorsiProgettazioneType.

        Importo totale dei premi  # noqa: E501

        :param imp_totale_premi: The imp_totale_premi of this QuadroEconomicoConcorsiProgettazioneType.  # noqa: E501
        :type: float
        """
        if imp_totale_premi is None:
            raise ValueError("Invalid value for `imp_totale_premi`, must not be `None`")  # noqa: E501

        self._imp_totale_premi = imp_totale_premi

    @property
    def imp_stimato_prog_successiva(self):
        """Gets the imp_stimato_prog_successiva of this QuadroEconomicoConcorsiProgettazioneType.  # noqa: E501

        Importo stimato del servizio di progettazione successiva  # noqa: E501

        :return: The imp_stimato_prog_successiva of this QuadroEconomicoConcorsiProgettazioneType.  # noqa: E501
        :rtype: float
        """
        return self._imp_stimato_prog_successiva

    @imp_stimato_prog_successiva.setter
    def imp_stimato_prog_successiva(self, imp_stimato_prog_successiva):
        """Sets the imp_stimato_prog_successiva of this QuadroEconomicoConcorsiProgettazioneType.

        Importo stimato del servizio di progettazione successiva  # noqa: E501

        :param imp_stimato_prog_successiva: The imp_stimato_prog_successiva of this QuadroEconomicoConcorsiProgettazioneType.  # noqa: E501
        :type: float
        """

        self._imp_stimato_prog_successiva = imp_stimato_prog_successiva

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
        if issubclass(QuadroEconomicoConcorsiProgettazioneType, dict):
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
        if not isinstance(other, QuadroEconomicoConcorsiProgettazioneType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
