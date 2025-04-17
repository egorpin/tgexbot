def get_training_plan(goal: str, level: str, equipment: str) -> str | None:
    if goal == "muscle_gain" and level == "beginner" and equipment == "dumbbells":
        return """Пример плана для набора массы (новичок, гантели):
        1. Приседания с гантелями: 3 подхода по 10-12 повторений
        2. Жим гантелей лежа: 3 подхода по 10-12 повторений
        ...
        """
    elif goal == "fat_loss" and level == "intermediate" and equipment == "no_equipment":
        return """Пример плана для сжигания жира (средний, без оборудования):
        1. Берпи: 3 подхода по 15 повторений
        2. Планка: 3 подхода по 60 секунд
        ...
        """
    return None
