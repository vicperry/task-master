class Task:
    def __init__(self, id: int, description: str, done: bool = False):
        self.id = id
        self.description = description
        self.done = done
    def __str__(self):
        if self.done is False:
          return f"Tarefa #{self.id}: {self.description}. \nStatus: a fazer."
        else:
          return f"Tarefa #{self.id}: {self.description}. \nStatus: concluída."

tasks = []

def create_task(description: str):
  """
  Função para criar uma nova tarefa.

  :param description: Descrição da tarefa a ser criada.
  """
  id = len(tasks) + 1
  for task in tasks:
    if task.id == id:
      id = id + 1
  task = Task(id, description)
  tasks.append(task)
  print("Tarefa criada com sucesso.")

def list_tasks():
  """
  Função para listar todas as tarefas da lista.

  """
  if len(tasks) > 0:
    for task in tasks:
      print(task)
  else:
    print("Não há tarefas na lista.")

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
  print(f"Tarefa com ID {task_id} não encontrada.")

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
  """
  while True:
      print("\nTask Master: Escolha uma opção. \n1- Criar tarefa. \n2- Listar tarefas. \n3- Remover tarefa. \n4- Marcar tarefa como concluída.\n")
      option = input("Digite a opção desejada: ")
    
      if option == "1":
          description = input("Digite a descrição da tarefa: ")
          create_task(description)
      elif option == "2":
          list_tasks()
      elif option == "3":
          task_id = int(input("Digite o ID da tarefa a ser removida: "))
          remove_task(task_id)
      elif option == "4":
          task_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
          mark_task_done(task_id)
      else:
          print("Opção inválida. Por favor, digite uma opção válida.")

show_menu()
  
  


