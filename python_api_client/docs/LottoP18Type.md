# LottoP18Type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lot_identifier** | **str** | Id univoco del lotto generato dalla stazione appaltante - corrisponde al campo bt-137 - Purpose Lot Identifier del TED | 
**ipotesi_collegamento** | [**IpotesiCollegamentoType**](IpotesiCollegamentoType.md) |  | [optional] 
**categoria** | [**CategoriaEnum**](CategoriaEnum.md) |  | 
**acquisizione_cup** | **bool** | Il contratto è finalizzato alla realizzazione di progetti d&#x27;investimento pubblico per i quali è prevista l&#x27;acquisizione del codice CUP ai sensi dell&#x27;art. 11 L. 3/2003 e ss.mm.? (E&#x27; necessario acquisire e comunicare il CUP per interventi finanziati, anche in parte, con risorse Comunitarie) (Si/No) | [optional] 
**cup_lotto** | **list[str]** | Cup associati al lotto | [optional] 
**ccnl** | **str** | indicare il codice CNEL o non applicabile | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

