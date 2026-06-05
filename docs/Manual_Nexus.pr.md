



# Nexus
  
Módulo para conectar-se à API Nexus, permitindo ler/gravar dados e ouvir eventos em tempo real.  

*Read this in other languages: [English](Manual_Nexus.md), [Português](Manual_Nexus.pr.md), [Español](Manual_Nexus.es.md)*
  
![banner](imgs/BANNER_NEXUS.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar ao Nexus
  
Estabelece uma sessão com a API Nexus usando uma API Key.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL base|URL base do servidor Rocketview (ex. https//rocketview.myrb.io).|https://rocketview.myrb.io|
|API Key|API Key gerada nas configurações do app no Nexus.|rv_xxxxxxxxxxxxxxxx|
|Nome da sessão|Nome único para identificar esta sessão de conexão.|default|
|Variável resultado|Variável onde True será armazenado se a conexão for bem-sucedida.|resultado|

### Listar Tabelas
  
Retorna todas as tabelas disponíveis para esta API Key.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da sessão|Nome da sessão usada ao conectar.|default|
|Variável resultado|Variável onde a lista de tabelas será armazenada.|tabelas|

### Obter Tabela
  
Retorna a definição de uma tabela pelo ID.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da tabela|ID da tabela a obter.|id-da-tabela|
|Nome da sessão|Nome da sessão usada ao conectar.|default|
|Variável resultado|Variável onde a definição da tabela será armazenada.|tabela|

### Criar Tabela
  
Cria uma nova tabela.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Definição da tabela (JSON)|Objeto JSON com o nome e colunas da tabela.|{"name": "produtos", "columns": []}|
|Nome da sessão|Nome da sessão usada ao conectar.|default|
|Variável resultado|Variável onde a tabela criada será armazenada.|nova_tabela|

### Atualizar Tabela
  
Atualiza metadados da tabela (nome, colunas).
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da tabela|ID da tabela a atualizar.|id-da-tabela|
|Dados atualizados (JSON)|Objeto JSON com os campos a atualizar.|{"name": "novo_nome"}|
|Nome da sessão|Nome da sessão usada ao conectar.|default|
|Variável resultado|Variável onde a tabela atualizada será armazenada.|tabela_atualizada|

### Excluir Tabela
  
Exclui permanentemente uma tabela e todas as suas linhas.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da tabela|ID da tabela a excluir.|id-da-tabela|
|Nome da sessão|Nome da sessão usada ao conectar.|default|
|Variável resultado|Variável onde True será armazenado se a tabela foi excluída.|resultado|

### Atualizar Célula
  
Atualiza o valor de uma célula em uma linha.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da tabela|ID da tabela.|id-da-tabela|
|ID da linha|ID da linha a atualizar.|id-da-linha|
|Nome da coluna|Nome da coluna a atualizar.|preco|
|Novo valor|O novo valor para a célula.|99.99|
|Nome da sessão|Nome da sessão usada ao conectar.|default|
|Variável resultado|Variável onde a resposta será armazenada.|linha_atualizada|

### Obter Linhas
  
Obtém linhas de uma tabela do Nexus.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da tabela|ID da tabela do Nexus para leitura.|id-da-tabela|
|Limite (opcional)|Número máximo de linhas a retornar. Padrão 100.|100|
|Deslocamento (opcional)|Número de linhas a pular. Padrão 0.|0|
|Nome da sessão|Nome da sessão usada ao conectar.|session|
|Variável resultado|Variável onde a lista de linhas será armazenada.|linhas|

### Inserir Linha
  
Insere uma nova linha em uma tabela do Nexus.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da tabela|ID da tabela onde a linha será inserida.|id-da-tabela|
|Dados da linha (JSON)|Objeto JSON com os pares coluna/valor a inserir.|{"campo1": "valor1", "preco": 99.99}|
|Nome da sessão|Nome da sessão usada ao conectar.|session|
|Variável resultado|Variável onde a linha inserida (com seu ID) será armazenada.|nova_linha|

### Atualizar Linha
  
Atualiza uma linha existente pelo seu ID.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da linha|ID da linha a atualizar.|id-da-linha|
|Dados atualizados (JSON)|Objeto JSON com os campos a atualizar.|{"preco": 199.99, "estoque": 5}|
|Nome da sessão|Nome da sessão usada ao conectar.|session|
|Variável resultado|Variável onde a linha atualizada será armazenada.|linha_atualizada|

### Excluir Linha
  
Exclui uma linha pelo seu ID.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da linha|ID da linha a excluir.|id-da-linha|
|Nome da sessão|Nome da sessão usada ao conectar.|session|
|Variável resultado|Variável onde True será armazenado se a linha foi excluída.|resultado|

### Excluir Todas as Linhas
  
Apaga todas as linhas de uma tabela sem excluir a tabela.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da tabela|ID da tabela a limpar.|id-da-tabela|
|Nome da sessão|Nome da sessão usada ao conectar.|default|
|Variável resultado|Variável onde True será armazenado em caso de sucesso.|resultado|

### Listar Consultas
  
Retorna todas as consultas salvas para esta API Key.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da sessão|Nome da sessão usada ao conectar.|default|
|Variável resultado|Variável onde a lista de consultas será armazenada.|consultas|

### Executar Query
  
Executa uma query salva no Nexus com parâmetros opcionais.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da query|ID da query a executar.|id-da-query|
|Parâmetros (JSON, opcional)|Objeto JSON com parâmetros dinâmicos para a query.|{"busca": "laptop", "precoMin": 100}|
|Nome da sessão|Nome da sessão usada ao conectar.|session|
|Variável resultado|Variável onde o resultado da query será armazenado.|resultado_query|
