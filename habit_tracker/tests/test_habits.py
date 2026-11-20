from main import mark_done, mark_skip, add_habit, active_habits, habit_names_upper

def test_mark_done():
    habit = {"name":"бег","streak":2,"best":5,"total":10}
    mark_done(habit)
    assert habit["streak"] == 3
    assert habit["total"] == 11
    assert habit["best"]== 5

def test_mark_done_record():
    habit = {"name":"бег","streak":5,"best":5,"total":20}
    mark_done(habit)
    assert habit["best"] == 6

def test_mark_skip():
    habit = {"name":"бег","streak":7,"best":10,"total":15}
    mark_skip(habit)
    assert habit["streak"] == 0
    assert habit["best"] == 10
    assert habit["total"] == 15

def test_add_habit():
    habits = []
    assert add_habit(habits,"плавание") == True
    assert habits[0]["name"] == "плавание"
    assert habits[0]["total"] ==0

def test_add_habit_double():
    habits = [{"name":"бег","streak":1,"best":3,"total":8}]
    assert add_habit(habits,"бег") == False
    assert len(habits) == 1
    assert habits[0]["total"]== 8

def test_active_habits():
    habits = [
        {"name":"бег","streak":0,"best":5,"total":5},
        {"name":"чтение","streak":0,"best":0,"total":0},
    ]
    assert active_habits(habits) == ["бег"]
    assert active_habits([]) == []

def test_generators():
    habits = [{"name":"бег","streak":0,"best":0,"total":1}]
    assert habit_names_upper(habits) == ["БЕГ"]