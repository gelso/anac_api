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
from swagger_client.models.aggiudicazione_completa_type import AggiudicazioneCompletaType  # noqa: F401,E501

class AggiudicazioneA133Type(AggiudicazioneCompletaType):
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
        'numero_offerte_ammesse': 'float',
        'esito_procedura_annullata': 'EsitoProceduraAnnullataEnum'
    }
    if hasattr(AggiudicazioneCompletaType, "swagger_types"):
        swagger_types.update(AggiudicazioneCompletaType.swagger_types)

    attribute_map = {
        'numero_offerte_ammesse': 'numeroOfferteAmmesse',
        'esito_procedura_annullata': 'esitoProceduraAnnullata'
    }
    if hasattr(AggiudicazioneCompletaType, "attribute_map"):
        attribute_map.update(AggiudicazioneCompletaType.attribute_map)

    def __init__(self, numero_offerte_ammesse=None, esito_procedura_annullata=None, *args, **kwargs):  # noqa: E501
        """AggiudicazioneA133Type - a model defined in Swagger"""  # noqa: E501
        self._numero_offerte_ammesse = None
        self._esito_procedura_annullata = None
        self.discriminator = None
        self.numero_offerte_ammesse = numero_offerte_ammesse
        if esito_procedura_annullata is not None:
            self.esito_procedura_annullata = esito_procedura_annullata
        AggiudicazioneCompletaType.__init__(self, *args, **kwargs)

    @property
    def numero_offerte_ammesse(self):
        """Gets the numero_offerte_ammesse of this AggiudicazioneA133Type.  # noqa: E501

        numero di offerte ammesse  # noqa: E501

        :return: The numero_offerte_ammesse of this AggiudicazioneA133Type.  # noqa: E501
        :rtype: float
        """
        return self._numero_offerte_ammesse

    @numero_offerte_ammesse.setter
    def numero_offerte_ammesse(self, numero_offerte_ammesse):
        """Sets the numero_offerte_ammesse of this AggiudicazioneA133Type.

        numero di offerte ammesse  # noqa: E501

        :param numero_offerte_ammesse: The numero_offerte_ammesse of this AggiudicazioneA133Type.  # noqa: E501
        :type: float
        """
        if numero_offerte_ammesse is None:
            raise ValueError("Invalid value for `numero_offerte_ammesse`, must not be `None`")  # noqa: E501

        self._numero_offerte_ammesse = numero_offerte_ammesse

    @property
    def esito_procedura_annullata(self):
        """Gets the esito_procedura_annullata of this AggiudicazioneA133Type.  # noqa: E501


        :return: The esito_procedura_annullata of this AggiudicazioneA133Type.  # noqa: E501
        :rtype: EsitoProceduraAnnullataEnum
        """
        return self._esito_procedura_annullata

    @esito_procedura_annullata.setter
    def esito_procedura_annullata(self, esito_procedura_annullata):
        """Sets the esito_procedura_annullata of this AggiudicazioneA133Type.


        :param esito_procedura_annullata: The esito_procedura_annullata of this AggiudicazioneA133Type.  # noqa: E501
        :type: EsitoProceduraAnnullataEnum
        """

        self._esito_procedura_annullata = esito_procedura_annullata

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
        if issubclass(AggiudicazioneA133Type, dict):
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
        if not isinstance(other, AggiudicazioneA133Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
