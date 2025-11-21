# Felipe Larrocca dos Santos - 23013864
# Pedro Henrique Bertochi Sousa – 23013915

# NotesPlus  
Sistema de organização de tarefas e listas com Aplicação de Padrões de Projeto  

Este projeto foi desenvolvido como parte da atividade "Padrões de Projeto - Parte 2", utilizando Python e incorporando quatro padrões de projeto estudados na plataforma Refactoring.Guru.

A aplicação permite o usuário gerenciar tarefas de forma simples e eficiente, oferecendo recursos para criar notas individuais, criar listas de tarefas, adicionar e remover itens em listas, além de exportar e acompanhar eventos internos através dos padrões implementados.

---

## Objetivos do Projeto
- Demonstrar o uso prático de pelo menos 4 padrões de projeto.
- Criar uma aplicação funcional e organizada.
- Fornecer justificativas técnicas claras para cada padrão utilizado.
- Estruturar um repositório bem documentado e fácil de executar.

---

## Padrões de Projeto Utilizados

### 1. Singleton  
Utilizado no `NoteManager` para garantir uma única instância global responsável por gerenciar notas e observadores.

### 2. Factory Method  
Usado na `NoteFactory` para criar diferentes tipos de notas sem acoplamento direto às classes concretas.

### 3. Strategy  
Aplicado no sistema de exportação de notas, permitindo exportar em:
- JSON  
- Markdown  
- Texto simples  

### 4. Observer  
Usado para registrar observadores (como logger e notificações) que são automaticamente ativados quando uma nota é criada.

---

## Estrutura do Projeto

notesplus/
├── src/
│ ├── main.py
│ ├── patterns/
│ │ ├── singleton.py
│ │ ├── factory.py
│ │ ├── strategy.py
│ │ └── observer.py
│ ├── models/
│ │ ├── note.py
│ │ └── note_types.py
│ └── services/
│ └── note_manager.py
├── README.md
└── RESUMO.md


---

## Como Executar

1. Certifique-se de que Python 3.x está instalado.  
2. No terminal, navegue até a pasta do projeto e execute: python src/main.py


3. O sistema irá:
- Criar notas
- Notificar observadores
- Exportar notas em diferentes formatos

---

## Funcionalidades da Aplicação

- Criar notas de diferentes tipos:
  - Texto  
  - Lista  
  - Checklist  
- Gerenciar todas as notas através de uma instância única (Singleton)
- Exportar notas em múltiplos formatos (Strategy)
- Receber notificações automáticas ao criar notas (Observer)

---

## Documento de Resumo  
O arquivo `RESUMO.md` contém:
- Explicações teóricas dos padrões de projeto utilizados  
- Aplicações práticas no código  
- Justificativas detalhadas para cada escolha arquitetural  

---

## Desenvolvedores  
Projeto desenvolvido para fins acadêmicos na disciplina de Padrões e Arquitetura de Software.  


