# NETFLOWBR
Sistema de Gestão de Tickets e OS para Provedores de Internet (ISP)

# 🌐 NetFlowBR — Sistema de Gestão de Tickets e OS para Provedores de Internet (ISP)

> 🚀 **Acesse o sistema online e homologado:** [https://netflowbr.onrender.com/](https://netflowbr.onrender.com/)

O **NetFlowBR** é uma aplicação web de nível profissional desenvolvida sob medida para a operação da **Rede BR Telecom**[cite: 1]. O sistema funciona como um centralizador de suporte técnico (CRM/Helpdesk) focado na resolução de falhas de conexão, instalações e atendimentos em campo, substituindo o gerenciamento descentralizado por um fluxo de trabalho estruturado, inteligente e seguro[cite: 1].

*Nota: Para facilitar a homologação, testes rápidos de recrutadores e demonstração de portfólio, o sistema está configurado para acesso direto, sem barreiras de autenticação/login.*

---

## 🚀 Principais Funcionalidades

### 1. Painel Executivo Dinâmico (Dashboard)
* **Indicadores em Tempo Real:** Cards dinâmicos no topo da página que monitoram e exibem a quantidade exata de chamados filtrados por status: *Abertos*, *Em Atendimento* e *Finalizados*[cite: 1, 3].
* **Tomada de Decisão Rápida:** Permite aos gestores mapear o gargalo da operação técnica em segundos[cite: 1].

### 2. Gestão de SLA Inteligente (Service Level Agreement)
* **Cálculo Automático de Prazos:** O sistema utiliza lógica integrada no back-end (`esta_atrasado`) para verificar de forma autônoma se um ticket ultrapassou o tempo limite de atendimento[cite: 1, 3].
* **Alertas Visuais na Tabela:** Caso um ticket esteja fora do prazo aceitável de resposta, a linha inteira do cliente é destacada com uma interface visual chamativa, impedindo que o chamado seja esquecido[cite: 1, 3].

### 3. Sinalização Dinâmica de Prioridade
* **Foco no que Importa:** O sistema conta com uma estrutura booleana simplificada para definir urgência[cite: 1, 9]. Chamados urgentes ganham um destaque imediato com o selo vermelho **⚠ PRIORIDADE**[cite: 1, 3].
* **Impacto no SLA:** O prazo tolerável de um ticket normal é de **3 dias**, enquanto os tickets com o selo de prioridade têm o tempo de resposta reduzido para **2 dias**, reajustando automaticamente a regra de atraso[cite: 1, 9].

### 4. Usabilidade e UI/UX Avançada
* **Componentes Modernos:** Telas construídas com **Bootstrap 5** totalmente responsivas[cite: 1].
* **Componente Customizado (Switch):** Substituição de checkboxes nativos pálidos do navegador por um botão estilo *Switch (Interruptor)* customizado via CSS isolado (`newcall.css`), que se expande em escala e muda dinamicamente para vermelho vibrante ao ser ativado pelo técnico[cite: 1, 5, 8].
* **Notificações Integradas (Django Messages):** Mensagens flutuantes de feedback no topo da tela (*Toasts/Alerts*) que notificam o operador instantaneamente quando uma ação é executada (ex: *"Chamado criado com sucesso!"*)[cite: 1].

### 5. Emissão de Ordens de Serviço (Relatórios em PDF)
* **Geração Automatizada:** Integração com a biblioteca **ReportLab** para compilar todos os dados de um chamado em uma folha de Ordem de Serviço (OS) limpa e padronizada com um único clique[cite: 1, 2].
* **Documentação de Campo:** O arquivo gerado serve como documento impresso ou digital para o técnico levar até a rua, contendo campos para colher a assinatura do cliente e validar juridicamente a execução do reparo[cite: 1].

---

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python 3 + Django Framework (Camada MVT - Model, View, Template)[cite: 1]
* **Banco de Dados:** SQLite (com estrutura relacional adaptada para migrações dinâmicas)[cite: 1, 9]
* **Front-end:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons[cite: 1]
* **Geração de Arquivos:** ReportLab (Geração estática de PDF em tempo real)[cite: 1]

---

## 📁 Estrutura de Arquivos Principais

O projeto foi organizado seguindo as melhores práticas arquiteturais do Django:

* `models.py`: Guarda a tabela `Chamado` com todas as propriedades (cliente, titulo, descricao, status, prioridade, data_criacao) e os métodos de cálculo de atraso[cite: 1, 9].
* `forms.py`: Controla a validação dos formulários, injetando classes de design do Bootstrap de forma segura[cite: 1, 8].
* `views.py`: Processa a lógica de negócios, filtros de busca por nome de cliente, contador de status e geração do PDF[cite: 1, 3].
* `urls.py`: Mapeia as rotas amigáveis do sistema (Lista, Criação, Detalhes, Edição, Exclusão e PDF)[cite: 1].
* `templates/`: Diretório contendo os blocos reutilizáveis (`base.html`), formulários de cadastro e o painel de listagem[cite: 1, 3, 5].

---

## 💻 Como Rodar o Projeto Localmente

Siga os passos abaixo no seu terminal (CMD) para configurar e executar o sistema na sua máquina:

```bash
# 1. Clonar o repositório e entrar na pasta do projeto
git clone [https://github.com/asafearaujo/NETFLOWBR.git](https://github.com/asafearaujo/NETFLOWBR.git)
cd NetFlowBR

# 2. Criar e ativar o ambiente virtual (VENV no Windows)
python -m venv venv
venv\Scripts\activate

# 3. Instalar as dependências do sistema
pip install django reportlab gunicorn

# 4. Executar as migrações do banco de dados (SQLite)
python manage.py makemigrations
python manage.py migrate

# 5. Iniciar o servidor de desenvolvimento
python manage.py runserver
