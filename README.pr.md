



# Nexus
  
Módulo para conectar-se à API Nexus, permitindo ler/gravar dados e ouvir eventos em tempo real.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Conectar ao Nexus  
Estabelece uma sessão com a API Nexus usando uma API Key.

2. Listar Tabelas  
Retorna todas as tabelas disponíveis para esta API Key.

3. Obter Tabela  
Retorna a definição de uma tabela pelo ID.

4. Criar Tabela  
Cria uma nova tabela.

5. Atualizar Tabela  
Atualiza metadados da tabela (nome, colunas).

6. Excluir Tabela  
Exclui permanentemente uma tabela e todas as suas linhas.

7. Atualizar Célula  
Atualiza o valor de uma célula em uma linha.

8. Obter Linhas  
Obtém linhas de uma tabela do Nexus.

9. Inserir Linha  
Insere uma nova linha em uma tabela do Nexus.

10. Atualizar Linha  
Atualiza uma linha existente pelo seu ID.

11. Excluir Linha  
Exclui uma linha pelo seu ID.

12. Excluir Todas as Linhas  
Apaga todas as linhas de uma tabela sem excluir a tabela.

13. Listar Consultas  
Retorna todas as consultas salvas para esta API Key.

14. Executar Query  
Executa uma query salva no Nexus com parâmetros opcionais.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**requests**](https://pypi.org/project/requests/)
### License
  
![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)  
[MIT](https://opensource.org/license/mit)