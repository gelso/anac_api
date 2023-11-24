# swagger_client.CodeListApi

All URIs are relative to *https://repositorydocument.swagger.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_recupera_elenco_tipologiche**](CodeListApi.md#id_recupera_elenco_tipologiche) | **GET** /recupera-elenco-tipologiche | API Rest per il recupero dell&#x27;elenco delle tipologiche disponibili. SINCRONO
[**id_recupera_item_tipologica**](CodeListApi.md#id_recupera_item_tipologica) | **GET** /recupera-valore-tipologica | API Rest per il recupero di un singolo item di una tipologica. SINCRONO
[**id_recupera_tipologica**](CodeListApi.md#id_recupera_tipologica) | **GET** /recupera-tipologica | API Rest per il recupero di una specifica tipologica. SINCRONO

# **id_recupera_elenco_tipologiche**
> TipologicaListaResponse id_recupera_elenco_tipologiche(page=page, per_page=per_page)

API Rest per il recupero dell'elenco delle tipologiche disponibili. SINCRONO

Il servizio restituiti un'elenco delle tipologiche disponibili. SINCRONO

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
api_instance = swagger_client.CodeListApi(swagger_client.ApiClient(configuration))
page = 1 # int | numero della pagina da visualizzare (optional) (default to 1)
per_page = 20 # int | numero di elementi per pagina (optional) (default to 20)

try:
    # API Rest per il recupero dell'elenco delle tipologiche disponibili. SINCRONO
    api_response = api_instance.id_recupera_elenco_tipologiche(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeListApi->id_recupera_elenco_tipologiche: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| numero della pagina da visualizzare | [optional] [default to 1]
 **per_page** | **int**| numero di elementi per pagina | [optional] [default to 20]

### Return type

[**TipologicaListaResponse**](TipologicaListaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_recupera_item_tipologica**
> TipologicaItemResponse id_recupera_item_tipologica(id_tipologica, codice)

API Rest per il recupero di un singolo item di una tipologica. SINCRONO

Il servizio restituiti il valore di un singolo item che si vuole recuperare dalla tipologica. SINCRONO

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
api_instance = swagger_client.CodeListApi(swagger_client.ApiClient(configuration))
id_tipologica = 'id_tipologica_example' # str | Identificativo della tipologica
codice = 'codice_example' # str | Codice del valore che si vuole recuperare dalla tipologica

try:
    # API Rest per il recupero di un singolo item di una tipologica. SINCRONO
    api_response = api_instance.id_recupera_item_tipologica(id_tipologica, codice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeListApi->id_recupera_item_tipologica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_tipologica** | **str**| Identificativo della tipologica | 
 **codice** | **str**| Codice del valore che si vuole recuperare dalla tipologica | 

### Return type

[**TipologicaItemResponse**](TipologicaItemResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_recupera_tipologica**
> TipologicaResponse id_recupera_tipologica(id_tipologica, data_inizio=data_inizio, data_fine=data_fine, page=page, per_page=per_page)

API Rest per il recupero di una specifica tipologica. SINCRONO

Il servizio restituiti l'elenco di una singola tipologica. SINCRONO

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
api_instance = swagger_client.CodeListApi(swagger_client.ApiClient(configuration))
id_tipologica = 'id_tipologica_example' # str | Identificativo della tipologica
data_inizio = '2013-10-20T19:20:30+01:00' # datetime | Data di inizio (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
data_fine = '2013-10-20T19:20:30+01:00' # datetime | Data di fine (A date-time specified by ISO 8601 as profiled by RFC 3339) (optional)
page = 1 # int | numero della pagina da visualizzare (optional) (default to 1)
per_page = 20 # int | numero di elementi per pagina (optional) (default to 20)

try:
    # API Rest per il recupero di una specifica tipologica. SINCRONO
    api_response = api_instance.id_recupera_tipologica(id_tipologica, data_inizio=data_inizio, data_fine=data_fine, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeListApi->id_recupera_tipologica: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_tipologica** | **str**| Identificativo della tipologica | 
 **data_inizio** | **datetime**| Data di inizio (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **data_fine** | **datetime**| Data di fine (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
 **page** | **int**| numero della pagina da visualizzare | [optional] [default to 1]
 **per_page** | **int**| numero di elementi per pagina | [optional] [default to 20]

### Return type

[**TipologicaResponse**](TipologicaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

