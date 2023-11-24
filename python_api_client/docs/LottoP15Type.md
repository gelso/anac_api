# LottoP15Type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lot_identifier** | **str** | Id univoco del lotto generato dalla stazione appaltante - corrisponde al campo bt-137 - Purpose Lot Identifier del TED | 
**strumenti_elettronici_specifici** | **bool** | Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche | [optional] 
**cod_istat** | [**CodIstatEnum**](CodIstatEnum.md) |  | 
**servizio_pubblico_locale** | **bool** | Flag servizio pubblico locale | 
**lavoro_o_acquisto_previsto_in_programmazione** | **bool** | Il lavoro o l’acquisto di bene o servizio è stato previsto all’interno della programmazione | 
**cui** | **str** | CUI programma triennale lavori pubblici o programma biennale forniture e servizi | [optional] 
**ripetizioni_e_consegne_complementari** | **bool** | L’appalto prevede ripetizioni di servizi/forniture/lavori analoghi e consegne complementari? | 
**ipotesi_collegamento** | [**IpotesiCollegamentoType**](IpotesiCollegamentoType.md) |  | [optional] 
**opzioni_rinnovi** | **bool** | L’appalto prevede opzioni/rinnovi? | 
**afferente_investimenti_pnrr** | **bool** | L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)? | 
**acquisizione_cup** | **bool** | Il contratto è finalizzato alla realizzazione di progetti d&#x27;investimento pubblico per i quali è prevista l&#x27;acquisizione del codice CUP ai sensi dell&#x27;art. 11 L. 3/2003 e ss.mm.? (E&#x27; necessario acquisire e comunicare il CUP per interventi finanziati, anche in parte, con risorse Comunitarie) (Si/No) | [optional] 
**cup_lotto** | **list[str]** | Cup associati al lotto | [optional] 
**parita_di_genere_generazionale** | [**ParitaDiGenereGenerazionaleType**](ParitaDiGenereGenerazionaleType.md) |  | [optional] 
**ccnl** | **str** | indicare il codice CNEL o non applicabile | 
**tipologia_lavoro** | [**list[TipologiaLavoroEnum]**](TipologiaLavoroEnum.md) |  | [optional] 
**modalita_acquisizione** | [**ModalitaAcquisizioneEnum**](ModalitaAcquisizioneEnum.md) |  | [optional] 
**categoria** | [**CategoriaEnum**](CategoriaEnum.md) |  | 
**prestazioni_comprese** | [**PrestazioniEnum**](PrestazioniEnum.md) |  | 
**oggetto_principale_contratto** | [**OggettoPrincipaleContrattoEnum**](OggettoPrincipaleContrattoEnum.md) |  | [optional] 
**finanziamenti** | [**list[FinanziamentoType]**](FinanziamentoType.md) | Dati relativi ai finanziamenti | [optional] 
**quadro_economico_standard** | [**QuadroEconomicoType**](QuadroEconomicoType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

