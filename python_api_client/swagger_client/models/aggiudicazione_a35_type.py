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

class AggiudicazioneA35Type(object):
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
        'cig': 'str',
        'numero_offerte_ammesse': 'float',
        'offerte_presentate': 'list[OfferteType]',
        'quadro_economico_concessioni': 'QuadroEconomicoConcessioniType',
        'dati_base_risultato_procedura': 'AllOfAggiudicazioneA35TypeDatiBaseRisultatoProcedura',
        'dati_base_aggiudicazione_appalto': 'DatiBaseAggiudicazioneAppaltoType',
        'dati_base_accessibilita': 'DatiBaseAccessibilitaType'
    }

    attribute_map = {
        'cig': 'cig',
        'numero_offerte_ammesse': 'numeroOfferteAmmesse',
        'offerte_presentate': 'offertePresentate',
        'quadro_economico_concessioni': 'quadroEconomicoConcessioni',
        'dati_base_risultato_procedura': 'datiBaseRisultatoProcedura',
        'dati_base_aggiudicazione_appalto': 'datiBaseAggiudicazioneAppalto',
        'dati_base_accessibilita': 'datiBaseAccessibilita'
    }

    def __init__(self, cig=None, numero_offerte_ammesse=None, offerte_presentate=None, quadro_economico_concessioni=None, dati_base_risultato_procedura=None, dati_base_aggiudicazione_appalto=None, dati_base_accessibilita=None):  # noqa: E501
        """AggiudicazioneA35Type - a model defined in Swagger"""  # noqa: E501
        self._cig = None
        self._numero_offerte_ammesse = None
        self._offerte_presentate = None
        self._quadro_economico_concessioni = None
        self._dati_base_risultato_procedura = None
        self._dati_base_aggiudicazione_appalto = None
        self._dati_base_accessibilita = None
        self.discriminator = None
        self.cig = cig
        self.numero_offerte_ammesse = numero_offerte_ammesse
        if offerte_presentate is not None:
            self.offerte_presentate = offerte_presentate
        if quadro_economico_concessioni is not None:
            self.quadro_economico_concessioni = quadro_economico_concessioni
        if dati_base_risultato_procedura is not None:
            self.dati_base_risultato_procedura = dati_base_risultato_procedura
        if dati_base_aggiudicazione_appalto is not None:
            self.dati_base_aggiudicazione_appalto = dati_base_aggiudicazione_appalto
        if dati_base_accessibilita is not None:
            self.dati_base_accessibilita = dati_base_accessibilita

    @property
    def cig(self):
        """Gets the cig of this AggiudicazioneA35Type.  # noqa: E501

        codice identificativo lotto  # noqa: E501

        :return: The cig of this AggiudicazioneA35Type.  # noqa: E501
        :rtype: str
        """
        return self._cig

    @cig.setter
    def cig(self, cig):
        """Sets the cig of this AggiudicazioneA35Type.

        codice identificativo lotto  # noqa: E501

        :param cig: The cig of this AggiudicazioneA35Type.  # noqa: E501
        :type: str
        """
        if cig is None:
            raise ValueError("Invalid value for `cig`, must not be `None`")  # noqa: E501

        self._cig = cig

    @property
    def numero_offerte_ammesse(self):
        """Gets the numero_offerte_ammesse of this AggiudicazioneA35Type.  # noqa: E501

        numero di offerte ammesse  # noqa: E501

        :return: The numero_offerte_ammesse of this AggiudicazioneA35Type.  # noqa: E501
        :rtype: float
        """
        return self._numero_offerte_ammesse

    @numero_offerte_ammesse.setter
    def numero_offerte_ammesse(self, numero_offerte_ammesse):
        """Sets the numero_offerte_ammesse of this AggiudicazioneA35Type.

        numero di offerte ammesse  # noqa: E501

        :param numero_offerte_ammesse: The numero_offerte_ammesse of this AggiudicazioneA35Type.  # noqa: E501
        :type: float
        """
        if numero_offerte_ammesse is None:
            raise ValueError("Invalid value for `numero_offerte_ammesse`, must not be `None`")  # noqa: E501

        self._numero_offerte_ammesse = numero_offerte_ammesse

    @property
    def offerte_presentate(self):
        """Gets the offerte_presentate of this AggiudicazioneA35Type.  # noqa: E501

        Dati degli aggiudicatari  # noqa: E501

        :return: The offerte_presentate of this AggiudicazioneA35Type.  # noqa: E501
        :rtype: list[OfferteType]
        """
        return self._offerte_presentate

    @offerte_presentate.setter
    def offerte_presentate(self, offerte_presentate):
        """Sets the offerte_presentate of this AggiudicazioneA35Type.

        Dati degli aggiudicatari  # noqa: E501

        :param offerte_presentate: The offerte_presentate of this AggiudicazioneA35Type.  # noqa: E501
        :type: list[OfferteType]
        """

        self._offerte_presentate = offerte_presentate

    @property
    def quadro_economico_concessioni(self):
        """Gets the quadro_economico_concessioni of this AggiudicazioneA35Type.  # noqa: E501


        :return: The quadro_economico_concessioni of this AggiudicazioneA35Type.  # noqa: E501
        :rtype: QuadroEconomicoConcessioniType
        """
        return self._quadro_economico_concessioni

    @quadro_economico_concessioni.setter
    def quadro_economico_concessioni(self, quadro_economico_concessioni):
        """Sets the quadro_economico_concessioni of this AggiudicazioneA35Type.


        :param quadro_economico_concessioni: The quadro_economico_concessioni of this AggiudicazioneA35Type.  # noqa: E501
        :type: QuadroEconomicoConcessioniType
        """

        self._quadro_economico_concessioni = quadro_economico_concessioni

    @property
    def dati_base_risultato_procedura(self):
        """Gets the dati_base_risultato_procedura of this AggiudicazioneA35Type.  # noqa: E501


        :return: The dati_base_risultato_procedura of this AggiudicazioneA35Type.  # noqa: E501
        :rtype: AllOfAggiudicazioneA35TypeDatiBaseRisultatoProcedura
        """
        return self._dati_base_risultato_procedura

    @dati_base_risultato_procedura.setter
    def dati_base_risultato_procedura(self, dati_base_risultato_procedura):
        """Sets the dati_base_risultato_procedura of this AggiudicazioneA35Type.


        :param dati_base_risultato_procedura: The dati_base_risultato_procedura of this AggiudicazioneA35Type.  # noqa: E501
        :type: AllOfAggiudicazioneA35TypeDatiBaseRisultatoProcedura
        """

        self._dati_base_risultato_procedura = dati_base_risultato_procedura

    @property
    def dati_base_aggiudicazione_appalto(self):
        """Gets the dati_base_aggiudicazione_appalto of this AggiudicazioneA35Type.  # noqa: E501


        :return: The dati_base_aggiudicazione_appalto of this AggiudicazioneA35Type.  # noqa: E501
        :rtype: DatiBaseAggiudicazioneAppaltoType
        """
        return self._dati_base_aggiudicazione_appalto

    @dati_base_aggiudicazione_appalto.setter
    def dati_base_aggiudicazione_appalto(self, dati_base_aggiudicazione_appalto):
        """Sets the dati_base_aggiudicazione_appalto of this AggiudicazioneA35Type.


        :param dati_base_aggiudicazione_appalto: The dati_base_aggiudicazione_appalto of this AggiudicazioneA35Type.  # noqa: E501
        :type: DatiBaseAggiudicazioneAppaltoType
        """

        self._dati_base_aggiudicazione_appalto = dati_base_aggiudicazione_appalto

    @property
    def dati_base_accessibilita(self):
        """Gets the dati_base_accessibilita of this AggiudicazioneA35Type.  # noqa: E501


        :return: The dati_base_accessibilita of this AggiudicazioneA35Type.  # noqa: E501
        :rtype: DatiBaseAccessibilitaType
        """
        return self._dati_base_accessibilita

    @dati_base_accessibilita.setter
    def dati_base_accessibilita(self, dati_base_accessibilita):
        """Sets the dati_base_accessibilita of this AggiudicazioneA35Type.


        :param dati_base_accessibilita: The dati_base_accessibilita of this AggiudicazioneA35Type.  # noqa: E501
        :type: DatiBaseAccessibilitaType
        """

        self._dati_base_accessibilita = dati_base_accessibilita

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
        if issubclass(AggiudicazioneA35Type, dict):
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
        if not isinstance(other, AggiudicazioneA35Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
