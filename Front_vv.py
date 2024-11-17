import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def front_v(data_bar, choice, summury):
    root = tk.Tk()
    root.title("Qriam")
    root.geometry("1920x1080")

        

    def print_sprint(data_bar, choice,que, right, summery):
        data_bar.pop("backlog_change")
        sp = list(data_bar.values())
        for k,v in data_bar.items():
            data_bar[k] = round(v/100, 2)

        canvas_width = 500
        canvas_height = 150

        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        canvas.grid(row = que, column= right)

        # Рассчитываем координаты прямоугольников
        per_x = 20
        per_y = 110
        c= 0
            # Функция для расчета размеров прямоугольников
        def calculate_rectangles(data, canvas_width, canvas_height):
            total = sum(data.values())
            rectangles = []
            x = 0
            for category, value in data_bar.items():
                width = value * canvas_width
                height = 100
                rectangles.append((category, x, 0, x + width, height))
                x += width
            return rectangles

        rectangles_mean = calculate_rectangles(data_bar, canvas_width, canvas_height)

        colors = {
        "for_exect": "#f4a261",
        "in_work": "#e9c46a",
        "done": "#2a9d8f",
        "removed": "#e76f51"
        }

        # Рисуем прямоугольники и легедну
        for rectangle in rectangles_mean:
            
            category, x1, y1, x2, y2 = rectangle
            color = colors[category]
            canvas.create_rectangle(x1, y1+50, x2, y2, fill=color, outline="")

            center_x = x1 + (x2-x1) / 2
            center_y = (y1+50)+ (y2- y1) / 2
            #canvas.create_text(center_x, center_y, text=per_scent[c], font=("Arial", 16))


            x_l, y_l = per_x, per_y

            x_l2, y_l2 = x_l + 10, y_l + 10

            color = colors[rectangle[0]]

            canvas.create_rectangle(x_l +20,y_l, x_l2 +20, y_l2, fill=color, outline="")
            canvas.create_text(x_l2+20, y_l2+10, text=category, font=("Arial", 9))

            per_x += 120
            c+=1
        health = f'Задач "К выполнению" от общего объема: {summery["for_exect"]}\n\nЗадач "Снято" от общего объема: {summery["removed"]}\n\nИзменение бэклога: {summery["backlog_change"]}'
        label = tk.Label(root, text=health, font=("Arial", 10), justify="left", anchor="w")
        label.grid(row=que+1,column= right)
        
        root.update()

    def grap():
        pass




    #ГРАФИКИ
    target_key = 'for_exect'
    values_for_print = [d[target_key] for d in data_bar]
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(values_for_print)
    ax.set_title(f'График значений по ключу "{target_key}"')
    ax.set_xlabel('Спринты начиная с 0')
    ax.set_ylabel('Значение')
    canvas1 = FigureCanvasTkAgg(fig, master=root)
    canvas1.draw()
    canvas1.get_tk_widget().place(relx=1.0, rely=0.0, anchor="ne")

    target_key = 'done'
    values_for_print = [d[target_key] for d in data_bar]
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(values_for_print)
    ax.set_title(f'График значений по ключу "{target_key}"')
    ax.set_xlabel('Спринты начиная с 0')
    ax.set_ylabel('Значение')
    canvas1 = FigureCanvasTkAgg(fig, master=root)
    canvas1.draw()
    canvas1.get_tk_widget().place(relx=0.7, rely=0.0, anchor="ne")

    target_key = 'in_work'
    values_for_print = [d[target_key] for d in data_bar]
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(values_for_print)
    ax.set_title(f'График значений по ключу "{target_key}"')
    ax.set_xlabel('Спринты начиная с 0')
    ax.set_ylabel('Значение')
    canvas1 = FigureCanvasTkAgg(fig, master=root)
    canvas1.draw()
    canvas1.get_tk_widget().place(relx=0.7, rely=0.45, anchor="ne")

    target_key = 'removed'
    values_for_print = [d[target_key] for d in data_bar]
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(values_for_print)
    ax.set_title(f'График значений по ключу "{target_key}"')
    ax.set_xlabel('Спринты начиная с 0')
    ax.set_ylabel('Значение')
    canvas1 = FigureCanvasTkAgg(fig, master=root)
    canvas1.draw()
    canvas1.get_tk_widget().place(relx=1.0, rely=0.45, anchor="ne")
    
    


    #БАРЫ
    q = 3
    right = 0
    
    iters = 0
    for x in data_bar:
        if iters == 3:
            break
        print_sprint(x, choice, q, right, summury[iters])
        q +=2
        if q > 100:
            right += 1
            q = 0
        iters += 1



    choice = "Sprint 1"
    label = tk.Label(root, text=choice, font=("Arial", 14))
    label.grid(row=0,column=0)

    choice_temas = "Team1, Team2"
    label = tk.Label(root, text=choice_temas, font=("Arial", 14))
    label.grid(row=1, column=0)



    
    



    root.mainloop()













    
    

