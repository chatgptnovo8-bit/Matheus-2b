# Sistema de Cadastro de Alunos

Versão simplificada da tarefa de aprofundamento em Python, conforme o enunciado anexado.

## Como executar

Com o Python 3 instalado, abra a pasta no VS Code e execute o arquivo pelo terminal:

```bash
python sistema_cadastro_alunos.py
```

Também é possível executar diretamente pelo botão **Run Python File** do VS Code.

## Funcionalidades

1. Cadastrar um ou mais alunos.
2. Listar os alunos e suas situações.
3. Pesquisar um aluno pelo nome ou parte do nome.
4. Calcular a média geral da turma.
5. Sair do sistema.
6. Mostrar a quantidade total de alunos cadastrados com `len()`.
7. Mostrar a quantidade de alunos aprovados.

## Requisitos atendidos

- Lista global `alunos` para armazenamento dos cadastros.
- Dicionários com as chaves `nome` e `nota` para cada aluno.
- Funções organizadas com `def`.
- Condicionais `if`, `elif` e `else`.
- Laços `for` e `while`.
- Tratamento de entradas inválidas com `try` e `except`.
- Cadastro de múltiplos alunos.
- Situação **Aprovado** para notas maiores ou iguais a 7 e **Recuperação** para notas abaixo de 7.
- Cálculo da média da turma, contagem de aprovados e total de alunos cadastrados.
