def get_preferred_option(task_1, task_2):

    if task_1 == "Wash the dishes":
        if task_2 == "Cook dinner" or task_2 == "Wash clothes":
            return task_1
        elif task_2 == "Clean windows" or task_2 == "Do ironing":
            return task_2

    if task_1 == "Cook dinner":
        if task_2 == "Clean windows" or task_2 == "Do ironing":
            return task_1
        elif task_2 == "Wash the dishes" or task_2 == "Wash clothes":
            return task_2
    
    if task_1 == "Clean windows":
        if task_2 == "Wash the dishes" or task_2 == "Do ironing":
            return task_1
        elif task_2 == "Cook dinner" or task_2 == "Wash clothes":
            return task_2

    if task_1 == "Do ironing":
        if task_2 == "Wash the dishes" or task_2 == "Wash clothes":
            return task_1
        elif task_2 == "Cook dinner" or task_2 == "Clean windows":
            return task_2

    if task_1 == "Wash clothes":
        if task_2 == "Cook dinner" or task_2 == "Clean windows":
            return task_1
        elif task_2 == "Do ironing" or task_2 == "Wash the dishes":
            return task_2
    





    # if task_1 == "Wash the dishes" and task_2 == "Cook dinner":
    #     return task_1
    # elif task_1 == "Clean windows" and task_2 == "Wash the dishes":
    #     return task_1
    # elif task_1 == "Clean windows"
    # elif task_1 == "Cook dinner" and task_2 == "Clean windows":
    #     return task_1
    # elif task_1 == "Wash the dishes" and task_2 == "Clean windows":
    #     return task_2
    # else:
    #     return "What???"