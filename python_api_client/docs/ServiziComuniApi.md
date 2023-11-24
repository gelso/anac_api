# swagger_client.ServiziComuniApi

All URIs are relative to *https://repositorydocument.swagger.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_appalto_stato**](ServiziComuniApi.md#id_appalto_stato) | **GET** /stato-appalto | API Rest per il recupero dello stato dell&#x27;Appalto, del Lotto o del Contratto. SINCRONO
[**id_operazione_esito**](ServiziComuniApi.md#id_operazione_esito) | **GET** /esito-operazione | API Rest per il recupero dell&#x27;esito dell&#x27;operazione. SINCRONO

# **id_appalto_stato**
> StatoResponse id_appalto_stato(id_appalto=id_appalto, cig=cig, id_contratto=id_contratto)

API Rest per il recupero dello stato dell'Appalto, del Lotto o del Contratto. SINCRONO

Servizio per il recupero dello stato in cui si trova l’Appalto, il Lotto o il Contratto. Il compito dispositivo di aggiornare lo stato proveniente dai sistemi esterni, TED e/o PPL-ANAC, sarà in carico ad un task schedulato PCP. Pertanto il recupero dello stato da parte del servizio insiste su uno stato PCP che restituisce anche la data in cui il task schedulato ha effettuato il controllo sui sistemi esterni. SINCRONO

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
api_instance = swagger_client.ServiziComuniApi(swagger_client.ApiClient(configuration))
id_appalto = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo univoco dell'Appalto definito da ANAC. Alternativo agli altri parametri di input. (optional)
cig = 'cig_example' # str | Identificativo univoco Gara-Lotto rilasciato da ANAC. Alternativo agli altri parametri di input. (optional)
id_contratto = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identificativo univoco del Contratto definito da ANAC. Alternativo agli altri parametri di input. (optional)

try:
    # API Rest per il recupero dello stato dell'Appalto, del Lotto o del Contratto. SINCRONO
    api_response = api_instance.id_appalto_stato(id_appalto=id_appalto, cig=cig, id_contratto=id_contratto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiziComuniApi->id_appalto_stato: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_appalto** | [**str**](.md)| Identificativo univoco dell&#x27;Appalto definito da ANAC. Alternativo agli altri parametri di input. | [optional] 
 **cig** | **str**| Identificativo univoco Gara-Lotto rilasciato da ANAC. Alternativo agli altri parametri di input. | [optional] 
 **id_contratto** | [**str**](.md)| Identificativo univoco del Contratto definito da ANAC. Alternativo agli altri parametri di input. | [optional] 

### Return type

[**StatoResponse**](StatoResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_operazione_esito**
> EsitoOperazioneListaResponse id_operazione_esito(id_appalto, tipo_operazione, tipo_ricerca, esito=esito)

API Rest per il recupero dell'esito dell'operazione. SINCRONO

Il compito dispositivo di aggiornare l'esito delle operazioni provenienti dai sistemi esterni, TED e/o PPL-ANAC, sarà in carico ad un task schedulato PCP. Pertanto il recupero dell'esito operazione da parte del servizio insiste su uno stato dell'esito PCP che restituisce anche la data in cui il task schedulato ha effettuato il controllo sui sistemi esterni. SINCRONO

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
api_instance = swagger_client.ServiziComuniApi(swagger_client.ApiClient(configuration))
id_appalto = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | identificativo univoco dell'Appalto definito da ANAC. (A UUID specified by RFC4122)
tipo_operazione = 'tipo_operazione_example' # str | Tipo operazione di cui si vuole conoscere l'esito - fare riferimento ai valori contenuti nel file [tipoOperazione.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoOperazione.json)
tipo_ricerca = 'tipo_ricerca_example' # str | Codice Tipo di ricerca da eseguire - fare riferimento ai valori contenuti nel file [tipoRicercaOperazione.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoRicercaOperazione.json)
esito = 'esito_example' # str | Codice sintetico esito operazione - fare riferimento ai valori contenuti nel file [esito.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/esito.json) (optional)

try:
    # API Rest per il recupero dell'esito dell'operazione. SINCRONO
    api_response = api_instance.id_operazione_esito(id_appalto, tipo_operazione, tipo_ricerca, esito=esito)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiziComuniApi->id_operazione_esito: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_appalto** | [**str**](.md)| identificativo univoco dell&#x27;Appalto definito da ANAC. (A UUID specified by RFC4122) | 
 **tipo_operazione** | **str**| Tipo operazione di cui si vuole conoscere l&#x27;esito - fare riferimento ai valori contenuti nel file [tipoOperazione.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoOperazione.json) | 
 **tipo_ricerca** | **str**| Codice Tipo di ricerca da eseguire - fare riferimento ai valori contenuti nel file [tipoRicercaOperazione.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/tipoRicercaOperazione.json) | 
 **esito** | **str**| Codice sintetico esito operazione - fare riferimento ai valori contenuti nel file [esito.json](https://raw.githubusercontent.com/anticorruzione/npa/main/docs/modello-dati/tipologiche/esito.json) | [optional] 

### Return type

[**EsitoOperazioneListaResponse**](EsitoOperazioneListaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

