# swagger_client.GestioneUtentiApi

All URIs are relative to *https://repositorydocument.swagger.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_incaricato_ricerca**](GestioneUtentiApi.md#id_incaricato_ricerca) | **GET** /ricerca-soggetti | API Rest per la ricerca dei soggetti incaricati.Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base agli appalti di competenza dell&#x27; RP e della SA per la quale sta operando. SINCRONO
[**id_presa_carico**](GestioneUtentiApi.md#id_presa_carico) | **POST** /presa-carico | API Rest per l’associazione di un Responsabile di Progetto. SINCRONO
[**id_soggetto_aggiungi**](GestioneUtentiApi.md#id_soggetto_aggiungi) | **POST** /aggiungi-soggetto | API Rest per associare un soggetto delegato. SINCRONO
[**id_soggetto_elimina**](GestioneUtentiApi.md#id_soggetto_elimina) | **POST** /elimina-soggetto | API Rest per eliminare da un ruolo un soggetto delegato. SINCRONO

# **id_incaricato_ricerca**
> SoggettoListaResponse id_incaricato_ricerca(id_appalto, cig=cig, codice_fiscale=codice_fiscale, ruolo=ruolo, servizio=servizio, operazione=operazione, data_inizio_da=data_inizio_da, data_inizio_a=data_inizio_a, data_fine_da=data_fine_da, data_fine_a=data_fine_a)

API Rest per la ricerca dei soggetti incaricati.Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base agli appalti di competenza dell' RP e della SA per la quale sta operando. SINCRONO

viene recuperata la lista con i dati di sintesi dei soggetti incaricati. SINCRONO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apiKeyAuth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GestioneUtentiApi(swagger_client.ApiClient(configuration))
id_appalto = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo univoco dell'Appalto definito da ANAC. (A UUID specified by FC4122).
cig = 'cig_example' # str | Non gestito nella prima release - Identificativo univoco Gara-Lotto rilasciato da ANAC (optional)
codice_fiscale = 'codice_fiscale_example' # str | codice fiscale del soggetto (optional)
ruolo = 'ruolo_example' # str | Codice ruolo di un soggetto - fare riferimento ai valori contenuti nel file [tipoRuolo.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoRuolo.json) (optional)
servizio = 'servizio_example' # str | Non gestito nella prima release - Codice servizio delegato al soggetto - fare riferimento ai valori contenuti nel file [tipoServizioSoggetto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoServizioSoggetto.json) (optional)
operazione = 'operazione_example' # str | Non gestito nella prima release - Codice operazione delegata al soggetto - fare riferimento ai valori contenuti nel file [tipoOperazioneSoggetto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoOperazioneSoggetto.json) (optional)
data_inizio_da = '2013-10-20T19:20:30+01:00' # datetime | Data inizio incarico soggetto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_inizio_a = '2013-10-20T19:20:30+01:00' # datetime | Data inizio incarico soggetto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_fine_da = '2013-10-20T19:20:30+01:00' # datetime | Data fine incarico soggetto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_fine_a = '2013-10-20T19:20:30+01:00' # datetime | data fine incarico soggetto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)

try:
    # API Rest per la ricerca dei soggetti incaricati.Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base agli appalti di competenza dell' RP e della SA per la quale sta operando. SINCRONO
    api_response = api_instance.id_incaricato_ricerca(id_appalto, cig=cig, codice_fiscale=codice_fiscale, ruolo=ruolo, servizio=servizio, operazione=operazione, data_inizio_da=data_inizio_da, data_inizio_a=data_inizio_a, data_fine_da=data_fine_da, data_fine_a=data_fine_a)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GestioneUtentiApi->id_incaricato_ricerca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_appalto** | [**str**](.md)| Identificativo univoco dell&#x27;Appalto definito da ANAC. (A UUID specified by FC4122). | 
 **cig** | **str**| Non gestito nella prima release - Identificativo univoco Gara-Lotto rilasciato da ANAC | [optional] 
 **codice_fiscale** | **str**| codice fiscale del soggetto | [optional] 
 **ruolo** | **str**| Codice ruolo di un soggetto - fare riferimento ai valori contenuti nel file [tipoRuolo.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoRuolo.json) | [optional] 
 **servizio** | **str**| Non gestito nella prima release - Codice servizio delegato al soggetto - fare riferimento ai valori contenuti nel file [tipoServizioSoggetto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoServizioSoggetto.json) | [optional] 
 **operazione** | **str**| Non gestito nella prima release - Codice operazione delegata al soggetto - fare riferimento ai valori contenuti nel file [tipoOperazioneSoggetto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoOperazioneSoggetto.json) | [optional] 
 **data_inizio_da** | **datetime**| Data inizio incarico soggetto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_inizio_a** | **datetime**| Data inizio incarico soggetto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_fine_da** | **datetime**| Data fine incarico soggetto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_fine_a** | **datetime**| data fine incarico soggetto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 

### Return type

[**SoggettoListaResponse**](SoggettoListaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_presa_carico**
> PresaCaricoResponse id_presa_carico(body)

API Rest per l’associazione di un Responsabile di Progetto. SINCRONO

servizio utile per l’associazione di un responsabile di progetto. SINCRONO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apiKeyAuth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GestioneUtentiApi(swagger_client.ApiClient(configuration))
body = swagger_client.PresaCaricoRequest() # PresaCaricoRequest | Oggetto generico in ingresso al servizio

try:
    # API Rest per l’associazione di un Responsabile di Progetto. SINCRONO
    api_response = api_instance.id_presa_carico(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GestioneUtentiApi->id_presa_carico: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PresaCaricoRequest**](PresaCaricoRequest.md)| Oggetto generico in ingresso al servizio | 

### Return type

[**PresaCaricoResponse**](PresaCaricoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_soggetto_aggiungi**
> AggiungiSoggettoResponse id_soggetto_aggiungi(body)

API Rest per associare un soggetto delegato. SINCRONO

servizio che ha lo scopo aggiungere l’istanza di un soggetto delegato. SINCRONO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apiKeyAuth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GestioneUtentiApi(swagger_client.ApiClient(configuration))
body = swagger_client.SoggettoRequest() # SoggettoRequest | Oggetto generico in ingresso al servizio

try:
    # API Rest per associare un soggetto delegato. SINCRONO
    api_response = api_instance.id_soggetto_aggiungi(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GestioneUtentiApi->id_soggetto_aggiungi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SoggettoRequest**](SoggettoRequest.md)| Oggetto generico in ingresso al servizio | 

### Return type

[**AggiungiSoggettoResponse**](AggiungiSoggettoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_soggetto_elimina**
> EliminaSoggettoResponse id_soggetto_elimina(body)

API Rest per eliminare da un ruolo un soggetto delegato. SINCRONO

servizio di cancellazione logica di un soggetto. SINCRONO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apiKeyAuth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GestioneUtentiApi(swagger_client.ApiClient(configuration))
body = swagger_client.EliminaSoggettoRequest() # EliminaSoggettoRequest | Oggetto generico in ingresso al servizio

try:
    # API Rest per eliminare da un ruolo un soggetto delegato. SINCRONO
    api_response = api_instance.id_soggetto_elimina(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GestioneUtentiApi->id_soggetto_elimina: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EliminaSoggettoRequest**](EliminaSoggettoRequest.md)| Oggetto generico in ingresso al servizio | 

### Return type

[**EliminaSoggettoResponse**](EliminaSoggettoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

