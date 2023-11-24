# LottoP3BaseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lot_identifier** | **str** | Id univoco del lotto generato dalla stazione appaltante - corrisponde al campo bt-137 - Purpose Lot Identifier del TED | 
**cod_istat** | [**CodIstatEnum**](CodIstatEnum.md) |  | 
**acquisizione_cup** | **bool** | Il contratto è finalizzato alla realizzazione di progetti d&#x27;investimento pubblico per i quali è prevista l&#x27;acquisizione del codice CUP ai sensi dell&#x27;art. 11 L. 3/2003 e ss.mm.? (E&#x27; necessario acquisire e comunicare il CUP per interventi finanziati, anche in parte, con risorse Comunitarie) (Si/No) | [optional] 
**cup_lotto** | **list[str]** | Cup associati al lotto | [optional] 
**modalita_acquisizione** | [**ModalitaAcquisizioneEnum**](ModalitaAcquisizioneEnum.md) |  | [optional] 
**tipologia_lavoro** | [**list[TipologiaLavoroEnum]**](TipologiaLavoroEnum.md) |  | 
**oggetto_principale_contratto** | [**OggettoPrincipaleContrattoEnum**](OggettoPrincipaleContrattoEnum.md) |  | [optional] 
**parita_di_genere_generazionale** | [**ParitaDiGenereGenerazionaleType**](ParitaDiGenereGenerazionaleType.md) |  | [optional] 
**finanziamenti** | [**list[FinanziamentoType]**](FinanziamentoType.md) | Dati relativi ai finanziamenti | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

