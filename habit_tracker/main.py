#Вариант 38. Трекер привычек
import random
from habits_data import *
random.seed(67)

def show_help():
    print("Доступные команды:")
    print("  list - список привычек")
    print("  done <номер> - отметить выполнение")
    print("  skip <номер> - пропустить привычку")
    print("  status <номер> - статистика привычки")
    print("  add <имя> - добавить привычку")
    print("  active - привычки с выполнениями")
    print("  today - выполнено сегодня")
    print("  marks - история отметок")
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
def add_habit(habits,name):
    if name in [h["name"] for h in habits]:
        return False
    habits.append({"name": name,"streak": 0,"best": 0,"total": 0})
    return True
def active_habits(habits):
    return [h["name"] for h in habits if h["total"]>0]
def habit_names_upper(habits):
    return [h["name"].upper() for h in habits]
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

def main():
    print("=== Трекер привычек ===")
    print("Введите одну из команд: help, list, status <номер>, motivation, active, today, marks add <имя>, done <номер>, skip <номер>, exit")
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
        elif cmd == "active":
            act = active_habits(HABITS)
            if act:
                print("Активные:", ", ".join(act))
            else:
                print("Пока нет привычек с выполнениями.")
        elif cmd == "today":
            if DONE_TODAY:
                print("Сегодня выполнено:", ", ".join(sorted(DONE_TODAY)))
            else:
                print("Сегодня ещё ничего не выполнено.")
        elif cmd == "marks":
            if MARKS:
                for m in MARKS:
                    print(" ", m)
            else:
                print("Отметок пока нет.")
        elif cmd == "add":
            if len(cmdidx) < 2:
                print("Укажите имя: add <имя>")
                continue
            name = " ".join(cmdidx[1:])
            if add_habit(HABITS,name):
                print(f"Привычка '{name}' добавлена.")
            else:
                print("Такая привычка уже есть.")
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
                    MARKS.append("done "+habit["name"])
                    DONE_TODAY.add(habit["name"])
                    print("Привычка выполнена.")
                    print("Текущая серия:", habit["streak"])
                    print("Лучшая серия:", habit["best"])
                elif cmd == "skip":
                    mark_skip(habit)
                    MARKS.append("skip "+habit["name"])
                    DONE_TODAY.discard(habit["name"])
                    print("Пропуск отмечен. Текущая серия сброшена.")
                    print("Текущая серия:", habit["streak"])
                    print("Лучшая серия:", habit["best"])
            else:
                print(f"Для этой команды требуется верный индекс[1-{len(HABITS)}]. Введите его через пробел после команды.")
        else:
            print("Неизвестная команда.")
            print("Доступные команды: help, list, status <номер>, motivation, active, today, marks add <имя>, done <номер>, skip <номер>, exit")

if __name__ == "__main__":
    main()
