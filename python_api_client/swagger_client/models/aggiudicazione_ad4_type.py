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

class AggiudicazioneAD4Type(object):
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
        'lot_identifier': 'str',
        'afferente_investimenti_pnrr': 'bool',
        'cup_lotto': 'list[str]',
        'parita_di_genere_generazionale': 'ParitaDiGenereGenerazionaleType',
        'quadro_economico_standard': 'QuadroEconomicoType',
        'quadro_economico_concessioni': 'QuadroEconomicoConcessioniType',
        'finanziamenti': 'list[FinanziamentoType]',
        'partecipanti': 'list[PartecipanteADType]',
        'dati_base_aggiudicazione_appalto_type': 'DatiBaseAggiudicazioneAppaltoType',
        'dati_base_accessibilita': 'DatiBaseAccessibilitaType'
    }

    attribute_map = {
        'lot_identifier': 'lotIdentifier',
        'afferente_investimenti_pnrr': 'afferenteInvestimentiPNRR',
        'cup_lotto': 'cupLotto',
        'parita_di_genere_generazionale': 'paritaDiGenereGenerazionale',
        'quadro_economico_standard': 'quadroEconomicoStandard',
        'quadro_economico_concessioni': 'quadroEconomicoConcessioni',
        'finanziamenti': 'finanziamenti',
        'partecipanti': 'partecipanti',
        'dati_base_aggiudicazione_appalto_type': 'datiBaseAggiudicazioneAppaltoType',
        'dati_base_accessibilita': 'datiBaseAccessibilita'
    }

    def __init__(self, lot_identifier=None, afferente_investimenti_pnrr=None, cup_lotto=None, parita_di_genere_generazionale=None, quadro_economico_standard=None, quadro_economico_concessioni=None, finanziamenti=None, partecipanti=None, dati_base_aggiudicazione_appalto_type=None, dati_base_accessibilita=None):  # noqa: E501
        """AggiudicazioneAD4Type - a model defined in Swagger"""  # noqa: E501
        self._lot_identifier = None
        self._afferente_investimenti_pnrr = None
        self._cup_lotto = None
        self._parita_di_genere_generazionale = None
        self._quadro_economico_standard = None
        self._quadro_economico_concessioni = None
        self._finanziamenti = None
        self._partecipanti = None
        self._dati_base_aggiudicazione_appalto_type = None
        self._dati_base_accessibilita = None
        self.discriminator = None
        self.lot_identifier = lot_identifier
        self.afferente_investimenti_pnrr = afferente_investimenti_pnrr
        if cup_lotto is not None:
            self.cup_lotto = cup_lotto
        if parita_di_genere_generazionale is not None:
            self.parita_di_genere_generazionale = parita_di_genere_generazionale
        if quadro_economico_standard is not None:
            self.quadro_economico_standard = quadro_economico_standard
        if quadro_economico_concessioni is not None:
            self.quadro_economico_concessioni = quadro_economico_concessioni
        if finanziamenti is not None:
            self.finanziamenti = finanziamenti
        self.partecipanti = partecipanti
        if dati_base_aggiudicazione_appalto_type is not None:
            self.dati_base_aggiudicazione_appalto_type = dati_base_aggiudicazione_appalto_type
        if dati_base_accessibilita is not None:
            self.dati_base_accessibilita = dati_base_accessibilita

    @property
    def lot_identifier(self):
        """Gets the lot_identifier of this AggiudicazioneAD4Type.  # noqa: E501

        Id univoco del lotto generato dalla stazione appaltante - corrisponde al campo bt-137 - Purpose Lot Identifier del TED  # noqa: E501

        :return: The lot_identifier of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: str
        """
        return self._lot_identifier

    @lot_identifier.setter
    def lot_identifier(self, lot_identifier):
        """Sets the lot_identifier of this AggiudicazioneAD4Type.

        Id univoco del lotto generato dalla stazione appaltante - corrisponde al campo bt-137 - Purpose Lot Identifier del TED  # noqa: E501

        :param lot_identifier: The lot_identifier of this AggiudicazioneAD4Type.  # noqa: E501
        :type: str
        """
        if lot_identifier is None:
            raise ValueError("Invalid value for `lot_identifier`, must not be `None`")  # noqa: E501

        self._lot_identifier = lot_identifier

    @property
    def afferente_investimenti_pnrr(self):
        """Gets the afferente_investimenti_pnrr of this AggiudicazioneAD4Type.  # noqa: E501

        L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)?  # noqa: E501

        :return: The afferente_investimenti_pnrr of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: bool
        """
        return self._afferente_investimenti_pnrr

    @afferente_investimenti_pnrr.setter
    def afferente_investimenti_pnrr(self, afferente_investimenti_pnrr):
        """Sets the afferente_investimenti_pnrr of this AggiudicazioneAD4Type.

        L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)?  # noqa: E501

        :param afferente_investimenti_pnrr: The afferente_investimenti_pnrr of this AggiudicazioneAD4Type.  # noqa: E501
        :type: bool
        """
        if afferente_investimenti_pnrr is None:
            raise ValueError("Invalid value for `afferente_investimenti_pnrr`, must not be `None`")  # noqa: E501

        self._afferente_investimenti_pnrr = afferente_investimenti_pnrr

    @property
    def cup_lotto(self):
        """Gets the cup_lotto of this AggiudicazioneAD4Type.  # noqa: E501

        Cup associati al lotto  # noqa: E501

        :return: The cup_lotto of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: list[str]
        """
        return self._cup_lotto

    @cup_lotto.setter
    def cup_lotto(self, cup_lotto):
        """Sets the cup_lotto of this AggiudicazioneAD4Type.

        Cup associati al lotto  # noqa: E501

        :param cup_lotto: The cup_lotto of this AggiudicazioneAD4Type.  # noqa: E501
        :type: list[str]
        """

        self._cup_lotto = cup_lotto

    @property
    def parita_di_genere_generazionale(self):
        """Gets the parita_di_genere_generazionale of this AggiudicazioneAD4Type.  # noqa: E501


        :return: The parita_di_genere_generazionale of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: ParitaDiGenereGenerazionaleType
        """
        return self._parita_di_genere_generazionale

    @parita_di_genere_generazionale.setter
    def parita_di_genere_generazionale(self, parita_di_genere_generazionale):
        """Sets the parita_di_genere_generazionale of this AggiudicazioneAD4Type.


        :param parita_di_genere_generazionale: The parita_di_genere_generazionale of this AggiudicazioneAD4Type.  # noqa: E501
        :type: ParitaDiGenereGenerazionaleType
        """

        self._parita_di_genere_generazionale = parita_di_genere_generazionale

    @property
    def quadro_economico_standard(self):
        """Gets the quadro_economico_standard of this AggiudicazioneAD4Type.  # noqa: E501


        :return: The quadro_economico_standard of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: QuadroEconomicoType
        """
        return self._quadro_economico_standard

    @quadro_economico_standard.setter
    def quadro_economico_standard(self, quadro_economico_standard):
        """Sets the quadro_economico_standard of this AggiudicazioneAD4Type.


        :param quadro_economico_standard: The quadro_economico_standard of this AggiudicazioneAD4Type.  # noqa: E501
        :type: QuadroEconomicoType
        """

        self._quadro_economico_standard = quadro_economico_standard

    @property
    def quadro_economico_concessioni(self):
        """Gets the quadro_economico_concessioni of this AggiudicazioneAD4Type.  # noqa: E501


        :return: The quadro_economico_concessioni of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: QuadroEconomicoConcessioniType
        """
        return self._quadro_economico_concessioni

    @quadro_economico_concessioni.setter
    def quadro_economico_concessioni(self, quadro_economico_concessioni):
        """Sets the quadro_economico_concessioni of this AggiudicazioneAD4Type.


        :param quadro_economico_concessioni: The quadro_economico_concessioni of this AggiudicazioneAD4Type.  # noqa: E501
        :type: QuadroEconomicoConcessioniType
        """

        self._quadro_economico_concessioni = quadro_economico_concessioni

    @property
    def finanziamenti(self):
        """Gets the finanziamenti of this AggiudicazioneAD4Type.  # noqa: E501

        Dati relativi ai finanziamenti  # noqa: E501

        :return: The finanziamenti of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: list[FinanziamentoType]
        """
        return self._finanziamenti

    @finanziamenti.setter
    def finanziamenti(self, finanziamenti):
        """Sets the finanziamenti of this AggiudicazioneAD4Type.

        Dati relativi ai finanziamenti  # noqa: E501

        :param finanziamenti: The finanziamenti of this AggiudicazioneAD4Type.  # noqa: E501
        :type: list[FinanziamentoType]
        """

        self._finanziamenti = finanziamenti

    @property
    def partecipanti(self):
        """Gets the partecipanti of this AggiudicazioneAD4Type.  # noqa: E501


        :return: The partecipanti of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: list[PartecipanteADType]
        """
        return self._partecipanti

    @partecipanti.setter
    def partecipanti(self, partecipanti):
        """Sets the partecipanti of this AggiudicazioneAD4Type.


        :param partecipanti: The partecipanti of this AggiudicazioneAD4Type.  # noqa: E501
        :type: list[PartecipanteADType]
        """
        if partecipanti is None:
            raise ValueError("Invalid value for `partecipanti`, must not be `None`")  # noqa: E501

        self._partecipanti = partecipanti

    @property
    def dati_base_aggiudicazione_appalto_type(self):
        """Gets the dati_base_aggiudicazione_appalto_type of this AggiudicazioneAD4Type.  # noqa: E501


        :return: The dati_base_aggiudicazione_appalto_type of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: DatiBaseAggiudicazioneAppaltoType
        """
        return self._dati_base_aggiudicazione_appalto_type

    @dati_base_aggiudicazione_appalto_type.setter
    def dati_base_aggiudicazione_appalto_type(self, dati_base_aggiudicazione_appalto_type):
        """Sets the dati_base_aggiudicazione_appalto_type of this AggiudicazioneAD4Type.


        :param dati_base_aggiudicazione_appalto_type: The dati_base_aggiudicazione_appalto_type of this AggiudicazioneAD4Type.  # noqa: E501
        :type: DatiBaseAggiudicazioneAppaltoType
        """

        self._dati_base_aggiudicazione_appalto_type = dati_base_aggiudicazione_appalto_type

    @property
    def dati_base_accessibilita(self):
        """Gets the dati_base_accessibilita of this AggiudicazioneAD4Type.  # noqa: E501


        :return: The dati_base_accessibilita of this AggiudicazioneAD4Type.  # noqa: E501
        :rtype: DatiBaseAccessibilitaType
        """
        return self._dati_base_accessibilita

    @dati_base_accessibilita.setter
    def dati_base_accessibilita(self, dati_base_accessibilita):
        """Sets the dati_base_accessibilita of this AggiudicazioneAD4Type.


        :param dati_base_accessibilita: The dati_base_accessibilita of this AggiudicazioneAD4Type.  # noqa: E501
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
        if issubclass(AggiudicazioneAD4Type, dict):
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
        if not isinstance(other, AggiudicazioneAD4Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
