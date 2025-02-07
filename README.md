# Lista de contatos

Esta lista de contatos é um sistema CRUD, feito com Python e uma integração ao mySQL. Nele, é possível adicionar, editar, buscar ou remover contatos em uma lista, cada contato podendo possuir um nome, um número de telefone, um endereço de e-mail, uma data de nascimento e notas adicionais.
Os nomes não podem ser repetidos.

## Instalação

1. Baixar os arquivos `crud_contatos.py`, `dump_contatos.sql` e `requirements.txt`

2. Criar um ambiente virtual
   
```bash
python -m venv venv
```
3. Ativar o ambiente virtual

4. Instalar as bibliotecas do arquivo `requirements.txt`:

   
```bash
pip install -r requirements.txt
```


6.  Converter o arquivo `dump_contatos.sql` em um banco de dados

7. Executar o arquivo `crud_contatos.py`.

_Observação:_ As credenciais do usuário podem estar erradas. Altere as credenciais no código fonte (linhas 9, 10 e 11) caso necessário.
