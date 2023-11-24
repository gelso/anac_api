# swagger_client.PubblicaAvvisoApi

All URIs are relative to *https://repositorydocument.swagger.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_avviso_anteprima**](PubblicaAvvisoApi.md#id_avviso_anteprima) | **GET** /consulta-rendering-avviso | API Rest per il recupero del PDF di un Avviso. SINCRONO
[**id_avviso_cancella**](PubblicaAvvisoApi.md#id_avviso_cancella) | **POST** /cancella-avviso | API Rest per la richiesta di annullamento di pubblicazione di un avviso non ancora pubblicato. ASINCRONO - ASIMMETRICO
[**id_avviso_dettaglio**](PubblicaAvvisoApi.md#id_avviso_dettaglio) | **GET** /consulta-avviso | API Rest per il recupero del dettaglio di un Avviso. SINCRONO
[**id_avviso_modifica**](PubblicaAvvisoApi.md#id_avviso_modifica) | **POST** /modifica-avviso | API Rest per la creazione di un avviso che sostituisce il precedente non ancora pubblicato sia a livello nazionale e sia europeo. ASINCRONO - ASIMMETRICO
[**id_avviso_pubblica**](PubblicaAvvisoApi.md#id_avviso_pubblica) | **POST** /pubblica-avviso | API Rest per la richiesta di pubblicazione di un&#x27;avviso sia a livello nazionale sia europeo. ASINCRONO - ASIMMETRICO
[**id_avviso_rettifica**](PubblicaAvvisoApi.md#id_avviso_rettifica) | **POST** /rettifica-avviso | API Rest per la creazione di un avviso che rettifica il precedente pubblicato sia a livello nazionale e sia europeo. ASINCRONO - ASIMMETRICO
[**id_avviso_ricerca**](PubblicaAvvisoApi.md#id_avviso_ricerca) | **GET** /ricerca-avviso | API Rest per la ricerca degli avvisi dell&#x27;appalto. SINCRONO
[**id_avviso_stato**](PubblicaAvvisoApi.md#id_avviso_stato) | **GET** /stato-avviso | API Rest per il recupero dello stato dell&#x27;Avviso. SINCRONO

# **id_avviso_anteprima**
> RenderingAvvisoResponse id_avviso_anteprima(id_avviso)

API Rest per il recupero del PDF di un Avviso. SINCRONO

Viene resituito il file in foramto PDF relativo all' Avviso.

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
api_instance = swagger_client.PubblicaAvvisoApi(swagger_client.ApiClient(configuration))
id_avviso = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo dell'Avviso generato da ANAC.

try:
    # API Rest per il recupero del PDF di un Avviso. SINCRONO
    api_response = api_instance.id_avviso_anteprima(id_avviso)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubblicaAvvisoApi->id_avviso_anteprima: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_avviso** | [**str**](.md)| Identificativo dell&#x27;Avviso generato da ANAC. | 

### Return type

[**RenderingAvvisoResponse**](RenderingAvvisoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_avviso_cancella**
> AckResponse id_avviso_cancella(body)

API Rest per la richiesta di annullamento di pubblicazione di un avviso non ancora pubblicato. ASINCRONO - ASIMMETRICO

Il servizio permette di sospensione una una richiesta di pubblicazione, sia nazionale sia europea, di un avviso non ancora pubblicato. ASINCRONO ASIMMETRICO

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
api_instance = swagger_client.PubblicaAvvisoApi(swagger_client.ApiClient(configuration))
body = swagger_client.CancellaAvvisoRequest() # CancellaAvvisoRequest | 

try:
    # API Rest per la richiesta di annullamento di pubblicazione di un avviso non ancora pubblicato. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_avviso_cancella(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubblicaAvvisoApi->id_avviso_cancella: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancellaAvvisoRequest**](CancellaAvvisoRequest.md)|  | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_avviso_dettaglio**
> ConsultaAvvisoResponse id_avviso_dettaglio(id_avviso)

API Rest per il recupero del dettaglio di un Avviso. SINCRONO

Viene resituita la definizione di un Avviso con tutte le sue informazioni di dettaglio.

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
api_instance = swagger_client.PubblicaAvvisoApi(swagger_client.ApiClient(configuration))
id_avviso = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo dell'Avviso generato da ANAC.

try:
    # API Rest per il recupero del dettaglio di un Avviso. SINCRONO
    api_response = api_instance.id_avviso_dettaglio(id_avviso)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubblicaAvvisoApi->id_avviso_dettaglio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_avviso** | [**str**](.md)| Identificativo dell&#x27;Avviso generato da ANAC. | 

### Return type

[**ConsultaAvvisoResponse**](ConsultaAvvisoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_avviso_modifica**
> AckResponse id_avviso_modifica(body)

API Rest per la creazione di un avviso che sostituisce il precedente non ancora pubblicato sia a livello nazionale e sia europeo. ASINCRONO - ASIMMETRICO

API Rest per la richiesta di pubblicazione di un'avviso sia a livello nazionale sia europeo. L'avviso sostituisce il precedente non ancora pubblicato. Il servizio gestisce la pubblicazione europea mediante l'acquisizione di dati nel formato definito da TED (eForm) e, la pubblicazione nazionale mediante l'acquisizione di dati definiti dall'ESPD Request più dati aggiuntivi richiesti da ANAC. Con la successiva chiamata al servizio esito-operazione è possibile recuperare l'idAvviso di modifica assegnato. ASINCRONO ASIMMETRICO

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
api_instance = swagger_client.PubblicaAvvisoApi(swagger_client.ApiClient(configuration))
body = swagger_client.AvvisoRequest() # AvvisoRequest | Inserimento Avviso con gli oggetti specifici per la pubblicazione in TED o in ambito Nazionale

try:
    # API Rest per la creazione di un avviso che sostituisce il precedente non ancora pubblicato sia a livello nazionale e sia europeo. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_avviso_modifica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubblicaAvvisoApi->id_avviso_modifica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AvvisoRequest**](AvvisoRequest.md)| Inserimento Avviso con gli oggetti specifici per la pubblicazione in TED o in ambito Nazionale | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_avviso_pubblica**
> AckResponse id_avviso_pubblica(body)

API Rest per la richiesta di pubblicazione di un'avviso sia a livello nazionale sia europeo. ASINCRONO - ASIMMETRICO

Il servizio avvia la richiesta di pubblicazione di un Avviso, a livello nazionale e/o europeo. A seguito della chiamata a questo servizio, l’avviso transita in stato “IN ATTESA PUBBLICAZIONE”. ASINCRONO - ASIMMETRICO

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
api_instance = swagger_client.PubblicaAvvisoApi(swagger_client.ApiClient(configuration))
body = swagger_client.PubblicaAvvisoRequest() # PubblicaAvvisoRequest | 

try:
    # API Rest per la richiesta di pubblicazione di un'avviso sia a livello nazionale sia europeo. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_avviso_pubblica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubblicaAvvisoApi->id_avviso_pubblica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PubblicaAvvisoRequest**](PubblicaAvvisoRequest.md)|  | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_avviso_rettifica**
> AckResponse id_avviso_rettifica(body)

API Rest per la creazione di un avviso che rettifica il precedente pubblicato sia a livello nazionale e sia europeo. ASINCRONO - ASIMMETRICO

API Rest per la richiesta di pubblicazione di un'avviso di rettifica sia a livello nazionale sia europeo. L'avviso rettifica il precedente già pubblicato. Il servizio gestisce la pubblicazione europea mediante l'acquisizione di dati nel formato definito da TED (eForm) e, la pubblicazione nazionale mediante l'acquisizione di dati definiti dall'ESPD Request più dati aggiuntivi richiesti da ANAC. Con la successiva chiamata al servizio esito-operazione è possibile recuperare l'idAvviso di rettifica assegnato. ASINCRONO ASIMMETRICO

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
api_instance = swagger_client.PubblicaAvvisoApi(swagger_client.ApiClient(configuration))
body = swagger_client.AvvisoRequest() # AvvisoRequest | Inserimento Avviso con gli oggetti specifici per la pubblicazione in TED o in ambito Nazionale

try:
    # API Rest per la creazione di un avviso che rettifica il precedente pubblicato sia a livello nazionale e sia europeo. ASINCRONO - ASIMMETRICO
    api_response = api_instance.id_avviso_rettifica(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubblicaAvvisoApi->id_avviso_rettifica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AvvisoRequest**](AvvisoRequest.md)| Inserimento Avviso con gli oggetti specifici per la pubblicazione in TED o in ambito Nazionale | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_avviso_ricerca**
> AvvisoListaResponse id_avviso_ricerca(codice_appalto=codice_appalto, id_appalto=id_appalto, cig=cig, stato=stato, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, stato_avviso=stato_avviso, tipo_avviso=tipo_avviso, azione_avviso=azione_avviso, data_creazione_avviso_da=data_creazione_avviso_da, data_creazione_avviso_a=data_creazione_avviso_a, page=page, per_page=per_page)

API Rest per la ricerca degli avvisi dell'appalto. SINCRONO

Viene recuperata la lista con i dati di sintesi degli Avvisi. Le informazioni restituite dal servizio saranno filtrate, oltre in base ai parametri di ricerca, anche in base agli appalti di competenza dell' RP e della SA per la quale sta operando. Almeno un filtro di ricerca deve essere valorizzato. SINCRONO

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
api_instance = swagger_client.PubblicaAvvisoApi(swagger_client.ApiClient(configuration))
codice_appalto = 'codice_appalto_example' # str | Identificativo univoco dell'appalto definito dalla Stazione Appaltante. Obbligatorio se idAppalto e cig non sono stati valorizzati. (optional)
id_appalto = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo univoco dell' Appalto definito da ANAC. (A UUID specified by FC4122). Obbligatorio se codiceAppalto e cig non sono stati valorizzati. (optional)
cig = 'cig_example' # str | Identificativo univoco Gara-Lotto rilasciato da ANAC. Obbligatorio se idAppalto e cig non sono stati valorizzati. (optional)
stato = 'stato_example' # str | Codice Stato dell'Appalto - fare riferimento ai valori contenuti nel file [statoAppalto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoAppalto.json) (optional)
data_creazione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione dell'Appalto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_creazione_a = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione della Appalto - intervallo precedente (A date-time specified by RF333) (optional)
stato_avviso = 'stato_avviso_example' # str | Codice Stato in cui si trova l' Avviso - fare riferimento ai valori contenuti nel file [statoAvviso.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoAvviso.json) (optional)
tipo_avviso = 'tipo_avviso_example' # str | Codice Tipo di avviso - fare riferimento ai valori contenuti nel file [tipoAvviso.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoAvviso.json) (optional)
azione_avviso = 'azione_avviso_example' # str | Codice Tipo di azione dell'avviso - fare riferimento ai valori contenuti nel file [tipoAzioneAvviso.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoAzioneAvviso.json) (optional)
data_creazione_avviso_da = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione dell'Avviso - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_creazione_avviso_a = '2013-10-20T19:20:30+01:00' # datetime | Data di crezione della Avviso - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
page = 1 # int | numero della pagina da visualizzare (optional) (default to 1)
per_page = 20 # int | numero di elementi per pagina (optional) (default to 20)

try:
    # API Rest per la ricerca degli avvisi dell'appalto. SINCRONO
    api_response = api_instance.id_avviso_ricerca(codice_appalto=codice_appalto, id_appalto=id_appalto, cig=cig, stato=stato, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, stato_avviso=stato_avviso, tipo_avviso=tipo_avviso, azione_avviso=azione_avviso, data_creazione_avviso_da=data_creazione_avviso_da, data_creazione_avviso_a=data_creazione_avviso_a, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubblicaAvvisoApi->id_avviso_ricerca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codice_appalto** | **str**| Identificativo univoco dell&#x27;appalto definito dalla Stazione Appaltante. Obbligatorio se idAppalto e cig non sono stati valorizzati. | [optional] 
 **id_appalto** | [**str**](.md)| Identificativo univoco dell&#x27; Appalto definito da ANAC. (A UUID specified by FC4122). Obbligatorio se codiceAppalto e cig non sono stati valorizzati. | [optional] 
 **cig** | **str**| Identificativo univoco Gara-Lotto rilasciato da ANAC. Obbligatorio se idAppalto e cig non sono stati valorizzati. | [optional] 
 **stato** | **str**| Codice Stato dell&#x27;Appalto - fare riferimento ai valori contenuti nel file [statoAppalto.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoAppalto.json) | [optional] 
 **data_creazione_da** | **datetime**| Data di crezione dell&#x27;Appalto - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_creazione_a** | **datetime**| Data di crezione della Appalto - intervallo precedente (A date-time specified by RF333) | [optional] 
 **stato_avviso** | **str**| Codice Stato in cui si trova l&#x27; Avviso - fare riferimento ai valori contenuti nel file [statoAvviso.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/statoAvviso.json) | [optional] 
 **tipo_avviso** | **str**| Codice Tipo di avviso - fare riferimento ai valori contenuti nel file [tipoAvviso.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoAvviso.json) | [optional] 
 **azione_avviso** | **str**| Codice Tipo di azione dell&#x27;avviso - fare riferimento ai valori contenuti nel file [tipoAzioneAvviso.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoAzioneAvviso.json) | [optional] 
 **data_creazione_avviso_da** | **datetime**| Data di crezione dell&#x27;Avviso - intervallo successivo (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_creazione_avviso_a** | **datetime**| Data di crezione della Avviso - intervallo precedente (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **page** | **int**| numero della pagina da visualizzare | [optional] [default to 1]
 **per_page** | **int**| numero di elementi per pagina | [optional] [default to 20]

### Return type

[**AvvisoListaResponse**](AvvisoListaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_avviso_stato**
> StatoAvvisoResponse id_avviso_stato(id_avviso)

API Rest per il recupero dello stato dell'Avviso. SINCRONO

Il compito dispositivo di aggiornare lo stato dell'avviso proveniente dai sistemi esterni, TED e/o PPL-ANAC, sarà in carico ad un task schedulato PCP. Pertanto il recupero dello stato da parte del servizio insiste su uno stato avviso PCP che restituisce anche la data in cui il task schedulato ha effettuato il controllo sui sistemi esterni. SINCRONO

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
api_instance = swagger_client.PubblicaAvvisoApi(swagger_client.ApiClient(configuration))
id_avviso = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo dell'Avviso generato da ANAC.

try:
    # API Rest per il recupero dello stato dell'Avviso. SINCRONO
    api_response = api_instance.id_avviso_stato(id_avviso)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubblicaAvvisoApi->id_avviso_stato: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_avviso** | [**str**](.md)| Identificativo dell&#x27;Avviso generato da ANAC. | 

### Return type

[**StatoAvvisoResponse**](StatoAvvisoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

