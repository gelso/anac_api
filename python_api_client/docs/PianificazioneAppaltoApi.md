# swagger_client.PianificazioneAppaltoApi

All URIs are relative to *https://repositorydocument.swagger.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_piano_cancella**](PianificazioneAppaltoApi.md#id_piano_cancella) | **POST** /cancella-piano | API Rest per l&#x27;eliminazione di una Pianificazione in lavorazione. SINCRONO
[**id_piano_conferma**](PianificazioneAppaltoApi.md#id_piano_conferma) | **POST** /conferma-piano | API Rest per la conferma dei dati inviati per una specifica Pianificazione. ASINCRONO - ASIMMETRICO
[**id_piano_crea**](PianificazioneAppaltoApi.md#id_piano_crea) | **POST** /crea-piano | API Rest per la creazione della Pianificazione. SINCRONO
[**id_piano_dettaglio**](PianificazioneAppaltoApi.md#id_piano_dettaglio) | **GET** /consulta-piano | API Rest per il recupero del dettaglio della Pianificazione. SINCRONO
[**id_piano_modifica**](PianificazioneAppaltoApi.md#id_piano_modifica) | **POST** /modifica-piano | API Rest per la modifica della Pianificazione. SINCRONO
[**id_piano_ricerca**](PianificazioneAppaltoApi.md#id_piano_ricerca) | **GET** /ricerca-piano | API Rest per la ricerca delle Pianificazioni. SINCRONO
[**id_piano_verifica**](PianificazioneAppaltoApi.md#id_piano_verifica) | **POST** /verifica-piano | API Rest per la validazione della Pianificazione. ASINCRONO - ASIMMETRICO

# **id_piano_cancella**
> CancellaPianoResponse id_piano_cancella(body)

API Rest per l'eliminazione di una Pianificazione in lavorazione. SINCRONO

Eliminazione della Pianificazione in lavorazione. SINCRONO

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
api_instance = swagger_client.PianificazioneAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.CancellaPianoRequest() # CancellaPianoRequest | 

try:
    # API Rest per l'eliminazione di una Pianificazione in lavorazione. SINCRONO
    api_response = api_instance.id_piano_cancella(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PianificazioneAppaltoApi->id_piano_cancella: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancellaPianoRequest**](CancellaPianoRequest.md)|  | 

### Return type

[**CancellaPianoResponse**](CancellaPianoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_piano_conferma**
> AckResponse id_piano_conferma(body)

API Rest per la conferma dei dati inviati per una specifica Pianificazione. ASINCRONO - ASIMMETRICO

Il servizio consente di confermare i dati inviati per una specifica Pianificazione e, qualora il tipo di scheda lo consente, avvia la fase di pubblicazione dell'avviso. Con la successiva chiamata al servizio esito-operazione è possibile recuperare l'idAvviso assegnato. ASINCRONO - ASIMMETRICO

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
api_instance = swagger_client.PianificazioneAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfermaPianoRequest() # ConfermaPianoRequest | 

try:
    # API Rest per la conferma dei dati inviati per una specifica Pianificazione. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_piano_conferma(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PianificazioneAppaltoApi->id_piano_conferma: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfermaPianoRequest**](ConfermaPianoRequest.md)|  | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_piano_crea**
> CreaPianoResponse id_piano_crea(body)

API Rest per la creazione della Pianificazione. SINCRONO

Il servizio permette di inviare la scheda per l'inserimento della Pianificazione nel formato definito da Anac e dell'eventuale avviso di pre-informazione in TED nel formato eForm. SINCRONO

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
api_instance = swagger_client.PianificazioneAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreaPianoRequest() # CreaPianoRequest | Inserimento piano con tutti i dati aggiuntivi

try:
    # API Rest per la creazione della Pianificazione. SINCRONO
    api_response = api_instance.id_piano_crea(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PianificazioneAppaltoApi->id_piano_crea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreaPianoRequest**](CreaPianoRequest.md)| Inserimento piano con tutti i dati aggiuntivi | 

### Return type

[**CreaPianoResponse**](CreaPianoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_piano_dettaglio**
> ConsultaPianoResponse id_piano_dettaglio(id_pianificazione)

API Rest per il recupero del dettaglio della Pianificazione. SINCRONO

API Rest per il recupero del dettaglio della Pianificazione. SINCRONO

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
api_instance = swagger_client.PianificazioneAppaltoApi(swagger_client.ApiClient(configuration))
id_pianificazione = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | identificativo univoco della Pianificazione definito da ANAC. (A UUID specified by RFC4122)

try:
    # API Rest per il recupero del dettaglio della Pianificazione. SINCRONO
    api_response = api_instance.id_piano_dettaglio(id_pianificazione)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PianificazioneAppaltoApi->id_piano_dettaglio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_pianificazione** | [**str**](.md)| identificativo univoco della Pianificazione definito da ANAC. (A UUID specified by RFC4122) | 

### Return type

[**ConsultaPianoResponse**](ConsultaPianoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_piano_modifica**
> ModificaPianoResponse id_piano_modifica(body)

API Rest per la modifica della Pianificazione. SINCRONO

Il servizio permette di inviare la scheda per sostituire la precedentemente Pianificazione in lavorazione. SINCRONO

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
api_instance = swagger_client.PianificazioneAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.DatiPianoRequest() # DatiPianoRequest | Oggetto generico in ingresso al servizio

try:
    # API Rest per la modifica della Pianificazione. SINCRONO
    api_response = api_instance.id_piano_modifica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PianificazioneAppaltoApi->id_piano_modifica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatiPianoRequest**](DatiPianoRequest.md)| Oggetto generico in ingresso al servizio | 

### Return type

[**ModificaPianoResponse**](ModificaPianoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_piano_ricerca**
> PianoListaResponse id_piano_ricerca(stato=stato, tipo=tipo, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, page=page, per_page=per_page)

API Rest per la ricerca delle Pianificazioni. SINCRONO

Viene recuperata la lista con i dati di sintesi delle Pianificazioni.Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base alla competenza della SA che sta operando. Almeno un filtro di ricerca deve essere valorizzato. SINCRONO

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
api_instance = swagger_client.PianificazioneAppaltoApi(swagger_client.ApiClient(configuration))
stato = 'stato_example' # str | Codice stato della Pianificazione - se valorizzato, il parametro richiedere obbligatoriamente la valorizzazione di almeno un altro parametro -  fare riferimento ai valori contenuti nel file [statoPiano.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoPiano.json) (optional)
tipo = 'tipo_example' # str | Codice tipologia della Pianificazione - fare riferimento ai valori contenuti nel file [tipoPiano.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoPiano.json) (optional)
data_creazione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione della Pianificazione - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_creazione_a = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione della Pianificazione - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
page = 1 # int | numero della pagina da visualizzare (optional) (default to 1)
per_page = 20 # int | numero di elementi per pagina (optional) (default to 20)

try:
    # API Rest per la ricerca delle Pianificazioni. SINCRONO
    api_response = api_instance.id_piano_ricerca(stato=stato, tipo=tipo, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PianificazioneAppaltoApi->id_piano_ricerca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stato** | **str**| Codice stato della Pianificazione - se valorizzato, il parametro richiedere obbligatoriamente la valorizzazione di almeno un altro parametro -  fare riferimento ai valori contenuti nel file [statoPiano.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoPiano.json) | [optional] 
 **tipo** | **str**| Codice tipologia della Pianificazione - fare riferimento ai valori contenuti nel file [tipoPiano.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoPiano.json) | [optional] 
 **data_creazione_da** | **datetime**| Data di crezione della Pianificazione - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_creazione_a** | **datetime**| Data di crezione della Pianificazione - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **page** | **int**| numero della pagina da visualizzare | [optional] [default to 1]
 **per_page** | **int**| numero di elementi per pagina | [optional] [default to 20]

### Return type

[**PianoListaResponse**](PianoListaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_piano_verifica**
> AckResponse id_piano_verifica(body)

API Rest per la validazione della Pianificazione. ASINCRONO - ASIMMETRICO

L'ultima istanza della Pianificazione inviata viene validata. In base alla tipologia della Pianificazione viene eseguita una validazione sintattica dei dati di input. ASINCRONO - ASIMMETRICO

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
api_instance = swagger_client.PianificazioneAppaltoApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerificaPianoRequest() # VerificaPianoRequest | 

try:
    # API Rest per la validazione della Pianificazione. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_piano_verifica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PianificazioneAppaltoApi->id_piano_verifica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerificaPianoRequest**](VerificaPianoRequest.md)|  | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

