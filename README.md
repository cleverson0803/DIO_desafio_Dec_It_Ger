# Sistema de Transações Bancárias

Este projeto implementa um sistema de transações bancárias com funcionalidades de decoradores, geradores e iteradores personalizados.

## Funcionalidades

1. **Decorador de Log**:
   - Registra a data e hora de cada transação, bem como o tipo de transação (depósito, saque, etc).

2. **Gerador de Relatórios**:
   - Permite iterar sobre as transações de uma conta e filtrar por tipo de transação.

3. **Iterador Personalizado**:
   - Itera sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).

## Instruções

1. **Crie os clientes** utilizando a classe `PessoaFisica`.
2. **Crie as contas** utilizando o método `nova_conta` da classe `Conta`.
3. **Adicione as contas aos clientes** utilizando o método `adicionar_conta` da classe `Cliente`.
4. **Realize as transações** (depósitos e saques) utilizando os métodos `depositar` e `sacar` da classe `Conta`.
5. **Gere relatórios de transações** utilizando o método `gerar_relatorio` da classe `Historico`.
6. **Itere sobre as contas do banco** utilizando a classe `ContaIterador`.

## Exemplos de Uso

Veja os exemplos de uso no código anexado para entender como utilizar as funcionalidades do sistema.

## Autor

Desenvolvido por [Cleverson](https://github.com/cleverson0803).
