# Projeto Jenkins - Conversor de Temperatura

Projeto de demonstração de CI/CD com Jenkins usando Pipeline as Code.

## Métodos
- `fahrenheit_para_celsius(f)` — converte Fahrenheit para Celsius
- `celsius_para_fahrenheit(c)` — converte Celsius para Fahrenheit

## Como rodar localmente

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Cobertura de código

```bash
pytest --cov=src --cov-report=html
```

## Pipeline CI/CD

O pipeline está definido no arquivo `Jenkinsfile` e executa as seguintes etapas:
1. Checkout do código
2. Setup do ambiente Python
3. Build (verificação de sintaxe)
4. Testes automatizados com cobertura