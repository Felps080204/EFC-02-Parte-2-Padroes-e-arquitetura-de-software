# Felipe Larrocca dos Santos - 23013864
# Pedro Henrique Bertochi Sousa – 23013915

# RESUMO TÉCNICO – Padrões de Projeto (Parte 2)

Este documento apresenta o estudo, análise e justificativa da aplicação de quatro padrões de projeto implementados no sistema NotesPlus, desenvolvido em Python. Os padrões escolhidos foram estudados na plataforma Refactoring.Guru e aplicados de forma prática na construção da aplicação.

---

# 1. Padrões de Projeto Estudados e Implementados

Os padrões selecionados pertencem a três categorias diferentes:

- **Criacional**: Singleton, Factory Method  
- **Estrutural**: (não utilizado, por decisão arquitetural)  
- **Comportamental**: Strategy, Observer  

**Criacionais**
Responsáveis por controlar a forma como os objetos são criados.

**Singleton**
Garante uma única instância de uma classe que é globalmente acessível.
No projeto, isso é útil para controlar todas as notas em um único ponto central.

Estrutura:
- Uma classe que armazena internamente a própria instância.
- Construtor privado ou controlado.
- Método estático que retorna sempre a mesma instância criada.

Quando utilizar
- Quando o sistema precisa de um único gerenciador central (ex.: gerenciador de notas, configurações, conexões).
- Quando múltiplas instâncias causariam inconsistências ou duplicação de dados.
- Quando é necessário compartilhar um estado global.

**Factory Method**
Definir uma interface para criar objetos, permitindo que subclasses decidam qual classe concreta será instanciada, evitando acoplamento direto, facilitando expansões.
No NotesPlus, novas notas podem ser criadas facilmente sem alterar o restante da aplicação.

Esses padrões lidam com como objetos são instanciados e como o sistema mantém ordem ao criar novos elementos.

Estrutura:
- Uma interface ou classe base com o método fábrica.
- Subclasses implementam esse método para retornar diferentes tipos de objetos.
- Cliente usa o método fábrica sem conhecer o tipo concreto.

Quando utilizar:
- Quando o código precisa criar objetos, mas não deve depender de suas classes concretas.
- Quando existem múltiplas variações de um mesmo tipo de objeto (ex.: diferentes tipos de notas).
- Quando o sistema deve ser extensível, permitindo adicionar novos tipos sem alterar o código existente.

**Estruturais**
Focados na forma como classes e objetos se organizam entre si.
Não foram utilizados neste projeto por decisão arquitetural.
A decisão de não incluir um padrão estrutural foi tomada porque:

- A aplicação já tinha uma estrutura simples e modular.
- A introdução de um padrão estrutural poderia complicar desnecessariamente o código.
- Os requisitos não demandavam composição ou adaptação de estruturas complexas.

Ainda assim, padrões estruturais como Adapter, Composite ou Decorator são excelentes para cenários em que objetos precisam trabalhar juntos de forma mais complexa.

**Comportamentais**
Cuidam da comunicação e do comportamento entre objetos, adicionando flexibilidade ao sistema.

**Strategy**
Permite alternar algoritmos de exportação sem modificar o código da nota.
Cada formato (JSON, Markdown, Texto) é implementado como uma estratégia separada.

Estrutura:
- Interface comum para os algoritmos (estratégias).
- Múltiplas implementações dessa interface.
- Um "contexto" que utiliza dinamicamente uma das estratégias.

Quando utilizar:
- Quando há diferentes formas de realizar uma operação, mas sem querer encher o código de condicionais.
- Quando o comportamento deve ser intercambiável (ex.: exportar em JSON, Markdown ou TXT).
- Quando é importante seguir o princípio Aberto/Fechado (OCP).

**Observer**
Criar um mecanismo no qual vários objetos (observadores) são notificados automaticamente quando ocorre um evento em outro objeto (sujeito).

Permite que o sistema reaja automaticamente a eventos, como a criação de notas.
Com ele, o NoteManager notifica loggers e sistemas de notificação sem acoplamento direto.

Estrutura:
- Um "Subject" que mantém uma lista de observadores.
- Observadores que implementam uma interface de notificação.
- Chamadas automáticas aos observadores quando um evento ocorre.

Quando utilizar:
- Quando vários componentes precisam reagir ao mesmo evento.
- Quando se deseja reduzir acoplamento entre módulos.
- Quando funcionalidades adicionais devem ser adicionadas sem modificar o núcleo do sistema (ex.: logs, alertas, notificações automáticas).

Esses padrões foram essenciais para:
- deixar o NotesPlus extensível;
- adicionar funcionalidades sem tocar no código já existente;
- permitir reações automáticas a ações do usuário (criação de notas).

A seguir, cada padrão é explicado em profundidade, incluindo sua aplicação no projeto e respectiva justificativa.

-----

# 2. Análise Individual dos Padrões

## 2.1 Singleton

### **Propósito**
Garantir que uma classe tenha uma única instância global, fornecendo um ponto de acesso centralizado.

### **Aplicação no Projeto**
Aplicado na classe `NoteManager`, responsável por:
- Armazenar todas as notas criadas
- Registrar observadores
- Notificar eventos
- Centralizar exportações

### **Por que foi escolhido**
A aplicação necessita de uma única fonte de verdade para todas as notas criadas. Múltiplas instâncias resultariam em inconsistências, dificultando o gerenciamento e sincronização.

### **Problema que resolve**
Evita a criação de múltiplos gerenciadores de notas e mantém o estado centralizado.

### **Benefícios**
- Organização global
- Evita duplicação de dados
- Facilita manutenção e controle

### **Como seria sem o padrão**
Haveria diversas listas de notas espalhadas pela aplicação, tornando o sistema difícil de escalonar e manter.

-----

## 2.2 Factory Method

### **Propósito**
Fornecer uma interface para criar objetos, permitindo que subclasses decidam qual classe concreta instanciar.

### **Aplicação no Projeto**
A classe `NoteFactory` cria:
- `TextNote`
- `ListNote`
- `ChecklistNote`

### **Por que foi escolhido**
Evita o uso de condicionais e instâncias “na mão” (`new`/instanciação direta) no código principal.

### **Problema que resolve**
Remove o acoplamento direto entre o sistema e suas classes concretas de notas.

### **Benefícios**
- Extensível (fácil adicionar novas notas)
- Mantém o código limpo
- Facilita testes

### **Como seria sem o padrão**
O `main.py` teria vários `if/elif` para instanciar tipos diferentes, tornando o código rígido.

-----

## 2.3 Strategy

### **Propósito**
Permitir que algoritmos possam ser trocados dinamicamente sem modificar o código cliente.

### **Aplicação no Projeto**
Usado para exportar notas em diferentes formatos:
- JSON (`ExportJSON`)
- Markdown (`ExportMarkdown`)
- Texto (`ExportText`)

### **Por que foi escolhido**
A exportação possui múltiplas versões, mas a lógica da nota não deveria saber disso. Assim, cada formato é apenas uma estratégia independente.

### **Problema que resolve**
Evita um método cheio de condicionais para exportar notas.

### **Benefícios**
- Código limpo
- Separação clara de responsabilidades
- Facilidade para adicionar novos formatos

### **Como seria sem o padrão**
Uma função enorme com `if formato == ...`, difícil de expandir.

-----

## 2.4 Observer

### **Propósito**
Permitir que objetos dependentes sejam automaticamente notificados quando um evento ocorre.

### **Aplicação no Projeto**
Usado para:
- Logar criação de notas (`LoggerObserver`)
- Enviar notificações (`NotificationObserver`)

### **Por que foi escolhido**
Diversas funcionalidades deveriam reagir ao evento de “nota criada”, mas sem acoplamento entre módulos.

### **Problema que resolve**
Evita chamadas diretas e dependências fortes entre componentes.

### **Benefícios**
- Baixo acoplamento
- Alta extensibilidade
- Reutilização de código

### **Como seria sem o padrão**
O `NoteManager` chamaria manualmente cada função dependente, dificultando futuras expansões.

-----

# 3. Comparação dos Padrões

# 3.1 Semelhanças
- Baixo acoplamento: todos os padrões promovem a redução de dependências diretas entre componentes.
- Alta coesão: cada classe tem um papel bem definido (ex.: Strategy cuida apenas da exportação, Factory apenas da criação).
- Facilidade de extensão: novos tipos de notas (via Factory), novos formatos de exportação (via Strategy) e novos observadores (via Observer) podem ser adicionados sem modificar o núcleo da aplicação.
- Encorajam boas práticas de design como o Open/Closed Principle e Single Responsibility Principle.

# 3.2 Papel no projeto e como agem na aplicação
| Padrão        | Categoria        | Papel no Projeto                                 |
|---------------|------------------|--------------------------------------------------|
| Singleton     | Criacional       | Controla instância global de notas              |
| Factory Method| Criacional       | Cria tipos de notas de forma flexível           |
| Strategy      | Comportamental   | Permite diferentes formas de exportação         |
| Observer      | Comportamental   | Notifica eventos automaticamente                |

Os padrões trabalham juntos para criar um sistema flexível, escalável e organizado.

**Singleton**: Foco principal: Gerenciamento de instâncias. Garante um único NoteManager centralizando tudo

**Factory Method**: Foco principal: Criação de objetos. Define como novos tipos de notas são criados

**Strategy**: Foco principal: Substituição de algoritmos. Permite escolher dinamicamente o tipo de exportação

**Observer**: Foco principal: Comunicação entre objetos. Permite reagir automaticamente a eventos, sem acoplamento

# 3.3 Combinações Possíveis entre os Padrões

**Singleton + Observer**
O Singleton (NoteManager) funciona como sujeito central para notificação de eventos.
Combinação natural: só existe um objeto notificando todos os observadores.

- Evita múltiplas listas de observadores contradizentes
- Simplifica a comunicação global

**Factory Method + Strategy**
A Factory cria notas sem acoplamento ao tipo concreto, e o Strategy exporta essas notas em diferentes formatos.
Eles se combinam para:
- Permitir criar diversos tipos de notas
- Exportá-las independentemente, sem modificar o código da nota

**Observer + Strategy**
O Observer pode, por exemplo:
- Acionar uma exportação automática
- Registrar logs sobre estratégias usadas
- Enviar notificações quando uma nota foi exportada
Esses padrões podem se complementar para processos monitorados e configuráveis.

Todos os quatro padrões juntos formam uma arquitetura completa porque cada um cumpre um papel específico:
- Factory Method cria objetos flexivelmente
- Singleton controla onde esses objetos ficam armazenados
- Observer reage a eventos gerados por eles
- Strategy define como eles podem ser exportados
Essa cooperação reduz a complexidade e facilita futuras expansões.

-----

# 4. Conclusão

Os quatro padrões escolhidos demonstraram alta coerência com as necessidades do sistema NotesPlus.  
Eles possibilitaram:
- Baixo acoplamento  
- Extensibilidade  
- Código limpo e coeso  
- Boa separação de responsabilidades  

A aplicação prática reforça o entendimento teórico estudado na plataforma Refactoring.Guru e demonstra sua utilidade real no desenvolvimento de sistemas organizados e de fácil manutenção.

