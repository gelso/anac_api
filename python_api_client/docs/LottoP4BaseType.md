# LottoP4BaseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servizio_pubblico_locale** | **bool** | Flag servizio pubblico locale | 
**lot_identifier** | **str** | Id univoco del lotto generato dalla stazione appaltante | 
**condizioni_negoziata** | [**list[CondizioniNegoziataEnum]**](CondizioniNegoziataEnum.md) |  | [optional] 
**cod_istat** | [**CodIstatEnum**](CodIstatEnum.md) |  | 
**contratti_disposizioni_particolari** | [**ContrattiDisposizioniParticolariEnum**](ContrattiDisposizioniParticolariEnum.md) |  | 
**lavoro_o_acquisto_previsto_in_programmazione** | **bool** | Il lavoro o l’acquisto di bene o servizio è stato previsto all’interno della programmazione | 
**cui** | **str** | CUI programma triennale lavori pubblici o programma biennale forniture e servizi | [optional] 
**ipotesi_collegamento** | [**IpotesiCollegamentoType**](IpotesiCollegamentoType.md) |  | [optional] 
**opzioni_rinnovi** | **bool** | L’appalto prevede opzioni/rinnovi? | 
**afferente_investimenti_pnrr** | **bool** | L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)? | 
**acquisizione_cup** | **bool** | Il contratto è finalizzato alla realizzazione di progetti d&#x27;investimento pubblico per i quali è prevista l&#x27;acquisizione del codice CUP ai sensi dell&#x27;art. 11 L. 3/2003 e ss.mm.? (E&#x27; necessario acquisire e comunicare il CUP per interventi finanziati, anche in parte, con risorse Comunitarie) (Si/No) | [optional] 
**cup_lotto** | **list[str]** | Cup associati al lotto | [optional] 
**parita_di_genere_generazionale** | [**ParitaDiGenereGenerazionaleType**](ParitaDiGenereGenerazionaleType.md) |  | [optional] 
**modalita_acquisizione** | [**ModalitaAcquisizioneEnum**](ModalitaAcquisizioneEnum.md) |  | [optional] 
**tipologia_lavoro** | [**list[TipologiaLavoroEnum]**](TipologiaLavoroEnum.md) |  | 
**categoria** | [**CategoriaEnum**](CategoriaEnum.md) |  | 
**finanziamenti** | [**list[FinanziamentoType]**](FinanziamentoType.md) | Dati relativi ai finanziamenti | [optional] 
**dati_base** | [**DatiBaseLottoType**](DatiBaseLottoType.md) |  | [optional] 
**dati_base_cpv** | [**DatiBaseCPVType**](DatiBaseCPVType.md) |  | [optional] 
**dati_base_contratto** | [**DatiBaseContrattoType**](DatiBaseContrattoType.md) |  | [optional] 
**dati_base_aggiudicazione** | [**DatiBaseAggiudicazioneOptionalType**](DatiBaseAggiudicazioneOptionalType.md) |  | [optional] 
**dati_base_aggiuntivi** | [**DatiBaseAggiuntiviType**](DatiBaseAggiuntiviType.md) |  | [optional] 
**dati_base_termini_invio** | [**DatiTerminiInvioType**](DatiTerminiInvioType.md) |  | [optional] 
**dati_base_accessibilita** | [**DatiBaseAccessibilitaType**](DatiBaseAccessibilitaType.md) |  | [optional] 
**dati_base_documenti** | **AllOfLottoP4BaseTypeDatiBaseDocumenti** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

