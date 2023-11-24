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
from swagger_client.models.lotto_base_type import LottoBaseType  # noqa: F401,E501

class LottoP10Type(LottoBaseType):
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
        'prestazioni_comprese': 'PrestazioniEnum',
        'servizio_pubblico_locale': 'bool',
        'ripetizioni_e_consegne_complementari': 'bool',
        'sa_non_soggetta_obblighi24_dicembre2015': 'bool',
        'iniziative_non_soddisfacenti': 'bool',
        'strumenti_elettronici_specifici': 'bool',
        'ccnl': 'str',
        'tipologia_lavoro': 'list[TipologiaLavoroEnum]',
        'modalita_acquisizione': 'ModalitaAcquisizioneEnum',
        'opzioni_rinnovi': 'bool',
        'ipotesi_collegamento': 'IpotesiCollegamentoType',
        'categoria': 'CategoriaEnum',
        'parita_di_genere_generazionale': 'ParitaDiGenereGenerazionaleType',
        'quadro_economico_standard': 'QuadroEconomicoType'
    }
    if hasattr(LottoBaseType, "swagger_types"):
        swagger_types.update(LottoBaseType.swagger_types)

    attribute_map = {
        'prestazioni_comprese': 'prestazioniComprese',
        'servizio_pubblico_locale': 'servizioPubblicoLocale',
        'ripetizioni_e_consegne_complementari': 'ripetizioniEConsegneComplementari',
        'sa_non_soggetta_obblighi24_dicembre2015': 'saNonSoggettaObblighi24Dicembre2015',
        'iniziative_non_soddisfacenti': 'iniziativeNonSoddisfacenti',
        'strumenti_elettronici_specifici': 'strumentiElettroniciSpecifici',
        'ccnl': 'ccnl',
        'tipologia_lavoro': 'tipologiaLavoro',
        'modalita_acquisizione': 'modalitaAcquisizione',
        'opzioni_rinnovi': 'opzioniRinnovi',
        'ipotesi_collegamento': 'ipotesiCollegamento',
        'categoria': 'categoria',
        'parita_di_genere_generazionale': 'paritaDiGenereGenerazionale',
        'quadro_economico_standard': 'quadroEconomicoStandard'
    }
    if hasattr(LottoBaseType, "attribute_map"):
        attribute_map.update(LottoBaseType.attribute_map)

    def __init__(self, prestazioni_comprese=None, servizio_pubblico_locale=None, ripetizioni_e_consegne_complementari=None, sa_non_soggetta_obblighi24_dicembre2015=None, iniziative_non_soddisfacenti=None, strumenti_elettronici_specifici=None, ccnl=None, tipologia_lavoro=None, modalita_acquisizione=None, opzioni_rinnovi=None, ipotesi_collegamento=None, categoria=None, parita_di_genere_generazionale=None, quadro_economico_standard=None, *args, **kwargs):  # noqa: E501
        """LottoP10Type - a model defined in Swagger"""  # noqa: E501
        self._prestazioni_comprese = None
        self._servizio_pubblico_locale = None
        self._ripetizioni_e_consegne_complementari = None
        self._sa_non_soggetta_obblighi24_dicembre2015 = None
        self._iniziative_non_soddisfacenti = None
        self._strumenti_elettronici_specifici = None
        self._ccnl = None
        self._tipologia_lavoro = None
        self._modalita_acquisizione = None
        self._opzioni_rinnovi = None
        self._ipotesi_collegamento = None
        self._categoria = None
        self._parita_di_genere_generazionale = None
        self._quadro_economico_standard = None
        self.discriminator = None
        self.prestazioni_comprese = prestazioni_comprese
        if servizio_pubblico_locale is not None:
            self.servizio_pubblico_locale = servizio_pubblico_locale
        self.ripetizioni_e_consegne_complementari = ripetizioni_e_consegne_complementari
        if sa_non_soggetta_obblighi24_dicembre2015 is not None:
            self.sa_non_soggetta_obblighi24_dicembre2015 = sa_non_soggetta_obblighi24_dicembre2015
        if iniziative_non_soddisfacenti is not None:
            self.iniziative_non_soddisfacenti = iniziative_non_soddisfacenti
        if strumenti_elettronici_specifici is not None:
            self.strumenti_elettronici_specifici = strumenti_elettronici_specifici
        self.ccnl = ccnl
        self.tipologia_lavoro = tipologia_lavoro
        if modalita_acquisizione is not None:
            self.modalita_acquisizione = modalita_acquisizione
        self.opzioni_rinnovi = opzioni_rinnovi
        if ipotesi_collegamento is not None:
            self.ipotesi_collegamento = ipotesi_collegamento
        self.categoria = categoria
        if parita_di_genere_generazionale is not None:
            self.parita_di_genere_generazionale = parita_di_genere_generazionale
        if quadro_economico_standard is not None:
            self.quadro_economico_standard = quadro_economico_standard
        LottoBaseType.__init__(self, *args, **kwargs)

    @property
    def prestazioni_comprese(self):
        """Gets the prestazioni_comprese of this LottoP10Type.  # noqa: E501


        :return: The prestazioni_comprese of this LottoP10Type.  # noqa: E501
        :rtype: PrestazioniEnum
        """
        return self._prestazioni_comprese

    @prestazioni_comprese.setter
    def prestazioni_comprese(self, prestazioni_comprese):
        """Sets the prestazioni_comprese of this LottoP10Type.


        :param prestazioni_comprese: The prestazioni_comprese of this LottoP10Type.  # noqa: E501
        :type: PrestazioniEnum
        """
        if prestazioni_comprese is None:
            raise ValueError("Invalid value for `prestazioni_comprese`, must not be `None`")  # noqa: E501

        self._prestazioni_comprese = prestazioni_comprese

    @property
    def servizio_pubblico_locale(self):
        """Gets the servizio_pubblico_locale of this LottoP10Type.  # noqa: E501

        Flag servizio pubblico locale  # noqa: E501

        :return: The servizio_pubblico_locale of this LottoP10Type.  # noqa: E501
        :rtype: bool
        """
        return self._servizio_pubblico_locale

    @servizio_pubblico_locale.setter
    def servizio_pubblico_locale(self, servizio_pubblico_locale):
        """Sets the servizio_pubblico_locale of this LottoP10Type.

        Flag servizio pubblico locale  # noqa: E501

        :param servizio_pubblico_locale: The servizio_pubblico_locale of this LottoP10Type.  # noqa: E501
        :type: bool
        """

        self._servizio_pubblico_locale = servizio_pubblico_locale

    @property
    def ripetizioni_e_consegne_complementari(self):
        """Gets the ripetizioni_e_consegne_complementari of this LottoP10Type.  # noqa: E501

        L’appalto prevede ripetizioni di servizi/forniture/lavori analoghi e consegne complementari?  # noqa: E501

        :return: The ripetizioni_e_consegne_complementari of this LottoP10Type.  # noqa: E501
        :rtype: bool
        """
        return self._ripetizioni_e_consegne_complementari

    @ripetizioni_e_consegne_complementari.setter
    def ripetizioni_e_consegne_complementari(self, ripetizioni_e_consegne_complementari):
        """Sets the ripetizioni_e_consegne_complementari of this LottoP10Type.

        L’appalto prevede ripetizioni di servizi/forniture/lavori analoghi e consegne complementari?  # noqa: E501

        :param ripetizioni_e_consegne_complementari: The ripetizioni_e_consegne_complementari of this LottoP10Type.  # noqa: E501
        :type: bool
        """
        if ripetizioni_e_consegne_complementari is None:
            raise ValueError("Invalid value for `ripetizioni_e_consegne_complementari`, must not be `None`")  # noqa: E501

        self._ripetizioni_e_consegne_complementari = ripetizioni_e_consegne_complementari

    @property
    def sa_non_soggetta_obblighi24_dicembre2015(self):
        """Gets the sa_non_soggetta_obblighi24_dicembre2015 of this LottoP10Type.  # noqa: E501

        Che questa stazione appaltante non è soggetta agli obblighi del DPCM 24 dicembre 2015 e ss.mm.ii.  # noqa: E501

        :return: The sa_non_soggetta_obblighi24_dicembre2015 of this LottoP10Type.  # noqa: E501
        :rtype: bool
        """
        return self._sa_non_soggetta_obblighi24_dicembre2015

    @sa_non_soggetta_obblighi24_dicembre2015.setter
    def sa_non_soggetta_obblighi24_dicembre2015(self, sa_non_soggetta_obblighi24_dicembre2015):
        """Sets the sa_non_soggetta_obblighi24_dicembre2015 of this LottoP10Type.

        Che questa stazione appaltante non è soggetta agli obblighi del DPCM 24 dicembre 2015 e ss.mm.ii.  # noqa: E501

        :param sa_non_soggetta_obblighi24_dicembre2015: The sa_non_soggetta_obblighi24_dicembre2015 of this LottoP10Type.  # noqa: E501
        :type: bool
        """

        self._sa_non_soggetta_obblighi24_dicembre2015 = sa_non_soggetta_obblighi24_dicembre2015

    @property
    def iniziative_non_soddisfacenti(self):
        """Gets the iniziative_non_soddisfacenti of this LottoP10Type.  # noqa: E501

        Che nessuna delle iniziative disponibili presso i soggetti aggregatori di riferimento ha caratteristiche in grado di soddisfare i fabbisogni di questa stazione appaltante  # noqa: E501

        :return: The iniziative_non_soddisfacenti of this LottoP10Type.  # noqa: E501
        :rtype: bool
        """
        return self._iniziative_non_soddisfacenti

    @iniziative_non_soddisfacenti.setter
    def iniziative_non_soddisfacenti(self, iniziative_non_soddisfacenti):
        """Sets the iniziative_non_soddisfacenti of this LottoP10Type.

        Che nessuna delle iniziative disponibili presso i soggetti aggregatori di riferimento ha caratteristiche in grado di soddisfare i fabbisogni di questa stazione appaltante  # noqa: E501

        :param iniziative_non_soddisfacenti: The iniziative_non_soddisfacenti of this LottoP10Type.  # noqa: E501
        :type: bool
        """

        self._iniziative_non_soddisfacenti = iniziative_non_soddisfacenti

    @property
    def strumenti_elettronici_specifici(self):
        """Gets the strumenti_elettronici_specifici of this LottoP10Type.  # noqa: E501

        Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche  # noqa: E501

        :return: The strumenti_elettronici_specifici of this LottoP10Type.  # noqa: E501
        :rtype: bool
        """
        return self._strumenti_elettronici_specifici

    @strumenti_elettronici_specifici.setter
    def strumenti_elettronici_specifici(self, strumenti_elettronici_specifici):
        """Sets the strumenti_elettronici_specifici of this LottoP10Type.

        Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche  # noqa: E501

        :param strumenti_elettronici_specifici: The strumenti_elettronici_specifici of this LottoP10Type.  # noqa: E501
        :type: bool
        """

        self._strumenti_elettronici_specifici = strumenti_elettronici_specifici

    @property
    def ccnl(self):
        """Gets the ccnl of this LottoP10Type.  # noqa: E501

        indicare il codice CNEL o non applicabile  # noqa: E501

        :return: The ccnl of this LottoP10Type.  # noqa: E501
        :rtype: str
        """
        return self._ccnl

    @ccnl.setter
    def ccnl(self, ccnl):
        """Sets the ccnl of this LottoP10Type.

        indicare il codice CNEL o non applicabile  # noqa: E501

        :param ccnl: The ccnl of this LottoP10Type.  # noqa: E501
        :type: str
        """
        if ccnl is None:
            raise ValueError("Invalid value for `ccnl`, must not be `None`")  # noqa: E501

        self._ccnl = ccnl

    @property
    def tipologia_lavoro(self):
        """Gets the tipologia_lavoro of this LottoP10Type.  # noqa: E501


        :return: The tipologia_lavoro of this LottoP10Type.  # noqa: E501
        :rtype: list[TipologiaLavoroEnum]
        """
        return self._tipologia_lavoro

    @tipologia_lavoro.setter
    def tipologia_lavoro(self, tipologia_lavoro):
        """Sets the tipologia_lavoro of this LottoP10Type.


        :param tipologia_lavoro: The tipologia_lavoro of this LottoP10Type.  # noqa: E501
        :type: list[TipologiaLavoroEnum]
        """
        if tipologia_lavoro is None:
            raise ValueError("Invalid value for `tipologia_lavoro`, must not be `None`")  # noqa: E501

        self._tipologia_lavoro = tipologia_lavoro

    @property
    def modalita_acquisizione(self):
        """Gets the modalita_acquisizione of this LottoP10Type.  # noqa: E501


        :return: The modalita_acquisizione of this LottoP10Type.  # noqa: E501
        :rtype: ModalitaAcquisizioneEnum
        """
        return self._modalita_acquisizione

    @modalita_acquisizione.setter
    def modalita_acquisizione(self, modalita_acquisizione):
        """Sets the modalita_acquisizione of this LottoP10Type.


        :param modalita_acquisizione: The modalita_acquisizione of this LottoP10Type.  # noqa: E501
        :type: ModalitaAcquisizioneEnum
        """

        self._modalita_acquisizione = modalita_acquisizione

    @property
    def opzioni_rinnovi(self):
        """Gets the opzioni_rinnovi of this LottoP10Type.  # noqa: E501

        L’appalto prevede opzioni/rinnovi?  # noqa: E501

        :return: The opzioni_rinnovi of this LottoP10Type.  # noqa: E501
        :rtype: bool
        """
        return self._opzioni_rinnovi

    @opzioni_rinnovi.setter
    def opzioni_rinnovi(self, opzioni_rinnovi):
        """Sets the opzioni_rinnovi of this LottoP10Type.

        L’appalto prevede opzioni/rinnovi?  # noqa: E501

        :param opzioni_rinnovi: The opzioni_rinnovi of this LottoP10Type.  # noqa: E501
        :type: bool
        """
        if opzioni_rinnovi is None:
            raise ValueError("Invalid value for `opzioni_rinnovi`, must not be `None`")  # noqa: E501

        self._opzioni_rinnovi = opzioni_rinnovi

    @property
    def ipotesi_collegamento(self):
        """Gets the ipotesi_collegamento of this LottoP10Type.  # noqa: E501


        :return: The ipotesi_collegamento of this LottoP10Type.  # noqa: E501
        :rtype: IpotesiCollegamentoType
        """
        return self._ipotesi_collegamento

    @ipotesi_collegamento.setter
    def ipotesi_collegamento(self, ipotesi_collegamento):
        """Sets the ipotesi_collegamento of this LottoP10Type.


        :param ipotesi_collegamento: The ipotesi_collegamento of this LottoP10Type.  # noqa: E501
        :type: IpotesiCollegamentoType
        """

        self._ipotesi_collegamento = ipotesi_collegamento

    @property
    def categoria(self):
        """Gets the categoria of this LottoP10Type.  # noqa: E501


        :return: The categoria of this LottoP10Type.  # noqa: E501
        :rtype: CategoriaEnum
        """
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        """Sets the categoria of this LottoP10Type.


        :param categoria: The categoria of this LottoP10Type.  # noqa: E501
        :type: CategoriaEnum
        """
        if categoria is None:
            raise ValueError("Invalid value for `categoria`, must not be `None`")  # noqa: E501

        self._categoria = categoria

    @property
    def parita_di_genere_generazionale(self):
        """Gets the parita_di_genere_generazionale of this LottoP10Type.  # noqa: E501


        :return: The parita_di_genere_generazionale of this LottoP10Type.  # noqa: E501
        :rtype: ParitaDiGenereGenerazionaleType
        """
        return self._parita_di_genere_generazionale

    @parita_di_genere_generazionale.setter
    def parita_di_genere_generazionale(self, parita_di_genere_generazionale):
        """Sets the parita_di_genere_generazionale of this LottoP10Type.


        :param parita_di_genere_generazionale: The parita_di_genere_generazionale of this LottoP10Type.  # noqa: E501
        :type: ParitaDiGenereGenerazionaleType
        """

        self._parita_di_genere_generazionale = parita_di_genere_generazionale

    @property
    def quadro_economico_standard(self):
        """Gets the quadro_economico_standard of this LottoP10Type.  # noqa: E501


        :return: The quadro_economico_standard of this LottoP10Type.  # noqa: E501
        :rtype: QuadroEconomicoType
        """
        return self._quadro_economico_standard

    @quadro_economico_standard.setter
    def quadro_economico_standard(self, quadro_economico_standard):
        """Sets the quadro_economico_standard of this LottoP10Type.


        :param quadro_economico_standard: The quadro_economico_standard of this LottoP10Type.  # noqa: E501
        :type: QuadroEconomicoType
        """

        self._quadro_economico_standard = quadro_economico_standard

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
        if issubclass(LottoP10Type, dict):
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
        if not isinstance(other, LottoP10Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
