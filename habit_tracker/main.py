#Вариант 38. Трекер привычек
import random
from habits_data import *

def show_help():
    print("Доступные команды:")
    print("  list - список привычек")
    print("  done <номер> - отметить выполнение")
    print("  skip <номер> - пропустить привычку")
    print("  status <номер> - статистика привычки")
    print("  motivation - случайная мотивация")
    print("  help - эта справка")
    print("  exit - выход")
def mark_done(habit):
    habit["streak"] += 1
    habit["total"] += 1
    if habit["streak"]> habit["best"]:
        habit["best"] = habit["streak"]
def mark_skip(habit):
    habit["streak"] =0
def random_motivation():
    print(random.choice(MOTIVATIONS))
def print_habits():
    if not HABITS:
        print("Список привычек пуст.")
        return
    print("Ваши привычки:")
    i = 1
    for habit in HABITS:
        print(f"{i}. {habit['name']}" 
              f"(серия: {habit['streak']}, лучшая: {habit['best']},всего: {habit['total']})")
        i += 1
def find_idx(parts):
    if len(parts) < 2:
        return -1
    try:
        return int(parts[1])
    except ValueError:
        return -1

print("=== Трекер привычек ===")
print("Введите одну из команд: help, list, status, motivation, done, skip, exit")
while True:
    cmdidx = input().strip().lower().split()
    if not cmdidx:
        print("Строка пустая.")
        continue
    cmd = cmdidx[0]
    if cmd == "help":
        show_help()
    elif cmd == "list":
        print_habits()
    elif cmd == "motivation":
        random_motivation()
    elif cmd == "exit":
        print("Выход из трекера. До встречи!")
        break
    elif cmd in ("status","done", "skip"):
        idx = find_idx(cmdidx)
        if not(idx < 1 or idx > len(HABITS)):
            habit = HABITS[idx-1]
            if cmd == "status": 
                print("Привычка:", habit["name"])
                print("Текущая серия:", habit["streak"])
                print("Лучшая серия:", habit["best"])
                print("Всего выполнений:", habit["total"])
            elif cmd =="done":
                mark_done(habit)
                print("Привычка выполнена.")
                print("Текущая серия:", habit["streak"])
                print("Лучшая серия:", habit["best"])
            elif cmd == "skip":
                mark_skip(habit)
                print("Пропуск отмечен. Текущая серия сброшена.")
                print("Текущая серия:", habit["streak"])
                print("Лучшая серия:", habit["best"])
        else:
            print("Для этой команды требуется верный индекс[1-3]. Введите его через пробел после команды.")
    else:
        print("Неизвестная команда.")
        print("Доступные команды: help, list, status, motivation, done, skip, exit")