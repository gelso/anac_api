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

class AppaltoAD4Type(object):
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
        'id_appalto': 'str',
        'codice_appalto': 'str',
        'cig': 'str',
        'data_adesione': 'datetime',
        'relazione_unica_sulle_procedure': 'bool',
        'opere_urbanizzazione_scomputo': 'bool',
        'dati_base_subappalti': 'DatiBaseSubappaltiType'
    }

    attribute_map = {
        'id_appalto': 'idAppalto',
        'codice_appalto': 'codiceAppalto',
        'cig': 'cig',
        'data_adesione': 'dataAdesione',
        'relazione_unica_sulle_procedure': 'relazioneUnicaSulleProcedure',
        'opere_urbanizzazione_scomputo': 'opereUrbanizzazioneScomputo',
        'dati_base_subappalti': 'datiBaseSubappalti'
    }

    def __init__(self, id_appalto=None, codice_appalto=None, cig=None, data_adesione=None, relazione_unica_sulle_procedure=None, opere_urbanizzazione_scomputo=None, dati_base_subappalti=None):  # noqa: E501
        """AppaltoAD4Type - a model defined in Swagger"""  # noqa: E501
        self._id_appalto = None
        self._codice_appalto = None
        self._cig = None
        self._data_adesione = None
        self._relazione_unica_sulle_procedure = None
        self._opere_urbanizzazione_scomputo = None
        self._dati_base_subappalti = None
        self.discriminator = None
        if id_appalto is not None:
            self.id_appalto = id_appalto
        self.codice_appalto = codice_appalto
        self.cig = cig
        self.data_adesione = data_adesione
        self.relazione_unica_sulle_procedure = relazione_unica_sulle_procedure
        self.opere_urbanizzazione_scomputo = opere_urbanizzazione_scomputo
        if dati_base_subappalti is not None:
            self.dati_base_subappalti = dati_base_subappalti

    @property
    def id_appalto(self):
        """Gets the id_appalto of this AppaltoAD4Type.  # noqa: E501

        Codice univoco dell'appalto. il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nelle put/post.  # noqa: E501

        :return: The id_appalto of this AppaltoAD4Type.  # noqa: E501
        :rtype: str
        """
        return self._id_appalto

    @id_appalto.setter
    def id_appalto(self, id_appalto):
        """Sets the id_appalto of this AppaltoAD4Type.

        Codice univoco dell'appalto. il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nelle put/post.  # noqa: E501

        :param id_appalto: The id_appalto of this AppaltoAD4Type.  # noqa: E501
        :type: str
        """

        self._id_appalto = id_appalto

    @property
    def codice_appalto(self):
        """Gets the codice_appalto of this AppaltoAD4Type.  # noqa: E501

        Identificativo univoco dell'appalto definito dalla Stazione Appaltante  # noqa: E501

        :return: The codice_appalto of this AppaltoAD4Type.  # noqa: E501
        :rtype: str
        """
        return self._codice_appalto

    @codice_appalto.setter
    def codice_appalto(self, codice_appalto):
        """Sets the codice_appalto of this AppaltoAD4Type.

        Identificativo univoco dell'appalto definito dalla Stazione Appaltante  # noqa: E501

        :param codice_appalto: The codice_appalto of this AppaltoAD4Type.  # noqa: E501
        :type: str
        """
        if codice_appalto is None:
            raise ValueError("Invalid value for `codice_appalto`, must not be `None`")  # noqa: E501

        self._codice_appalto = codice_appalto

    @property
    def cig(self):
        """Gets the cig of this AppaltoAD4Type.  # noqa: E501

        CIG relativo all’accordo quadro/convenzione cui si aderisce  # noqa: E501

        :return: The cig of this AppaltoAD4Type.  # noqa: E501
        :rtype: str
        """
        return self._cig

    @cig.setter
    def cig(self, cig):
        """Sets the cig of this AppaltoAD4Type.

        CIG relativo all’accordo quadro/convenzione cui si aderisce  # noqa: E501

        :param cig: The cig of this AppaltoAD4Type.  # noqa: E501
        :type: str
        """
        if cig is None:
            raise ValueError("Invalid value for `cig`, must not be `None`")  # noqa: E501

        self._cig = cig

    @property
    def data_adesione(self):
        """Gets the data_adesione of this AppaltoAD4Type.  # noqa: E501

        Data di adesione all'accordo quadro/convenzione  # noqa: E501

        :return: The data_adesione of this AppaltoAD4Type.  # noqa: E501
        :rtype: datetime
        """
        return self._data_adesione

    @data_adesione.setter
    def data_adesione(self, data_adesione):
        """Sets the data_adesione of this AppaltoAD4Type.

        Data di adesione all'accordo quadro/convenzione  # noqa: E501

        :param data_adesione: The data_adesione of this AppaltoAD4Type.  # noqa: E501
        :type: datetime
        """
        if data_adesione is None:
            raise ValueError("Invalid value for `data_adesione`, must not be `None`")  # noqa: E501

        self._data_adesione = data_adesione

    @property
    def relazione_unica_sulle_procedure(self):
        """Gets the relazione_unica_sulle_procedure of this AppaltoAD4Type.  # noqa: E501

        Il sottoscritto dichiara che questa SA ha redatto la Relazione Unica sulle Procedure  # noqa: E501

        :return: The relazione_unica_sulle_procedure of this AppaltoAD4Type.  # noqa: E501
        :rtype: bool
        """
        return self._relazione_unica_sulle_procedure

    @relazione_unica_sulle_procedure.setter
    def relazione_unica_sulle_procedure(self, relazione_unica_sulle_procedure):
        """Sets the relazione_unica_sulle_procedure of this AppaltoAD4Type.

        Il sottoscritto dichiara che questa SA ha redatto la Relazione Unica sulle Procedure  # noqa: E501

        :param relazione_unica_sulle_procedure: The relazione_unica_sulle_procedure of this AppaltoAD4Type.  # noqa: E501
        :type: bool
        """
        if relazione_unica_sulle_procedure is None:
            raise ValueError("Invalid value for `relazione_unica_sulle_procedure`, must not be `None`")  # noqa: E501

        self._relazione_unica_sulle_procedure = relazione_unica_sulle_procedure

    @property
    def opere_urbanizzazione_scomputo(self):
        """Gets the opere_urbanizzazione_scomputo of this AppaltoAD4Type.  # noqa: E501

        Opere di urbanizzazione a scomputo  # noqa: E501

        :return: The opere_urbanizzazione_scomputo of this AppaltoAD4Type.  # noqa: E501
        :rtype: bool
        """
        return self._opere_urbanizzazione_scomputo

    @opere_urbanizzazione_scomputo.setter
    def opere_urbanizzazione_scomputo(self, opere_urbanizzazione_scomputo):
        """Sets the opere_urbanizzazione_scomputo of this AppaltoAD4Type.

        Opere di urbanizzazione a scomputo  # noqa: E501

        :param opere_urbanizzazione_scomputo: The opere_urbanizzazione_scomputo of this AppaltoAD4Type.  # noqa: E501
        :type: bool
        """
        if opere_urbanizzazione_scomputo is None:
            raise ValueError("Invalid value for `opere_urbanizzazione_scomputo`, must not be `None`")  # noqa: E501

        self._opere_urbanizzazione_scomputo = opere_urbanizzazione_scomputo

    @property
    def dati_base_subappalti(self):
        """Gets the dati_base_subappalti of this AppaltoAD4Type.  # noqa: E501


        :return: The dati_base_subappalti of this AppaltoAD4Type.  # noqa: E501
        :rtype: DatiBaseSubappaltiType
        """
        return self._dati_base_subappalti

    @dati_base_subappalti.setter
    def dati_base_subappalti(self, dati_base_subappalti):
        """Sets the dati_base_subappalti of this AppaltoAD4Type.


        :param dati_base_subappalti: The dati_base_subappalti of this AppaltoAD4Type.  # noqa: E501
        :type: DatiBaseSubappaltiType
        """

        self._dati_base_subappalti = dati_base_subappalti

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
        if issubclass(AppaltoAD4Type, dict):
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
        if not isinstance(other, AppaltoAD4Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
