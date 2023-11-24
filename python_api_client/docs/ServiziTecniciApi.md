# swagger_client.ServiziTecniciApi

All URIs are relative to *https://repositorydocument.swagger.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_status_show**](ServiziTecniciApi.md#id_status_show) | **GET** /status | Ritorna lo stato dell&#x27;applicazione. SINCRONO

# **id_status_show**
> BaseResponse id_status_show()

Ritorna lo stato dell'applicazione. SINCRONO

Ritorna lo stato dell'applicazione. A scopo di test, su base randomica puo' ritornare un errore. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiziTecniciApi()

try:
    # Ritorna lo stato dell'applicazione. SINCRONO
    api_response = api_instance.id_status_show()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiziTecniciApi->id_status_show: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

