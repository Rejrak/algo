import matplotlib.pyplot as plt
import numpy as np

# Dati per i grafici
n = np.linspace(1, 10, 100)
o_1 = np.ones_like(n)
o_log_n = np.log(n)
o_n = n
o_n_log_n = n * np.log(n)
o_n2 = n ** 2

# Grafico Big O
plt.figure(figsize=(10, 6))
plt.plot(n, o_1, label='O(1)')
plt.plot(n, o_log_n, label='O(log n)')
plt.plot(n, o_n, label='O(n)')
plt.plot(n, o_n_log_n, label='O(n log n)')
plt.plot(n, o_n2, label='O(n^2)')
plt.yscale('log')
plt.xlabel('Dimensione Input (n)')
plt.ylabel('Tempo di Esecuzione')
plt.title('Esempi di Notazione Big O')
plt.legend()
plt.grid(True)
plt.savefig('./images/big_o_examples.   png')
plt.show()

# Grafico Small o
f_n = n
g_n = n ** 2

plt.figure(figsize=(10, 6))
plt.plot(n, f_n, label='f(n) = n')
plt.plot(n, g_n, label='g(n) = n^2')
plt.xlabel('Dimensione Input (n)')
plt.ylabel('Funzione')
plt.title('Esempio di Notazione Small o')
plt.legend()
plt.grid(True)
plt.savefig('   ./images/small_o_example.png')
plt.show()
