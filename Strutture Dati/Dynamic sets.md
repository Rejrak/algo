
Le **strutture dati** o **set di dati** che possono crescere o ridursi nel tempo sono chiamati **_dynamic sets_.**

Gli algoritmi possono voler effettuare vari tipi di operazioni sui sets.

In particolare i sets che supportano l’inserimento, la cancellazione e la verifica dell’appartenenza sono detti _**dictionaries**_.

## Operazioni sui dynamic sets

Operazioni sui dynamic sets possono essere raggruppate in due gruppi:

- **Queries**(interrogazioni) - operazioni che forniscono informazioni sul set.
- **Modifying operations** - operazioni che modificano il set.

Le operazioni più comuni sono:

- **$_Search(S, k)_$**: Una query che, dato un insieme **$S$** e un valore chiave **$k$**, restituisce un puntatore **x** a un elemento in **$S$** tale che $x.key = k$, oppure $NULL$ se nessun elemento appartiene a $S$.
- $Insert(S,x)$: Un'operazione di modifica che aggiunge l'elemento puntato da $x$ all'insieme $S$. Di solito si assume che tutti gli attributi dell'elemento $x$ necessari all'implementazione dell'insieme siano già stati inizializzati.
- $Delete(S, x)$: Un'operazione di modifica che, dato un puntatore $x$ a un elemento dell'insieme $S$, rimuove $x$ da $S$. (Si noti che questa operazione prende un puntatore a un elemento x, non un valore chiave).
- $Minimum(S)$ e $Massimo(S)$: Interrogazioni su un insieme totalmente ordinato $S$ che restituiscono:
    - un puntatore all'elemento di $S$ con k più piccolo (per Minimum).
        - un puntatore all'elemento di $S$ con k più grande (per Maximum).
- $Successor(S,x)$: Una query che, dato un elemento $x$ la cui chiave proviene da un insieme totalmente ordinato $S$, restituisce un puntatore al prossimo elemento più grande di $S$, oppure $NULL$ se $x$ è l'elemento massimo.
- $Predecessor(S, x)$: Una query che, dato un elemento $x$ la cui chiave proviene da un insieme totalmente ordinato $S$, restituisce un puntatore al prossimo elemento più piccolo in $S$, o $NULL$ se $x$ è l'elemento minimo.

In alcune situazioni, è possibile estendere le query $Successor$ e $Predecessor$ in modo che si applichino a insiemi con chiavi non distinte.