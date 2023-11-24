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
from swagger_client.models.lotto_p3_base_type import LottoP3BaseType  # noqa: F401,E501

class LottoP34Type(LottoP3BaseType):
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
        'afferente_investimenti_pnrr': 'bool',
        'categoria': 'CategoriaEnum',
        'servizio_pubblico_locale': 'bool',
        'strumenti_elettronici_specifici': 'bool',
        'contratti_disposizioni_particolari': 'ContrattiDisposizioniParticolariEnum',
        'lavoro_o_acquisto_previsto_in_programmazione': 'bool',
        'cui': 'str',
        'quadro_economico_standard': 'QuadroEconomicoType',
        'dati_base': 'DatiBaseLottoOptionalType',
        'dati_base_cpv': 'DatiBaseCPVType',
        'dati_base_contratto': 'DatiBaseContrattoType',
        'dati_base_aggiudicazione': 'AllOfLottoP34TypeDatiBaseAggiudicazione',
        'dati_base_termini_invio': 'DatiTerminiInvioType',
        'dati_base_accessibilita': 'DatiBaseAccessibilitaType',
        'dati_base_documenti': 'DatiBaseDocumentiOptionalType'
    }
    if hasattr(LottoP3BaseType, "swagger_types"):
        swagger_types.update(LottoP3BaseType.swagger_types)

    attribute_map = {
        'afferente_investimenti_pnrr': 'afferenteInvestimentiPNRR',
        'categoria': 'categoria',
        'servizio_pubblico_locale': 'servizioPubblicoLocale',
        'strumenti_elettronici_specifici': 'strumentiElettroniciSpecifici',
        'contratti_disposizioni_particolari': 'contrattiDisposizioniParticolari',
        'lavoro_o_acquisto_previsto_in_programmazione': 'lavoroOAcquistoPrevistoInProgrammazione',
        'cui': 'cui',
        'quadro_economico_standard': 'quadroEconomicoStandard',
        'dati_base': 'datiBase',
        'dati_base_cpv': 'datiBaseCPV',
        'dati_base_contratto': 'datiBaseContratto',
        'dati_base_aggiudicazione': 'datiBaseAggiudicazione',
        'dati_base_termini_invio': 'datiBaseTerminiInvio',
        'dati_base_accessibilita': 'datiBaseAccessibilita',
        'dati_base_documenti': 'datiBaseDocumenti'
    }
    if hasattr(LottoP3BaseType, "attribute_map"):
        attribute_map.update(LottoP3BaseType.attribute_map)

    def __init__(self, afferente_investimenti_pnrr=None, categoria=None, servizio_pubblico_locale=None, strumenti_elettronici_specifici=None, contratti_disposizioni_particolari=None, lavoro_o_acquisto_previsto_in_programmazione=None, cui=None, quadro_economico_standard=None, dati_base=None, dati_base_cpv=None, dati_base_contratto=None, dati_base_aggiudicazione=None, dati_base_termini_invio=None, dati_base_accessibilita=None, dati_base_documenti=None, *args, **kwargs):  # noqa: E501
        """LottoP34Type - a model defined in Swagger"""  # noqa: E501
        self._afferente_investimenti_pnrr = None
        self._categoria = None
        self._servizio_pubblico_locale = None
        self._strumenti_elettronici_specifici = None
        self._contratti_disposizioni_particolari = None
        self._lavoro_o_acquisto_previsto_in_programmazione = None
        self._cui = None
        self._quadro_economico_standard = None
        self._dati_base = None
        self._dati_base_cpv = None
        self._dati_base_contratto = None
        self._dati_base_aggiudicazione = None
        self._dati_base_termini_invio = None
        self._dati_base_accessibilita = None
        self._dati_base_documenti = None
        self.discriminator = None
        self.afferente_investimenti_pnrr = afferente_investimenti_pnrr
        self.categoria = categoria
        self.servizio_pubblico_locale = servizio_pubblico_locale
        self.strumenti_elettronici_specifici = strumenti_elettronici_specifici
        self.contratti_disposizioni_particolari = contratti_disposizioni_particolari
        self.lavoro_o_acquisto_previsto_in_programmazione = lavoro_o_acquisto_previsto_in_programmazione
        if cui is not None:
            self.cui = cui
        if quadro_economico_standard is not None:
            self.quadro_economico_standard = quadro_economico_standard
        if dati_base is not None:
            self.dati_base = dati_base
        if dati_base_cpv is not None:
            self.dati_base_cpv = dati_base_cpv
        if dati_base_contratto is not None:
            self.dati_base_contratto = dati_base_contratto
        if dati_base_aggiudicazione is not None:
            self.dati_base_aggiudicazione = dati_base_aggiudicazione
        if dati_base_termini_invio is not None:
            self.dati_base_termini_invio = dati_base_termini_invio
        if dati_base_accessibilita is not None:
            self.dati_base_accessibilita = dati_base_accessibilita
        if dati_base_documenti is not None:
            self.dati_base_documenti = dati_base_documenti
        LottoP3BaseType.__init__(self, *args, **kwargs)

    @property
    def afferente_investimenti_pnrr(self):
        """Gets the afferente_investimenti_pnrr of this LottoP34Type.  # noqa: E501

        L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)?  # noqa: E501

        :return: The afferente_investimenti_pnrr of this LottoP34Type.  # noqa: E501
        :rtype: bool
        """
        return self._afferente_investimenti_pnrr

    @afferente_investimenti_pnrr.setter
    def afferente_investimenti_pnrr(self, afferente_investimenti_pnrr):
        """Sets the afferente_investimenti_pnrr of this LottoP34Type.

        L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)?  # noqa: E501

        :param afferente_investimenti_pnrr: The afferente_investimenti_pnrr of this LottoP34Type.  # noqa: E501
        :type: bool
        """
        if afferente_investimenti_pnrr is None:
            raise ValueError("Invalid value for `afferente_investimenti_pnrr`, must not be `None`")  # noqa: E501

        self._afferente_investimenti_pnrr = afferente_investimenti_pnrr

    @property
    def categoria(self):
        """Gets the categoria of this LottoP34Type.  # noqa: E501


        :return: The categoria of this LottoP34Type.  # noqa: E501
        :rtype: CategoriaEnum
        """
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        """Sets the categoria of this LottoP34Type.


        :param categoria: The categoria of this LottoP34Type.  # noqa: E501
        :type: CategoriaEnum
        """
        if categoria is None:
            raise ValueError("Invalid value for `categoria`, must not be `None`")  # noqa: E501

        self._categoria = categoria

    @property
    def servizio_pubblico_locale(self):
        """Gets the servizio_pubblico_locale of this LottoP34Type.  # noqa: E501

        Flag servizio pubblico locale  # noqa: E501

        :return: The servizio_pubblico_locale of this LottoP34Type.  # noqa: E501
        :rtype: bool
        """
        return self._servizio_pubblico_locale

    @servizio_pubblico_locale.setter
    def servizio_pubblico_locale(self, servizio_pubblico_locale):
        """Sets the servizio_pubblico_locale of this LottoP34Type.

        Flag servizio pubblico locale  # noqa: E501

        :param servizio_pubblico_locale: The servizio_pubblico_locale of this LottoP34Type.  # noqa: E501
        :type: bool
        """
        if servizio_pubblico_locale is None:
            raise ValueError("Invalid value for `servizio_pubblico_locale`, must not be `None`")  # noqa: E501

        self._servizio_pubblico_locale = servizio_pubblico_locale

    @property
    def strumenti_elettronici_specifici(self):
        """Gets the strumenti_elettronici_specifici of this LottoP34Type.  # noqa: E501

        Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche  # noqa: E501

        :return: The strumenti_elettronici_specifici of this LottoP34Type.  # noqa: E501
        :rtype: bool
        """
        return self._strumenti_elettronici_specifici

    @strumenti_elettronici_specifici.setter
    def strumenti_elettronici_specifici(self, strumenti_elettronici_specifici):
        """Sets the strumenti_elettronici_specifici of this LottoP34Type.

        Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche  # noqa: E501

        :param strumenti_elettronici_specifici: The strumenti_elettronici_specifici of this LottoP34Type.  # noqa: E501
        :type: bool
        """
        if strumenti_elettronici_specifici is None:
            raise ValueError("Invalid value for `strumenti_elettronici_specifici`, must not be `None`")  # noqa: E501

        self._strumenti_elettronici_specifici = strumenti_elettronici_specifici

    @property
    def contratti_disposizioni_particolari(self):
        """Gets the contratti_disposizioni_particolari of this LottoP34Type.  # noqa: E501


        :return: The contratti_disposizioni_particolari of this LottoP34Type.  # noqa: E501
        :rtype: ContrattiDisposizioniParticolariEnum
        """
        return self._contratti_disposizioni_particolari

    @contratti_disposizioni_particolari.setter
    def contratti_disposizioni_particolari(self, contratti_disposizioni_particolari):
        """Sets the contratti_disposizioni_particolari of this LottoP34Type.


        :param contratti_disposizioni_particolari: The contratti_disposizioni_particolari of this LottoP34Type.  # noqa: E501
        :type: ContrattiDisposizioniParticolariEnum
        """
        if contratti_disposizioni_particolari is None:
            raise ValueError("Invalid value for `contratti_disposizioni_particolari`, must not be `None`")  # noqa: E501

        self._contratti_disposizioni_particolari = contratti_disposizioni_particolari

    @property
    def lavoro_o_acquisto_previsto_in_programmazione(self):
        """Gets the lavoro_o_acquisto_previsto_in_programmazione of this LottoP34Type.  # noqa: E501

        Il lavoro o l’acquisto di bene o servizio è stato previsto all’interno della programmazione  # noqa: E501

        :return: The lavoro_o_acquisto_previsto_in_programmazione of this LottoP34Type.  # noqa: E501
        :rtype: bool
        """
        return self._lavoro_o_acquisto_previsto_in_programmazione

    @lavoro_o_acquisto_previsto_in_programmazione.setter
    def lavoro_o_acquisto_previsto_in_programmazione(self, lavoro_o_acquisto_previsto_in_programmazione):
        """Sets the lavoro_o_acquisto_previsto_in_programmazione of this LottoP34Type.

        Il lavoro o l’acquisto di bene o servizio è stato previsto all’interno della programmazione  # noqa: E501

        :param lavoro_o_acquisto_previsto_in_programmazione: The lavoro_o_acquisto_previsto_in_programmazione of this LottoP34Type.  # noqa: E501
        :type: bool
        """
        if lavoro_o_acquisto_previsto_in_programmazione is None:
            raise ValueError("Invalid value for `lavoro_o_acquisto_previsto_in_programmazione`, must not be `None`")  # noqa: E501

        self._lavoro_o_acquisto_previsto_in_programmazione = lavoro_o_acquisto_previsto_in_programmazione

    @property
    def cui(self):
        """Gets the cui of this LottoP34Type.  # noqa: E501

        CUI programma triennale lavori pubblici o programma biennale forniture e servizi  # noqa: E501

        :return: The cui of this LottoP34Type.  # noqa: E501
        :rtype: str
        """
        return self._cui

    @cui.setter
    def cui(self, cui):
        """Sets the cui of this LottoP34Type.

        CUI programma triennale lavori pubblici o programma biennale forniture e servizi  # noqa: E501

        :param cui: The cui of this LottoP34Type.  # noqa: E501
        :type: str
        """

        self._cui = cui

    @property
    def quadro_economico_standard(self):
        """Gets the quadro_economico_standard of this LottoP34Type.  # noqa: E501


        :return: The quadro_economico_standard of this LottoP34Type.  # noqa: E501
        :rtype: QuadroEconomicoType
        """
        return self._quadro_economico_standard

    @quadro_economico_standard.setter
    def quadro_economico_standard(self, quadro_economico_standard):
        """Sets the quadro_economico_standard of this LottoP34Type.


        :param quadro_economico_standard: The quadro_economico_standard of this LottoP34Type.  # noqa: E501
        :type: QuadroEconomicoType
        """

        self._quadro_economico_standard = quadro_economico_standard

    @property
    def dati_base(self):
        """Gets the dati_base of this LottoP34Type.  # noqa: E501


        :return: The dati_base of this LottoP34Type.  # noqa: E501
        :rtype: DatiBaseLottoOptionalType
        """
        return self._dati_base

    @dati_base.setter
    def dati_base(self, dati_base):
        """Sets the dati_base of this LottoP34Type.


        :param dati_base: The dati_base of this LottoP34Type.  # noqa: E501
        :type: DatiBaseLottoOptionalType
        """

        self._dati_base = dati_base

    @property
    def dati_base_cpv(self):
        """Gets the dati_base_cpv of this LottoP34Type.  # noqa: E501


        :return: The dati_base_cpv of this LottoP34Type.  # noqa: E501
        :rtype: DatiBaseCPVType
        """
        return self._dati_base_cpv

    @dati_base_cpv.setter
    def dati_base_cpv(self, dati_base_cpv):
        """Sets the dati_base_cpv of this LottoP34Type.


        :param dati_base_cpv: The dati_base_cpv of this LottoP34Type.  # noqa: E501
        :type: DatiBaseCPVType
        """

        self._dati_base_cpv = dati_base_cpv

    @property
    def dati_base_contratto(self):
        """Gets the dati_base_contratto of this LottoP34Type.  # noqa: E501


        :return: The dati_base_contratto of this LottoP34Type.  # noqa: E501
        :rtype: DatiBaseContrattoType
        """
        return self._dati_base_contratto

    @dati_base_contratto.setter
    def dati_base_contratto(self, dati_base_contratto):
        """Sets the dati_base_contratto of this LottoP34Type.


        :param dati_base_contratto: The dati_base_contratto of this LottoP34Type.  # noqa: E501
        :type: DatiBaseContrattoType
        """

        self._dati_base_contratto = dati_base_contratto

    @property
    def dati_base_aggiudicazione(self):
        """Gets the dati_base_aggiudicazione of this LottoP34Type.  # noqa: E501


        :return: The dati_base_aggiudicazione of this LottoP34Type.  # noqa: E501
        :rtype: AllOfLottoP34TypeDatiBaseAggiudicazione
        """
        return self._dati_base_aggiudicazione

    @dati_base_aggiudicazione.setter
    def dati_base_aggiudicazione(self, dati_base_aggiudicazione):
        """Sets the dati_base_aggiudicazione of this LottoP34Type.


        :param dati_base_aggiudicazione: The dati_base_aggiudicazione of this LottoP34Type.  # noqa: E501
        :type: AllOfLottoP34TypeDatiBaseAggiudicazione
        """

        self._dati_base_aggiudicazione = dati_base_aggiudicazione

    @property
    def dati_base_termini_invio(self):
        """Gets the dati_base_termini_invio of this LottoP34Type.  # noqa: E501


        :return: The dati_base_termini_invio of this LottoP34Type.  # noqa: E501
        :rtype: DatiTerminiInvioType
        """
        return self._dati_base_termini_invio

    @dati_base_termini_invio.setter
    def dati_base_termini_invio(self, dati_base_termini_invio):
        """Sets the dati_base_termini_invio of this LottoP34Type.


        :param dati_base_termini_invio: The dati_base_termini_invio of this LottoP34Type.  # noqa: E501
        :type: DatiTerminiInvioType
        """

        self._dati_base_termini_invio = dati_base_termini_invio

    @property
    def dati_base_accessibilita(self):
        """Gets the dati_base_accessibilita of this LottoP34Type.  # noqa: E501


        :return: The dati_base_accessibilita of this LottoP34Type.  # noqa: E501
        :rtype: DatiBaseAccessibilitaType
        """
        return self._dati_base_accessibilita

    @dati_base_accessibilita.setter
    def dati_base_accessibilita(self, dati_base_accessibilita):
        """Sets the dati_base_accessibilita of this LottoP34Type.


        :param dati_base_accessibilita: The dati_base_accessibilita of this LottoP34Type.  # noqa: E501
        :type: DatiBaseAccessibilitaType
        """

        self._dati_base_accessibilita = dati_base_accessibilita

    @property
    def dati_base_documenti(self):
        """Gets the dati_base_documenti of this LottoP34Type.  # noqa: E501


        :return: The dati_base_documenti of this LottoP34Type.  # noqa: E501
        :rtype: DatiBaseDocumentiOptionalType
        """
        return self._dati_base_documenti

    @dati_base_documenti.setter
    def dati_base_documenti(self, dati_base_documenti):
        """Sets the dati_base_documenti of this LottoP34Type.


        :param dati_base_documenti: The dati_base_documenti of this LottoP34Type.  # noqa: E501
        :type: DatiBaseDocumentiOptionalType
        """

        self._dati_base_documenti = dati_base_documenti

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
        if issubclass(LottoP34Type, dict):
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
        if not isinstance(other, LottoP34Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
