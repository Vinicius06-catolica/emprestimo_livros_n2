### Clonar repo


```bash
git clone https://github.com/Vinicius06-catolica/emprestimo_livros_n2.git
```

### 1. Ativar o ambiente virtual

No terminal do PyCharm ou no terminal do sistema:

```bash
python -m venv .venv
```
---
```bash
.venv\Scripts\activate
OU 
source .venv/bin/activate
```

### 2. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

---

## Executando Testes e Gerando Relatório de Cobertura

### Rodar os testes com coverage:

```bash
coverage run -m unittest test_biblioteca.py
```

### Gerar relatório no terminal:

```bash
coverage report -m
```

### Gerar relatório em HTML:

```bash
coverage html
```

O relatório HTML será gerado na pasta `htmlcov`. Abra o arquivo `index.html` em um navegador para visualizar o relatório detalhado.

---

## Slides

https://www.canva.com/design/DAGo3gCBkPM/Dv41512vTTGp7crV5yHK8w/view?utm_content=DAGo3gCBkPM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hc9ead0cab6
