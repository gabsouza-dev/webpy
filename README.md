# 🌎 Meu Site com Flask

![Flask Badge](https://img.shields.io/badge/Flask-Python-blue)  
![CI](https://github.com/gabsouza-dev/webpy/actions/workflows/ci.yml/badge.svg)  

Um site web simples desenvolvido com **Python** e **Flask**. Ele possui uma página inicial e uma página "Sobre". Além disso, há uma configuração de **GitHub Actions** para CI/CD.

---

## 📌 Recursos  

✔️ Servidor web usando Flask  
✔️ Estrutura simples e escalável  
✔️ Suporte a templates HTML  
✔️ Testes automatizados com **pytest**  
✔️ CI/CD com **GitHub Actions**  

---

## 🚀 Como Executar o Projeto  

### 🔹 1. Clone o Repositório  

```bash
git clone https://github.com/gabsouza-dev/webpy.git
cd webpy
```

### 🔹 2. Crie um ambiente virtual e instale as dependências  

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🔹 3. Execute o Servidor  

```bash
python app.py
```

O site estará disponível em **http://127.0.0.1:5000/** 🎉  

---

## 🧪 Rodando os Testes  

Se houver testes, execute:

```bash
pytest
```

---

## 🔄 Integração Contínua  

Este projeto usa **GitHub Actions** para CI. O workflow roda automaticamente nos eventos:  

✔️ **push** para `main`  
✔️ **pull request** para `main`  

Verifique o status do pipeline no seu repositório na aba **Actions**.

---

## 📂 Estrutura do Projeto  

```
webpy/
│-- app.py                 # Código principal do Flask
│-- requirements.txt        # Dependências do projeto
│-- test_app.py             # Testes automatizados
│-- templates/              # Páginas HTML
│   │-- index.html
│   │-- about.html
│-- static/                 # Arquivos estáticos (CSS, JS, imagens)
│   │-- style.css
│-- .github/                # Configuração do GitHub Actions
│   │-- workflows/
│       │-- ci.yml
```

---

## 📜 Licença  

Este projeto está sob a licença **MIT**. Sinta-se à vontade para usá-lo e modificá-lo! 🚀  

---

## ✨ Autor  

Feito por [Seu Nome](https://github.com/gabsouza-dev) 💻💡