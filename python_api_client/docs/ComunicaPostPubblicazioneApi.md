# swagger_client.ComunicaPostPubblicazioneApi

All URIs are relative to *https://repositorydocument.swagger.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_scheda_cancella**](ComunicaPostPubblicazioneApi.md#id_scheda_cancella) | **POST** /cancella-scheda | API Rest per l&#x27;eliminazione di una specifica Scheda dati in lavorazione nelle fasi successive alla pubblicazione. SINCRONO
[**id_scheda_conferma**](ComunicaPostPubblicazioneApi.md#id_scheda_conferma) | **POST** /conferma-scheda | API Rest per la conferma dei dati inviati per una specifica Scheda. ASINCRONO - ASIMMETRICO
[**id_scheda_crea**](ComunicaPostPubblicazioneApi.md#id_scheda_crea) | **POST** /crea-scheda | API Rest generica per l&#x27;inserimento di una scheda dati per le fasi successive alla pubblicazione. SINCRONO
[**id_scheda_dettaglio**](ComunicaPostPubblicazioneApi.md#id_scheda_dettaglio) | **GET** /consulta-scheda | API Rest per il recupero del dettaglio di una specifica Scheda dati. SINCRONO
[**id_scheda_modifica**](ComunicaPostPubblicazioneApi.md#id_scheda_modifica) | **POST** /modifica-scheda | API Rest generica per la modifica di una scheda dati per le fasi successive alla pubblicazione. SINCRONO
[**id_scheda_ricerca**](ComunicaPostPubblicazioneApi.md#id_scheda_ricerca) | **GET** /ricerca-scheda | API Rest per la ricerca delle Schede dati inserite nelle fasi successive alla pubblicazione. SINCRONO
[**id_scheda_verifica**](ComunicaPostPubblicazioneApi.md#id_scheda_verifica) | **POST** /verifica-scheda | API Rest per la validazione di una Scheda dati. ASINCRONO - ASIMMETRICO

# **id_scheda_cancella**
> CancellaSchedaResponse id_scheda_cancella(body)

API Rest per l'eliminazione di una specifica Scheda dati in lavorazione nelle fasi successive alla pubblicazione. SINCRONO

Eliminazione della Scheda dati in lavorazione. SINCRONO

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
api_instance = swagger_client.ComunicaPostPubblicazioneApi(swagger_client.ApiClient(configuration))
body = swagger_client.CancellaSchedaRequest() # CancellaSchedaRequest | 

try:
    # API Rest per l'eliminazione di una specifica Scheda dati in lavorazione nelle fasi successive alla pubblicazione. SINCRONO
    api_response = api_instance.id_scheda_cancella(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaPostPubblicazioneApi->id_scheda_cancella: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancellaSchedaRequest**](CancellaSchedaRequest.md)|  | 

### Return type

[**CancellaSchedaResponse**](CancellaSchedaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_scheda_conferma**
> AckResponse id_scheda_conferma(body)

API Rest per la conferma dei dati inviati per una specifica Scheda. ASINCRONO - ASIMMETRICO

Il servizio consente di confermare i dati inviati per una specifica Scheda e, qualora il tipo di scheda lo consente, avvia la fase di pubblicazione dell'avviso. Con la successiva chiamata al servizio esito-operazione è possibile recuperare l'idAvviso assegnato. ASINCRONO - ASIMMETRICO

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
api_instance = swagger_client.ComunicaPostPubblicazioneApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfermaSchedaRequest() # ConfermaSchedaRequest | 

try:
    # API Rest per la conferma dei dati inviati per una specifica Scheda. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_scheda_conferma(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaPostPubblicazioneApi->id_scheda_conferma: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfermaSchedaRequest**](ConfermaSchedaRequest.md)|  | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_scheda_crea**
> CreaSchedaResponse id_scheda_crea(body)

API Rest generica per l'inserimento di una scheda dati per le fasi successive alla pubblicazione. SINCRONO

API Rest generica per l'inserimento delle schede dati delle fasi successive alla pubblicazione. A titolo esemplificativo si riportano di seguito alcuni eventi che determinano l'obbligo di invio dati alla PCP:Elenco Partecipanti, Aggiudicazione, Avvio Contratto, Avanzamento Contratto, Conclusione Contratto, Collaudo Contratto, Sospensione, Ripresa Esecuzione, Contratto, Risoluzione Contratto, Modifica Contratto, Subappalto, Recesso, Contenzioso, Accordo Quadro. SINCRONO

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
api_instance = swagger_client.ComunicaPostPubblicazioneApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreaSchedaRequest() # CreaSchedaRequest | Oggetto in ingresso al servizio

try:
    # API Rest generica per l'inserimento di una scheda dati per le fasi successive alla pubblicazione. SINCRONO
    api_response = api_instance.id_scheda_crea(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaPostPubblicazioneApi->id_scheda_crea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreaSchedaRequest**](CreaSchedaRequest.md)| Oggetto in ingresso al servizio | 

### Return type

[**CreaSchedaResponse**](CreaSchedaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_scheda_dettaglio**
> ConsultaSchedaResponse id_scheda_dettaglio(id_scheda)

API Rest per il recupero del dettaglio di una specifica Scheda dati. SINCRONO

Viene recuperato il dettaglio della specifica scheda dati. SINCRONO

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
api_instance = swagger_client.ComunicaPostPubblicazioneApi(swagger_client.ApiClient(configuration))
id_scheda = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo della singola scheda restituita da ANAC nella fase di inserimento

try:
    # API Rest per il recupero del dettaglio di una specifica Scheda dati. SINCRONO
    api_response = api_instance.id_scheda_dettaglio(id_scheda)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaPostPubblicazioneApi->id_scheda_dettaglio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_scheda** | [**str**](.md)| Identificativo della singola scheda restituita da ANAC nella fase di inserimento | 

### Return type

[**ConsultaSchedaResponse**](ConsultaSchedaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_scheda_modifica**
> ModificaSchedaResponse id_scheda_modifica(body)

API Rest generica per la modifica di una scheda dati per le fasi successive alla pubblicazione. SINCRONO

Il servizio sostituisce la precedentemente Scheda in lavorazione. SINCRONO

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
api_instance = swagger_client.ComunicaPostPubblicazioneApi(swagger_client.ApiClient(configuration))
body = swagger_client.DatiSchedaRequest() # DatiSchedaRequest | Oggetto in ingresso al servizio

try:
    # API Rest generica per la modifica di una scheda dati per le fasi successive alla pubblicazione. SINCRONO
    api_response = api_instance.id_scheda_modifica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaPostPubblicazioneApi->id_scheda_modifica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatiSchedaRequest**](DatiSchedaRequest.md)| Oggetto in ingresso al servizio | 

### Return type

[**ModificaSchedaResponse**](ModificaSchedaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_scheda_ricerca**
> SchedaListaResponse id_scheda_ricerca(id_appalto=id_appalto, cig=cig, stato=stato, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, codice_scheda=codice_scheda, stato_scheda=stato_scheda, page=page, per_page=per_page)

API Rest per la ricerca delle Schede dati inserite nelle fasi successive alla pubblicazione. SINCRONO

Viene recuperata la lista con i dati di sintesi delle schede.Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base agli appalti di competenza dell' RP e della SA per la quale sta operando. Almeno un filtro di ricerca deve essere valorizzato. SINCRONO

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
api_instance = swagger_client.ComunicaPostPubblicazioneApi(swagger_client.ApiClient(configuration))
id_appalto = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo univoco dell' Appalto definito da ANAC. (A UUID specified by FC4122). Obbligatorio se cig non è stato valorizzato. (optional)
cig = 'cig_example' # str | Identificativo univoco Gara-Lotto rilasciato da ANAC. Obbligatorio se idAppalto non è stato valorizzato. (optional)
stato = 'stato_example' # str | Codice stato dell'Appalto - fare riferimento ai valori contenuti nel file [statoAppalto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoAppalto.json) (optional)
data_creazione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione dell'Appalto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_creazione_a = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione della Gara - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
codice_scheda = 'codice_scheda_example' # str | Codice Scheda - fare riferimento ai valori contenuti nel file [codiceScheda.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/codiceScheda.json) (optional)
stato_scheda = 'stato_scheda_example' # str | Codice Stato della Scheda - fare riferimento ai valori contenuti nel file [statoScheda.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoScheda.json) (optional)
page = 1 # int | numero della pagina da visualizzare (optional) (default to 1)
per_page = 20 # int | numero di elementi per pagina (optional) (default to 20)

try:
    # API Rest per la ricerca delle Schede dati inserite nelle fasi successive alla pubblicazione. SINCRONO
    api_response = api_instance.id_scheda_ricerca(id_appalto=id_appalto, cig=cig, stato=stato, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, codice_scheda=codice_scheda, stato_scheda=stato_scheda, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaPostPubblicazioneApi->id_scheda_ricerca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_appalto** | [**str**](.md)| Identificativo univoco dell&#x27; Appalto definito da ANAC. (A UUID specified by FC4122). Obbligatorio se cig non è stato valorizzato. | [optional] 
 **cig** | **str**| Identificativo univoco Gara-Lotto rilasciato da ANAC. Obbligatorio se idAppalto non è stato valorizzato. | [optional] 
 **stato** | **str**| Codice stato dell&#x27;Appalto - fare riferimento ai valori contenuti nel file [statoAppalto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoAppalto.json) | [optional] 
 **data_creazione_da** | **datetime**| Data di crezione dell&#x27;Appalto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_creazione_a** | **datetime**| Data di crezione della Gara - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **codice_scheda** | **str**| Codice Scheda - fare riferimento ai valori contenuti nel file [codiceScheda.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/codiceScheda.json) | [optional] 
 **stato_scheda** | **str**| Codice Stato della Scheda - fare riferimento ai valori contenuti nel file [statoScheda.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoScheda.json) | [optional] 
 **page** | **int**| numero della pagina da visualizzare | [optional] [default to 1]
 **per_page** | **int**| numero di elementi per pagina | [optional] [default to 20]

### Return type

[**SchedaListaResponse**](SchedaListaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_scheda_verifica**
> AckResponse id_scheda_verifica(body)

API Rest per la validazione di una Scheda dati. ASINCRONO - ASIMMETRICO

L'ultimo istanza della Scheda inviata viene validata. La validazione è orchestrata da un Workflow Engine che, tramite il suo motore di regole, verifica sia se la scheda dati è coerente con lo stato dell’Appalto sia la correttezza sintattica dei dati di input.  ASINCRONO - ASIMMETRICO

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
api_instance = swagger_client.ComunicaPostPubblicazioneApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerificaSchedaRequest() # VerificaSchedaRequest | 

try:
    # API Rest per la validazione di una Scheda dati. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_scheda_verifica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComunicaPostPubblicazioneApi->id_scheda_verifica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerificaSchedaRequest**](VerificaSchedaRequest.md)|  | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

