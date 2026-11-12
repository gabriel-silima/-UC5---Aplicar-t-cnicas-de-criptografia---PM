# Manutenção do acervo

Preserve a estrutura do Classroom: `classroom/mural/` e `classroom/atividades/nenhum-tema/`. Não reagrupe os anexos por assunto sem uma nova solicitação.

1. Identifique a publicação e a posição do anexo.
2. Preserve o nome recebido e o conteúdo original em `anexos/`.
3. No catálogo JSON e CSV, registre origem, seção, publicação, data, ordem, caminho, tamanho e SHA-256.
4. Use `download_pendente` até que o arquivo esteja presente. `copia_salva` exige bytes verificados. Uma referência externa não é uma cópia.
5. Atualize os índices Markdown, as pendências e os totais do README juntos.

No PowerShell, obtenha a integridade com `Get-FileHash -Algorithm SHA256 -LiteralPath "caminho-do-arquivo"` e o tamanho com `(Get-Item -LiteralPath "caminho-do-arquivo").Length`.

Registros de práticas ficam em `registros/`. Não marque uma prática como executada sem evidência. Materiais de terceiros mantêm sua autoria. Senhas, tokens e chaves privadas de uso real não devem ser incluídos no repositório público.
