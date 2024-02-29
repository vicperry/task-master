class Task:
    def __init__(self, id: int, description: str, done: bool = False):
        self.id = id
        self.description = description
        self.done = done
    def __str__(self):
        return f"Tarefa {self.id}: {self.description}. Concluída: {self.done}."

tasks = []

def create_task(description: str):
  """
  Função para criar uma nova tarefa.

  :param description: Descrição da tarefa a ser criada.
  """
  task = Task(id=len(tasks) + 1, description=description)
  tasks.append(task)
  print("Tarefa criada com sucesso.")

def list_tasks():
  """
  Função para listar todas as tarefas da lista.

  """
  print(tasks)

def remove_task(task_id: int):
  """
  Função para remover uma tarefa da lista com base no índice.

  :param task_id: ID da tarefa a ser removida.
  """
  for task in tasks:
    if task.id == task_id:
      tasks.remove(task)
      print(f"Tarefa {task_id} removida.")
      return
    print(f"Tarefa com ID {tasks.id} não encontrada.")

def mark_task_done(task_id: int):
  """
  Função para marcar tarefa como concluída.

  :param task_id: ID da tarefa a ser marcada como concluída.
  """
  tasks[task_id - 1].done = True
  print(f"Tarefa {task_id} marcada como concluída.")

def show_menu():
  """
  Função para exibir menu de opções.

  :param option: Opção escolhida pelo usuário.
  """
  print("Task Master: Escolha uma opção. \n1- Criar tarefa. \n2- Listar tarefas. \n3- Remover tarefa. \n4- Marcar tarefa como concluída.\n")
  option = input("Digite a opção desejada: ")
  if option == "1":
    description = input("Digite a descrição da tarefa: ")
    create_task(description)
  if option == "2":
    list_tasks()
  if option == "3":
    task_id = int(input("Digite o ID da tarefa a ser removida: "))
    remove_task(task_id)
  if option == "4":
    task_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
    mark_task_done(task_id)

show_menu()
  
  


