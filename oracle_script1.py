import cx_Oracle

# Configuração de conexão com o banco de dados Oracle
dsn_tns = cx_Oracle.makedsn('<HOST>', '<PORT>', service_name='<SERVICE_NAME>')
conn = cx_Oracle.connect(user='<USERNAME>', password='<PASSWORD>', dsn=dsn_tns)

# Habilita a auditoria de logon
cursor = conn.cursor()
cursor.execute("AUDIT SESSION")

# Habilita a auditoria de alterações em tabelas
cursor.execute("AUDIT ALTER TABLE")
cursor.execute("AUDIT INSERT TABLE")
cursor.execute("AUDIT UPDATE TABLE")
cursor.execute("AUDIT DELETE TABLE")

# Exibe as informações de auditoria de logon
cursor.execute("SELECT OS_USERNAME, USERNAME, USERHOST, TERMINAL, TIMESTAMP, ACTION_NAME FROM DBA_AUDIT_TRAIL WHERE ACTION_NAME = 'LOGON'")
for row in cursor.fetchall():
    print(row)

# Exibe as informações de auditoria de alterações em tabelas
cursor.execute("SELECT OS_USERNAME, USERNAME, USERHOST, TERMINAL, TIMESTAMP, ACTION_NAME, OBJ_NAME FROM DBA_AUDIT_TRAIL WHERE ACTION_NAME IN ('INSERT', 'UPDATE', 'DELETE')")
for row in cursor.fetchall():
    print(row)

# Encerra a conexão com o banco de dados
conn.close()

