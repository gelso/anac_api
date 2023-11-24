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

class ModificaContrattuale40Type(object):
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
        'data_approvazione': 'datetime',
        'url_documentazione': 'str',
        'motivo_revisione_prezzi': 'MotiviRevisionePrezziEnum',
        'cig_nuova_procedura': 'str',
        'quadro_economico_concessioni_rideterminato': 'QuadroEconomicoConcessioniType'
    }

    attribute_map = {
        'data_approvazione': 'dataApprovazione',
        'url_documentazione': 'urlDocumentazione',
        'motivo_revisione_prezzi': 'motivoRevisionePrezzi',
        'cig_nuova_procedura': 'cigNuovaProcedura',
        'quadro_economico_concessioni_rideterminato': 'quadroEconomicoConcessioniRideterminato'
    }

    def __init__(self, data_approvazione=None, url_documentazione=None, motivo_revisione_prezzi=None, cig_nuova_procedura=None, quadro_economico_concessioni_rideterminato=None):  # noqa: E501
        """ModificaContrattuale40Type - a model defined in Swagger"""  # noqa: E501
        self._data_approvazione = None
        self._url_documentazione = None
        self._motivo_revisione_prezzi = None
        self._cig_nuova_procedura = None
        self._quadro_economico_concessioni_rideterminato = None
        self.discriminator = None
        if data_approvazione is not None:
            self.data_approvazione = data_approvazione
        if url_documentazione is not None:
            self.url_documentazione = url_documentazione
        if motivo_revisione_prezzi is not None:
            self.motivo_revisione_prezzi = motivo_revisione_prezzi
        if cig_nuova_procedura is not None:
            self.cig_nuova_procedura = cig_nuova_procedura
        if quadro_economico_concessioni_rideterminato is not None:
            self.quadro_economico_concessioni_rideterminato = quadro_economico_concessioni_rideterminato

    @property
    def data_approvazione(self):
        """Gets the data_approvazione of this ModificaContrattuale40Type.  # noqa: E501

        Data di approvazione della modifica contrattuale  # noqa: E501

        :return: The data_approvazione of this ModificaContrattuale40Type.  # noqa: E501
        :rtype: datetime
        """
        return self._data_approvazione

    @data_approvazione.setter
    def data_approvazione(self, data_approvazione):
        """Sets the data_approvazione of this ModificaContrattuale40Type.

        Data di approvazione della modifica contrattuale  # noqa: E501

        :param data_approvazione: The data_approvazione of this ModificaContrattuale40Type.  # noqa: E501
        :type: datetime
        """

        self._data_approvazione = data_approvazione

    @property
    def url_documentazione(self):
        """Gets the url_documentazione of this ModificaContrattuale40Type.  # noqa: E501

        URL documentazione varianti in corso d’opera  # noqa: E501

        :return: The url_documentazione of this ModificaContrattuale40Type.  # noqa: E501
        :rtype: str
        """
        return self._url_documentazione

    @url_documentazione.setter
    def url_documentazione(self, url_documentazione):
        """Sets the url_documentazione of this ModificaContrattuale40Type.

        URL documentazione varianti in corso d’opera  # noqa: E501

        :param url_documentazione: The url_documentazione of this ModificaContrattuale40Type.  # noqa: E501
        :type: str
        """

        self._url_documentazione = url_documentazione

    @property
    def motivo_revisione_prezzi(self):
        """Gets the motivo_revisione_prezzi of this ModificaContrattuale40Type.  # noqa: E501


        :return: The motivo_revisione_prezzi of this ModificaContrattuale40Type.  # noqa: E501
        :rtype: MotiviRevisionePrezziEnum
        """
        return self._motivo_revisione_prezzi

    @motivo_revisione_prezzi.setter
    def motivo_revisione_prezzi(self, motivo_revisione_prezzi):
        """Sets the motivo_revisione_prezzi of this ModificaContrattuale40Type.


        :param motivo_revisione_prezzi: The motivo_revisione_prezzi of this ModificaContrattuale40Type.  # noqa: E501
        :type: MotiviRevisionePrezziEnum
        """

        self._motivo_revisione_prezzi = motivo_revisione_prezzi

    @property
    def cig_nuova_procedura(self):
        """Gets the cig_nuova_procedura of this ModificaContrattuale40Type.  # noqa: E501

        CIG della nuova procedura avviata  # noqa: E501

        :return: The cig_nuova_procedura of this ModificaContrattuale40Type.  # noqa: E501
        :rtype: str
        """
        return self._cig_nuova_procedura

    @cig_nuova_procedura.setter
    def cig_nuova_procedura(self, cig_nuova_procedura):
        """Sets the cig_nuova_procedura of this ModificaContrattuale40Type.

        CIG della nuova procedura avviata  # noqa: E501

        :param cig_nuova_procedura: The cig_nuova_procedura of this ModificaContrattuale40Type.  # noqa: E501
        :type: str
        """

        self._cig_nuova_procedura = cig_nuova_procedura

    @property
    def quadro_economico_concessioni_rideterminato(self):
        """Gets the quadro_economico_concessioni_rideterminato of this ModificaContrattuale40Type.  # noqa: E501


        :return: The quadro_economico_concessioni_rideterminato of this ModificaContrattuale40Type.  # noqa: E501
        :rtype: QuadroEconomicoConcessioniType
        """
        return self._quadro_economico_concessioni_rideterminato

    @quadro_economico_concessioni_rideterminato.setter
    def quadro_economico_concessioni_rideterminato(self, quadro_economico_concessioni_rideterminato):
        """Sets the quadro_economico_concessioni_rideterminato of this ModificaContrattuale40Type.


        :param quadro_economico_concessioni_rideterminato: The quadro_economico_concessioni_rideterminato of this ModificaContrattuale40Type.  # noqa: E501
        :type: QuadroEconomicoConcessioniType
        """

        self._quadro_economico_concessioni_rideterminato = quadro_economico_concessioni_rideterminato

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
        if issubclass(ModificaContrattuale40Type, dict):
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
        if not isinstance(other, ModificaContrattuale40Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
