# swagger_client.ComunicaAppaltoApi

All URIs are relative to *https://repositorydocument.swagger.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_appalto_cancella**](ComunicaAppaltoApi.md#id_appalto_cancella) | **POST** /cancella-appalto | API Rest per l&#x27;eliminazione di un Appalto in lavorazione. SINCRONO
[**id_appalto_conferma**](ComunicaAppaltoApi.md#id_appalto_conferma) | **POST** /conferma-appalto | API Rest per la conferma dei dati di Appalto propedeutica alla generazione dei CIG. ASINCRONO - ASIMMETRICO
[**id_appalto_crea**](ComunicaAppaltoApi.md#id_appalto_crea) | **POST** /crea-appalto | API Rest per la creazione di un Appalto. SINCRONO
[**id_appalto_dettaglio**](ComunicaAppaltoApi.md#id_appalto_dettaglio) | **GET** /consulta-appalto | API Rest per il recupero del dettaglio dell&#x27;Appalto. SINCRONO
[**id_appalto_modifica**](ComunicaAppaltoApi.md#id_appalto_modifica) | **POST** /modifica-appalto | API Rest per la modifica dell&#x27;Appalto. SINCRONO
[**id_appalto_ricerca**](ComunicaAppaltoApi.md#id_appalto_ricerca) | **GET** /ricerca-appalto | API Rest per la ricerca delle Gare-Lotto dell&#x27;Appalto. SINCRONO
[**id_appalto_verifica**](ComunicaAppaltoApi.md#id_appalto_verifica) | **POST** /verifica-appalto | API Rest per la validazione dell&#x27;Appalto. ASINCRONO - ASIMMETRICO
[**id_cig_recupera**](ComunicaAppaltoApi.md#id_cig_recupera) | **GET** /recupera-cig | API Rest per il recupero dei CIG generati da ANAC e assegnati ai lotti dell’Appalto. SINCRONO

# **id_appalto_cancella**
> CancellaAppaltoResponse id_appalto_cancella(body)

API Rest per l'eliminazione di un Appalto in lavorazione. SINCRONO

Eliminazione logica di un Appalto e dei lotti in lavorazione. SINCRONO

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
api_instance = swagger_client.ComunicaAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.CancellaAppaltoRequest() # CancellaAppaltoRequest | 

try:
    # API Rest per l'eliminazione di un Appalto in lavorazione. SINCRONO
    api_response = api_instance.id_appalto_cancella(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaAppaltoApi->id_appalto_cancella: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancellaAppaltoRequest**](CancellaAppaltoRequest.md)|  | 

### Return type

[**CancellaAppaltoResponse**](CancellaAppaltoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_appalto_conferma**
> AckResponse id_appalto_conferma(body)

API Rest per la conferma dei dati di Appalto propedeutica alla generazione dei CIG. ASINCRONO - ASIMMETRICO

Il servizio permette la conferma dei dati dell'Appalto inviati, avvia la fase di validazione e assegnazione dei CIG ed inizializza il Fascicolo Virtuale dell'Appalto. Con la successiva chiamata al servizio esito-operazione è possibile recuperare l'idAvviso per invocare il successivo servizio pubblica-avviso. ASINCRONO - ASIMMETRICO

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
api_instance = swagger_client.ComunicaAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfermaAppaltoRequest() # ConfermaAppaltoRequest | 

try:
    # API Rest per la conferma dei dati di Appalto propedeutica alla generazione dei CIG. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_appalto_conferma(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaAppaltoApi->id_appalto_conferma: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfermaAppaltoRequest**](ConfermaAppaltoRequest.md)|  | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_appalto_crea**
> CreaAppaltoResponse id_appalto_crea(body)

API Rest per la creazione di un Appalto. SINCRONO

Il servizio permette di inviare la scheda per l'inserimento della prima istanza in lavorazione di un Appalto nel formato ESPD-Request, per tutte le tipologie anche affidamento diretto per le pubblicazioni nazionali, nel formato eForm per le pubblicazioni europee in TED, più un formato definito da ANAC con le informazioni aggiuntive. SINCRONO

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
api_instance = swagger_client.ComunicaAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreaAppaltoRequest() # CreaAppaltoRequest | Inserimento Appalto con tutti i dati aggiuntivi

try:
    # API Rest per la creazione di un Appalto. SINCRONO
    api_response = api_instance.id_appalto_crea(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaAppaltoApi->id_appalto_crea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreaAppaltoRequest**](CreaAppaltoRequest.md)| Inserimento Appalto con tutti i dati aggiuntivi | 

### Return type

[**CreaAppaltoResponse**](CreaAppaltoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_appalto_dettaglio**
> ConsultaAppaltoResponse id_appalto_dettaglio(id_appalto=id_appalto, cig=cig)

API Rest per il recupero del dettaglio dell'Appalto. SINCRONO

Servizio per la consultazione delle informazioni di dettaglio di un Appalto e dei relativi Lotti. SINCRONO

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
api_instance = swagger_client.ComunicaAppaltoApi(swagger_client.ApiClient(configuration))
id_appalto = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo univoco dell'Appalto definito da ANAC alternativo al CIG. (A UUID specified by FC4122). (optional)
cig = 'cig_example' # str | Identificativo univoco Gara-Lotto rilasciato da ANAC, alternativo all'idAppalto (optional)

try:
    # API Rest per il recupero del dettaglio dell'Appalto. SINCRONO
    api_response = api_instance.id_appalto_dettaglio(id_appalto=id_appalto, cig=cig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaAppaltoApi->id_appalto_dettaglio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_appalto** | [**str**](.md)| Identificativo univoco dell&#x27;Appalto definito da ANAC alternativo al CIG. (A UUID specified by FC4122). | [optional] 
 **cig** | **str**| Identificativo univoco Gara-Lotto rilasciato da ANAC, alternativo all&#x27;idAppalto | [optional] 

### Return type

[**ConsultaAppaltoResponse**](ConsultaAppaltoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_appalto_modifica**
> ModificaAppaltoResponse id_appalto_modifica(body)

API Rest per la modifica dell'Appalto. SINCRONO

Il servizio permette di inviare la scheda per sostituire la precedente istanza dell’Appalto in lavorazione. L'Appalto è nel formato ESPD-Request, per tutte le tipologie anche affidamento diretto per le pubblicazioni nazionali, nel formato eForm per le pubblicazioni europee in TED, più un formato definito da ANAC con le informazioni aggiuntive. SINCRONO

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
api_instance = swagger_client.ComunicaAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.DatiAppaltoRequest() # DatiAppaltoRequest | Modifica dell'Appalto con tutti i dati aggiuntivi

try:
    # API Rest per la modifica dell'Appalto. SINCRONO
    api_response = api_instance.id_appalto_modifica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaAppaltoApi->id_appalto_modifica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatiAppaltoRequest**](DatiAppaltoRequest.md)| Modifica dell&#x27;Appalto con tutti i dati aggiuntivi | 

### Return type

[**ModificaAppaltoResponse**](ModificaAppaltoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_appalto_ricerca**
> AppaltoListaResponse id_appalto_ricerca(codice_appalto=codice_appalto, cig=cig, lot_identifier=lot_identifier, stato=stato, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, page=page, per_page=per_page)

API Rest per la ricerca delle Gare-Lotto dell'Appalto. SINCRONO

Viene recuperata la lista con i dati di sintesi dell'Appalto e dei rispettivi lotti. Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base agli appalti di competenza dell' RP e della SA per la quale sta operando. Almeno un filtro di ricerca deve essere valorizzato. SINCRONO

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
api_instance = swagger_client.ComunicaAppaltoApi(swagger_client.ApiClient(configuration))
codice_appalto = 'codice_appalto_example' # str | Identificativo univoco dell'appalto definito dalla Stazione Appaltante (optional)
cig = 'cig_example' # str | Identificativo univoco Appalto-Lotto rilasciato da ANAC (optional)
lot_identifier = 'lot_identifier_example' # str | Id univoco del lotto generato dalla stazione appaltante - corrisponde al campo bt-137 - Purpose Lot Identifier del TED - Se valorizzato, il parametro richiedere obbligatoriamente la valorizzazione del codiceAppalto o cig. (optional)
stato = 'stato_example' # str | Codice Stato dell'Appalto - Se valorizzato, il parametro richiedere obbligatoriamente la valorizzazione di almeno un altro parametro - fare riferimento ai valori contenuti nel file [statoAppalto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoAppalto.json) (optional)
data_creazione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione dell'Appalto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_creazione_a = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione dell'Appalto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
page = 1 # int | numero della pagina da visualizzare (optional) (default to 1)
per_page = 20 # int | numero di elementi per pagina (optional) (default to 20)

try:
    # API Rest per la ricerca delle Gare-Lotto dell'Appalto. SINCRONO
    api_response = api_instance.id_appalto_ricerca(codice_appalto=codice_appalto, cig=cig, lot_identifier=lot_identifier, stato=stato, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaAppaltoApi->id_appalto_ricerca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codice_appalto** | **str**| Identificativo univoco dell&#x27;appalto definito dalla Stazione Appaltante | [optional] 
 **cig** | **str**| Identificativo univoco Appalto-Lotto rilasciato da ANAC | [optional] 
 **lot_identifier** | **str**| Id univoco del lotto generato dalla stazione appaltante - corrisponde al campo bt-137 - Purpose Lot Identifier del TED - Se valorizzato, il parametro richiedere obbligatoriamente la valorizzazione del codiceAppalto o cig. | [optional] 
 **stato** | **str**| Codice Stato dell&#x27;Appalto - Se valorizzato, il parametro richiedere obbligatoriamente la valorizzazione di almeno un altro parametro - fare riferimento ai valori contenuti nel file [statoAppalto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoAppalto.json) | [optional] 
 **data_creazione_da** | **datetime**| Data di crezione dell&#x27;Appalto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_creazione_a** | **datetime**| Data di crezione dell&#x27;Appalto - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **page** | **int**| numero della pagina da visualizzare | [optional] [default to 1]
 **per_page** | **int**| numero di elementi per pagina | [optional] [default to 20]

### Return type

[**AppaltoListaResponse**](AppaltoListaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_appalto_verifica**
> AckResponse id_appalto_verifica(body)

API Rest per la validazione dell'Appalto. ASINCRONO - ASIMMETRICO

L'ultima istanza di appalto inviata viene validata. In base alla tipologia dell'appalto viene eseguita una validazione sintattica dei dati di input dell'appalto (eForm, ESPDRequest, anacForm). ASINCRONO - ASIMMETRICO

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
api_instance = swagger_client.ComunicaAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerificaAppaltoRequest() # VerificaAppaltoRequest | 

try:
    # API Rest per la validazione dell'Appalto. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_appalto_verifica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaAppaltoApi->id_appalto_verifica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerificaAppaltoRequest**](VerificaAppaltoRequest.md)|  | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_cig_recupera**
> CigListaResponse id_cig_recupera(id_appalto, page=page, per_page=per_page)

API Rest per il recupero dei CIG generati da ANAC e assegnati ai lotti dell’Appalto. SINCRONO

Per un Appalto il servizio restituiti le coppie Lotto - CIG. SINCRONO

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
api_instance = swagger_client.ComunicaAppaltoApi(swagger_client.ApiClient(configuration))
id_appalto = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo univoco dell'Appalto definito da ANAC
page = 1 # int | numero della pagina da visualizzare (optional) (default to 1)
per_page = 20 # int | numero di elementi per pagina (optional) (default to 20)

try:
    # API Rest per il recupero dei CIG generati da ANAC e assegnati ai lotti dell’Appalto. SINCRONO
    api_response = api_instance.id_cig_recupera(id_appalto, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaAppaltoApi->id_cig_recupera: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_appalto** | [**str**](.md)| Identificativo univoco dell&#x27;Appalto definito da ANAC | 
 **page** | **int**| numero della pagina da visualizzare | [optional] [default to 1]
 **per_page** | **int**| numero di elementi per pagina | [optional] [default to 20]

### Return type

[**CigListaResponse**](CigListaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

