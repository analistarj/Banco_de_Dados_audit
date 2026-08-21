# Auditoria Oracle, protótipo

Protótipo educacional em Python para habilitar comandos tradicionais de auditoria do Oracle e consultar eventos registrados em `DBA_AUDIT_TRAIL`.

## O que o código atual faz

O arquivo `oracle_script1.py`:

1. cria uma conexão Oracle usando parâmetros substituíveis;
2. executa comandos `AUDIT` para sessão e alterações em tabelas;
3. consulta eventos de logon;
4. consulta eventos de inserção, atualização e exclusão;
5. imprime os resultados no terminal;
6. encerra a conexão.

## Status

Este repositório ainda não é uma ferramenta pronta para produção.

Limitações conhecidas:

- não possui interface de linha de comando;
- não possui testes automatizados ou integração contínua;
- não trata erros, timeouts ou interrupções;
- imprime metadados de auditoria diretamente no terminal;
- depende do modelo tradicional de auditoria e de `DBA_AUDIT_TRAIL`;
- não implementa Oracle Unified Auditing;
- não gera relatório protegido ou anonimizado.

## Segurança

Execute somente com autorização formal do responsável pelo banco de dados. Os comandos `AUDIT` alteram a configuração de auditoria e podem exigir privilégios elevados.

- nunca grave usuário e senha reais no código;
- prefira Oracle Wallet ou um cofre corporativo;
- use uma conta com o menor privilégio possível;
- não publique logs contendo nomes de usuários, hosts, terminais ou objetos;
- teste primeiro em um banco isolado com dados sintéticos;
- valide o impacto de volume e retenção dos registros de auditoria.

Os valores `<HOST>`, `<PORT>`, `<SERVICE_NAME>`, `<USERNAME>` e `<PASSWORD>` são apenas marcadores e devem permanecer sem credenciais reais no repositório.

## Requisitos atuais

- Python 3;
- driver `cx_Oracle`;
- Oracle Client compatível;
- autorização para executar os comandos de auditoria;
- acesso de leitura a `DBA_AUDIT_TRAIL`.

## Próximos passos

- separar configuração, coleta e apresentação;
- migrar para o driver `oracledb`;
- adicionar tratamento de erros e fechamento seguro;
- suportar Unified Auditing;
- criar saída protegida e minimizada;
- adicionar testes com objetos simulados;
- configurar lint e GitHub Actions.

## Uso responsável

Este projeto serve como base de aprendizagem e não deve ser executado em produção sem revisão de DBA, Segurança da Informação e Auditoria.
