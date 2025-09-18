<h1 align="center"> 👤 Projeto Avançado com User Models no Django </h1>

Este repositório faz parte do curso **Programação Web com Python e Django Framework: Essencial**, ministrado pela **Geek University** na plataforma Udemy.  

📌 O foco deste projeto é o estudo e a prática avançada de **User Models no Django**, explorando desde o modelo padrão até a criação de usuários customizados, perfis e signals.  

---

## 📚 Sobre o curso
- **Plataforma:** Udemy  
- **Professor:** Geek University  
- **Curso:** Programação Web com Python e Django Framework: Essencial  

---

## 📝 Conteúdo explorado

Durante o projeto, foram estudados e aplicados os seguintes conceitos sobre **User Models no Django**:

- Modelo de usuário padrão (`django.contrib.auth.models.User`).
- Customização do modelo de usuário:
  1. **Perfil (OneToOneField)** para armazenar informações extras.  
  2. **Custom User Model** herdando de `AbstractUser` ou `AbstractBaseUser`.  
  3. **Campos adicionais** diretamente no modelo customizado.  
- Configuração no `settings.py` com `AUTH_USER_MODEL`.  
- Criação e execução de **migrações**.  
- Registro e customização no **Django Admin**.  
- **Autenticação e permissões** (login, logout, grupos e permissões individuais).  
- Uso de **signals** (`post_save`) para criar perfis automaticamente.  
- Boas práticas para projetos Django que utilizam modelos de usuário customizados.  

---

## 📂 Estrutura do repositório

O repositório contém os arquivos do projeto Django com as implementações de **User Models**, incluindo exemplos de:

- Modelo customizado de usuário.  
- Uso de `signals` para criar perfis.  
- Configuração no `settings.py`.  

<p align="left">
  <img width="174" height="262" alt="print_projeto" src="https://github.com/user-attachments/assets/62729ed8-9cc6-4b24-9669-089a83f6303d" alt="imgprojeto" />
</p>

---

## 🖥 Como executar o projeto

### 1) Pré-requisitos
- Python 3.8+  
- Django 3.2+ (ou versão utilizada no curso)  
- Pip instalado  

Verifique:
```bash
python --version
python -m pip --version
```

### 2) Criar e ativar ambiente virtual
Crie:
```bash
python -m venv venv
```

Ative:  
- **Windows**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/MacOS**
  ```bash
  source venv/bin/activate
  ```

### 3) Instalar dependências
Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 4) Rodar migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5) Criar superusuário
```bash
python manage.py createsuperuser
```

### 6) Executar servidor
```bash
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📝 Observações
- Este projeto foi desenvolvido como parte do curso, servindo como **anotações práticas e de referência**.  
- A ideia é consolidar os principais pontos do **User Model no Django**, desde o uso básico até a customização avançada.  

---

## 📩 Contato
Caso queira trocar ideias sobre Django ou desenvolvimento, fique à vontade para entrar em contato! 😄
