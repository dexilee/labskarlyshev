#Вариант 38. Трекер привычек
print("=== Трекер привычек ===")
print("Введите одну из команд: done, skip, status, exit")
streak = best = total = 0
while True:
    command = input().strip().lower()
    if command =="done":
        streak += 1
        total += 1
        if streak > best:
            best = streak
        print("Привычка выполнена.")
        print("Текущая серия:", streak)
        print("Лучшая серия:",best)
    elif command == "skip":
        streak = 0
        print("Пропуск отмечен. Текущая серия сброшена.")
        print("Текущая серия:", streak)
        print("Лучшая серия:", best)
    elif command == "status":
        print("Текущая серия:", streak)
        print("Лучшая серия:", best)
        print("Всего выполнений:", total)
    elif command == "exit":
        print("Выход из трекера. До встречи!")
        break
    else:
        print("Неизвестная команда.")
        print("Доступные команды: done, skip, status, exit")