# PRODUTOR-CONSUMIDOR NA PLATAFORMA WINDOWS
Implementação do algoritmo produtor-consumidor em Python, utilizando a API do Windows 

Chamado de Produtor e o Consumidor (também conhecido como o problema do buffer limitado), consiste em um conjunto de processos que compartilham um mesmo buffer. Os processos chamados produtores põem informação no buffer. Os processos chamados consumidores retiram informação deste buffer. 

Esse é um problema clássico em sistemas operacionais, que busca exemplificar de forma clara, situações de impasses que ocorrem no gerenciamento de processos de um sistema operacional.

Há dois códigos executáveis independentes, porém correlacionados.

* PRODUTOR

Ao executar o algoritmo produtor.py, o mesmo começa a produzir no buffer conpartilhado até o limite definido.
Se, ao iniciar uma instância do produtor, o buffer estiver vazio, o mesmo produz.
Por outro lado, se o buffer já estiver cheio, o produtor aguarda liberação de espaço no buffer.

* CONSUMIDOR

Ao executar o algoritmo consumidor.py, o mesmo começa a consumir do buffer conpartilhado até o mesmo esvaziar.
Se, ao iniciar uma instância do consumidor, o buffer estiver cheio, o mesmo consome.
Por outro lado, se o buffer já estiver vazio, o produtor aguarda produção no buffer.

# Métodos Utilizados

* Semáforos
* Memória Compartilhada
* Threads
