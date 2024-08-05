		# Notazione Big O e Small o
		
		## Introduzione
		La notazione Big O e Small o sono strumenti matematici utilizzati per descrivere la complessità di algoritmi. Queste notazioni permettono di comprendere come il tempo di esecuzione (o l'uso di risorse) di un algoritmo scala con l'aumento delle dimensioni dell'input.
		
		## Notazione Big O (O-grande)
		
		### Definizione
		La notazione Big O fornisce un limite superiore al tempo di esecuzione di un algoritmo. Formalmente, diciamo che una funzione `f(n)` è `O(g(n))` se esistono costanti positive `c` e `n0` tali che per tutti i `n >= n0`:
		
		\[ f(n) \leq c \cdot g(n) \]
		
		### Interpretazione
		La notazione Big O rappresenta il caso peggiore di un algoritmo. È utilizzata per descrivere il comportamento asintotico di un algoritmo, ignorando le costanti moltiplicative e i termini meno significativi.
		
		### Esempi
		1. Se un algoritmo ha un tempo di esecuzione `f(n) = 3n^2 + 2n + 1`, possiamo dire che è `O(n^2)` poiché per valori grandi di `n`, il termine `n^2` domina gli altri termini.
		2. Un algoritmo con tempo di esecuzione `f(n) = 5n + 20` è `O(n)`.
		
		### Classi di Complessità Comune
		- `O(1)`: Tempo costante.
		- `O(log n)`: Tempo logaritmico.
		- `O(n)`: Tempo lineare.
		- `O(n log n)`: Tempo lineare-logaritmico.
		- `O(n^2)`: Tempo quadratico.
		- `O(2^n)`: Tempo esponenziale.
		- `O(n!)`: Tempo fattoriale.
		
		### Esempi con Grafici
		Di seguito sono riportati alcuni grafici che illustrano le classi di complessità comune:
		
		#### Grafico di `O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n^2)`
		
		![[big_o_examples.png]]
		## Notazione Small o (o-piccolo)
		
		### Definizione
		La notazione Small o fornisce un limite superiore non asintotico, più stretto rispetto alla notazione Big O. Formalmente, diciamo che una funzione `f(n)` è `o(g(n))` se per ogni costante positiva `c` esiste una costante `n0` tale che per tutti i `n >= n0`:
		
		\[ f(n) < c \cdot g(n) \]
		
		### Interpretazione
		La notazione Small o indica che `f(n)` cresce a un ritmo inferiore rispetto a `g(n)` e non può essere uguagliata a `g(n)` moltiplicata per alcuna costante positiva.
		
		### Esempi
		1. Se `f(n) = n` e `g(n) = n^2`, allora `f(n)` è `o(g(n))` perché `n` cresce molto più lentamente di `n^2`.
		2. Se `f(n) = log(n)` e `g(n) = n`, allora `f(n)` è `o(g(n))`.
		
		### Differenze tra Big O e Small o
		- Big O (`O(g(n))`): Indica che `f(n)` è al massimo di ordine `g(n)`.
		- Small o (`o(g(n))`): Indica che `f(n)` è di ordine strettamente inferiore a `g(n)`.
		
		### Esempi con Grafici
		Di seguito sono riportati alcuni grafici che illustrano la differenza tra Big O e Small o:
		
		#### Grafico di `f(n) = n` e `g(n) = n^2`
		![[small_o_example.png]]
		
		## Conclusioni
		La comprensione delle notazioni Big O e Small o è fondamentale per l'analisi degli algoritmi, poiché permette di valutare e confrontare l'efficienza degli algoritmi in termini di tempo di esecuzione e utilizzo delle risorse. La scelta dell'algoritmo ottimale per un problema specifico spesso dipende dall'analisi della sua complessità asintotica.
