#open the file 
with open("hr_system.txt") as systems:
    next(systems)
    for line in systems:
        worker = line.split(" ")

        name = worker[0]
        id = int(worker[1])
        title = worker[2]
        salary = float(worker[3])
        p_salary = salary/2

        if title == "Engineer":
          pc_salary =  p_salary + 1000
        else :
          pc_salary = p_salary
        print(f"{name} (ID: {id}), {title} - ${pc_salary:.2f}")



