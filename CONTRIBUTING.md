# Como adicionar materiais da UC5

1. Encontre a pasta do assunto no README.
2. Preserve os arquivos recebidos. Use nomes sem espaços e sem acentos nos caminhos para facilitar o uso no terminal.
3. Antes de importar, confira o título e o link no catálogo para evitar duplicação.
4. Adicione ou atualize o registro em `catalogo/materiais.json` e `catalogo/materiais.csv`. Use `download_pendente` quando só houver o link; use `copia_salva` quando os bytes estiverem presentes.
5. Registre o SHA-256 e o tamanho. No PowerShell: `Get-FileHash -Algorithm SHA256 -LiteralPath "caminho-do-arquivo"` e `(Get-Item -LiteralPath "caminho-do-arquivo").Length`.
6. Atualize os índices Markdown e os totais do README.
7. Para versões revisadas de materiais, mantenha a origem, descreva a alteração e faça um commit com mensagem clara.

Práticas e evidências ficam em `registros/AAAA-MM-DD-assunto/`. Registre o resultado observado; não marque uma prática como concluída sem sua execução. Não envie senhas, tokens, chaves privadas de uso real ou arquivos de ambiente para o repositório público.

Os materiais de terceiros mantêm sua autoria. Arquivos grandes, especialmente vídeos e máquinas virtuais, precisam de uma estratégia de armazenamento apropriada antes de sua inclusão no Git.
