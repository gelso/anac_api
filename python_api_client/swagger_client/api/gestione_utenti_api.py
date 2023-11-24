# coding: utf-8

"""
    Specifiche Servizi Appalto - OpenAPI 3.0

    Sono descritte le specifiche dei servizi esposti dalla Piattaforma Contratti Pubblici (PCP), richiamabili dalle Stazioni Appaltanti, per la gestione e la raccolta delle informazioni rilevanti nei processi che compongono l’intero ciclo di vita degli appalti.    #### Documentazione   La documentazione a supporto delle specifiche di interfaccia con i sistemi che interoperano con il nuovo sistema di digitalizzazione è redatta con il linguaggio di markup Markdown ed è presente al segunete url:     [documento-specifiche-servizi-npa](https://github.com/anticorruzione/npa/blob/main/docs/specifiche-interfacce/documento-specifiche-servizi-npa.md) ```  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ufficio.uscp@anticorruzione.it
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class GestioneUtentiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def id_incaricato_ricerca(self, id_appalto, **kwargs):  # noqa: E501
        """API Rest per la ricerca dei soggetti incaricati.Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base agli appalti di competenza dell' RP e della SA per la quale sta operando. SINCRONO  # noqa: E501

        viene recuperata la lista con i dati di sintesi dei soggetti incaricati. SINCRONO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.id_incaricato_ricerca(id_appalto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_appalto: Identificativo univoco dell'Appalto definito da ANAC. (A UUID specified by FC4122). (required)
        :param str cig: Non gestito nella prima release - Identificativo univoco Gara-Lotto rilasciato da ANAC
        :param str codice_fiscale: codice fiscale del soggetto
        :param str ruolo: Codice ruolo di un soggetto - fare riferimento ai valori contenuti nel file [tipoRuolo.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoRuolo.json)
        :param str servizio: Non gestito nella prima release - Codice servizio delegato al soggetto - fare riferimento ai valori contenuti nel file [tipoServizioSoggetto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoServizioSoggetto.json)
        :param str operazione: Non gestito nella prima release - Codice operazione delegata al soggetto - fare riferimento ai valori contenuti nel file [tipoOperazioneSoggetto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoOperazioneSoggetto.json)
        :param datetime data_inizio_da: Data inizio incarico soggetto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339)
        :param datetime data_inizio_a: Data inizio incarico soggetto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339)
        :param datetime data_fine_da: Data fine incarico soggetto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339)
        :param datetime data_fine_a: data fine incarico soggetto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339)
        :return: SoggettoListaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.id_incaricato_ricerca_with_http_info(id_appalto, **kwargs)  # noqa: E501
        else:
            (data) = self.id_incaricato_ricerca_with_http_info(id_appalto, **kwargs)  # noqa: E501
            return data

    def id_incaricato_ricerca_with_http_info(self, id_appalto, **kwargs):  # noqa: E501
        """API Rest per la ricerca dei soggetti incaricati.Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base agli appalti di competenza dell' RP e della SA per la quale sta operando. SINCRONO  # noqa: E501

        viene recuperata la lista con i dati di sintesi dei soggetti incaricati. SINCRONO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.id_incaricato_ricerca_with_http_info(id_appalto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_appalto: Identificativo univoco dell'Appalto definito da ANAC. (A UUID specified by FC4122). (required)
        :param str cig: Non gestito nella prima release - Identificativo univoco Gara-Lotto rilasciato da ANAC
        :param str codice_fiscale: codice fiscale del soggetto
        :param str ruolo: Codice ruolo di un soggetto - fare riferimento ai valori contenuti nel file [tipoRuolo.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoRuolo.json)
        :param str servizio: Non gestito nella prima release - Codice servizio delegato al soggetto - fare riferimento ai valori contenuti nel file [tipoServizioSoggetto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoServizioSoggetto.json)
        :param str operazione: Non gestito nella prima release - Codice operazione delegata al soggetto - fare riferimento ai valori contenuti nel file [tipoOperazioneSoggetto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoOperazioneSoggetto.json)
        :param datetime data_inizio_da: Data inizio incarico soggetto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339)
        :param datetime data_inizio_a: Data inizio incarico soggetto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339)
        :param datetime data_fine_da: Data fine incarico soggetto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339)
        :param datetime data_fine_a: data fine incarico soggetto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339)
        :return: SoggettoListaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_appalto', 'cig', 'codice_fiscale', 'ruolo', 'servizio', 'operazione', 'data_inizio_da', 'data_inizio_a', 'data_fine_da', 'data_fine_a']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method id_incaricato_ricerca" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_appalto' is set
        if ('id_appalto' not in params or
                params['id_appalto'] is None):
            raise ValueError("Missing the required parameter `id_appalto` when calling `id_incaricato_ricerca`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id_appalto' in params:
            query_params.append(('idAppalto', params['id_appalto']))  # noqa: E501
        if 'cig' in params:
            query_params.append(('cig', params['cig']))  # noqa: E501
        if 'codice_fiscale' in params:
            query_params.append(('codiceFiscale', params['codice_fiscale']))  # noqa: E501
        if 'ruolo' in params:
            query_params.append(('ruolo', params['ruolo']))  # noqa: E501
        if 'servizio' in params:
            query_params.append(('servizio', params['servizio']))  # noqa: E501
        if 'operazione' in params:
            query_params.append(('operazione', params['operazione']))  # noqa: E501
        if 'data_inizio_da' in params:
            query_params.append(('dataInizioDa', params['data_inizio_da']))  # noqa: E501
        if 'data_inizio_a' in params:
            query_params.append(('dataInizioA', params['data_inizio_a']))  # noqa: E501
        if 'data_fine_da' in params:
            query_params.append(('dataFineDa', params['data_fine_da']))  # noqa: E501
        if 'data_fine_a' in params:
            query_params.append(('dataFineA', params['data_fine_a']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/ricerca-soggetti', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SoggettoListaResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def id_presa_carico(self, body, **kwargs):  # noqa: E501
        """API Rest per l’associazione di un Responsabile di Progetto. SINCRONO  # noqa: E501

        servizio utile per l’associazione di un responsabile di progetto. SINCRONO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.id_presa_carico(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PresaCaricoRequest body: Oggetto generico in ingresso al servizio (required)
        :return: PresaCaricoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.id_presa_carico_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.id_presa_carico_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def id_presa_carico_with_http_info(self, body, **kwargs):  # noqa: E501
        """API Rest per l’associazione di un Responsabile di Progetto. SINCRONO  # noqa: E501

        servizio utile per l’associazione di un responsabile di progetto. SINCRONO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.id_presa_carico_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PresaCaricoRequest body: Oggetto generico in ingresso al servizio (required)
        :return: PresaCaricoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method id_presa_carico" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `id_presa_carico`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/presa-carico', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PresaCaricoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def id_soggetto_aggiungi(self, body, **kwargs):  # noqa: E501
        """API Rest per associare un soggetto delegato. SINCRONO  # noqa: E501

        servizio che ha lo scopo aggiungere l’istanza di un soggetto delegato. SINCRONO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.id_soggetto_aggiungi(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SoggettoRequest body: Oggetto generico in ingresso al servizio (required)
        :return: AggiungiSoggettoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.id_soggetto_aggiungi_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.id_soggetto_aggiungi_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def id_soggetto_aggiungi_with_http_info(self, body, **kwargs):  # noqa: E501
        """API Rest per associare un soggetto delegato. SINCRONO  # noqa: E501

        servizio che ha lo scopo aggiungere l’istanza di un soggetto delegato. SINCRONO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.id_soggetto_aggiungi_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SoggettoRequest body: Oggetto generico in ingresso al servizio (required)
        :return: AggiungiSoggettoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method id_soggetto_aggiungi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `id_soggetto_aggiungi`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/aggiungi-soggetto', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AggiungiSoggettoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def id_soggetto_elimina(self, body, **kwargs):  # noqa: E501
        """API Rest per eliminare da un ruolo un soggetto delegato. SINCRONO  # noqa: E501

        servizio di cancellazione logica di un soggetto. SINCRONO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.id_soggetto_elimina(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EliminaSoggettoRequest body: Oggetto generico in ingresso al servizio (required)
        :return: EliminaSoggettoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.id_soggetto_elimina_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.id_soggetto_elimina_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def id_soggetto_elimina_with_http_info(self, body, **kwargs):  # noqa: E501
        """API Rest per eliminare da un ruolo un soggetto delegato. SINCRONO  # noqa: E501

        servizio di cancellazione logica di un soggetto. SINCRONO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.id_soggetto_elimina_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EliminaSoggettoRequest body: Oggetto generico in ingresso al servizio (required)
        :return: EliminaSoggettoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method id_soggetto_elimina" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `id_soggetto_elimina`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/elimina-soggetto', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EliminaSoggettoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
