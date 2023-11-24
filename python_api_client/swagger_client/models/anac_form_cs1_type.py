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

class AnacFormCS1Type(object):
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
        'id_scheda': 'str',
        'subappalto': 'SubappaltoType2'
    }

    attribute_map = {
        'id_scheda': 'idScheda',
        'subappalto': 'subappalto'
    }

    def __init__(self, id_scheda=None, subappalto=None):  # noqa: E501
        """AnacFormCS1Type - a model defined in Swagger"""  # noqa: E501
        self._id_scheda = None
        self._subappalto = None
        self.discriminator = None
        self.id_scheda = id_scheda
        self.subappalto = subappalto

    @property
    def id_scheda(self):
        """Gets the id_scheda of this AnacFormCS1Type.  # noqa: E501

        identificativo restituito dal servizio all’invio della scheda di esito subappalto.  # noqa: E501

        :return: The id_scheda of this AnacFormCS1Type.  # noqa: E501
        :rtype: str
        """
        return self._id_scheda

    @id_scheda.setter
    def id_scheda(self, id_scheda):
        """Sets the id_scheda of this AnacFormCS1Type.

        identificativo restituito dal servizio all’invio della scheda di esito subappalto.  # noqa: E501

        :param id_scheda: The id_scheda of this AnacFormCS1Type.  # noqa: E501
        :type: str
        """
        if id_scheda is None:
            raise ValueError("Invalid value for `id_scheda`, must not be `None`")  # noqa: E501

        self._id_scheda = id_scheda

    @property
    def subappalto(self):
        """Gets the subappalto of this AnacFormCS1Type.  # noqa: E501


        :return: The subappalto of this AnacFormCS1Type.  # noqa: E501
        :rtype: SubappaltoType2
        """
        return self._subappalto

    @subappalto.setter
    def subappalto(self, subappalto):
        """Sets the subappalto of this AnacFormCS1Type.


        :param subappalto: The subappalto of this AnacFormCS1Type.  # noqa: E501
        :type: SubappaltoType2
        """
        if subappalto is None:
            raise ValueError("Invalid value for `subappalto`, must not be `None`")  # noqa: E501

        self._subappalto = subappalto

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
        if issubclass(AnacFormCS1Type, dict):
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
        if not isinstance(other, AnacFormCS1Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
