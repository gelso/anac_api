# AvanzamentoType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione_avanzamento** | **str** | Denominazione dello stato di avanzamento | 
**modalita_pagamento** | [**ModalitaPagamentoEnum**](ModalitaPagamentoEnum.md) |  | 
**imp_anticipazione** | **float** | Eventuale anticipazione | [optional] 
**data_certificato_anticipazione** | **datetime** | Data del certificato di pagamento relativo all&#x27;anticipazione | [optional] 
**data_avanzamento** | **datetime** | Data Stato di avanzamento | 
**imp_sal** | **float** | Importo stato avanzamento progressivo (cumulato) | 
**data_certificato_mandato_pagamento** | **datetime** | Data di emissione del certificato/mandato di pagamento. Per lavori, indicare la data del certificato. Per servizi e forniture, indicare la data del mandato | [optional] 
**imp_certificato_mandato_pagamento** | **float** | Importo del certificato/mandato di pagamento. Per lavori, indicare l’importo del certificato. Per servizi e forniture, indicare l’importo del mandato | [optional] 
**avanzamento** | [**AvanzamentoEnum**](AvanzamentoEnum.md) |  | 
**num_giorni_scostamento** | **float** | Indicare lo scostamento registrato in numero di giorni | [optional] 
**num_giorni_proroga** | **float** | Indicare il numero di giorni di proroga concessi (non conseguenti a modifiche contrattuali) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

