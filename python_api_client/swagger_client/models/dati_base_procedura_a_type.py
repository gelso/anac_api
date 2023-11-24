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

class DatiBaseProceduraAType(object):
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
        'tipo_procedura': 'TipoProceduraEnum',
        'giustificazioni_aggiudicazione_diretta': 'list[GiustificazioneAggiudicazioneDirettaEnum]'
    }

    attribute_map = {
        'tipo_procedura': 'tipoProcedura',
        'giustificazioni_aggiudicazione_diretta': 'giustificazioniAggiudicazioneDiretta'
    }

    def __init__(self, tipo_procedura=None, giustificazioni_aggiudicazione_diretta=None):  # noqa: E501
        """DatiBaseProceduraAType - a model defined in Swagger"""  # noqa: E501
        self._tipo_procedura = None
        self._giustificazioni_aggiudicazione_diretta = None
        self.discriminator = None
        if tipo_procedura is not None:
            self.tipo_procedura = tipo_procedura
        if giustificazioni_aggiudicazione_diretta is not None:
            self.giustificazioni_aggiudicazione_diretta = giustificazioni_aggiudicazione_diretta

    @property
    def tipo_procedura(self):
        """Gets the tipo_procedura of this DatiBaseProceduraAType.  # noqa: E501


        :return: The tipo_procedura of this DatiBaseProceduraAType.  # noqa: E501
        :rtype: TipoProceduraEnum
        """
        return self._tipo_procedura

    @tipo_procedura.setter
    def tipo_procedura(self, tipo_procedura):
        """Sets the tipo_procedura of this DatiBaseProceduraAType.


        :param tipo_procedura: The tipo_procedura of this DatiBaseProceduraAType.  # noqa: E501
        :type: TipoProceduraEnum
        """

        self._tipo_procedura = tipo_procedura

    @property
    def giustificazioni_aggiudicazione_diretta(self):
        """Gets the giustificazioni_aggiudicazione_diretta of this DatiBaseProceduraAType.  # noqa: E501


        :return: The giustificazioni_aggiudicazione_diretta of this DatiBaseProceduraAType.  # noqa: E501
        :rtype: list[GiustificazioneAggiudicazioneDirettaEnum]
        """
        return self._giustificazioni_aggiudicazione_diretta

    @giustificazioni_aggiudicazione_diretta.setter
    def giustificazioni_aggiudicazione_diretta(self, giustificazioni_aggiudicazione_diretta):
        """Sets the giustificazioni_aggiudicazione_diretta of this DatiBaseProceduraAType.


        :param giustificazioni_aggiudicazione_diretta: The giustificazioni_aggiudicazione_diretta of this DatiBaseProceduraAType.  # noqa: E501
        :type: list[GiustificazioneAggiudicazioneDirettaEnum]
        """

        self._giustificazioni_aggiudicazione_diretta = giustificazioni_aggiudicazione_diretta

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
        if issubclass(DatiBaseProceduraAType, dict):
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
        if not isinstance(other, DatiBaseProceduraAType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
