import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def front_v(data_bar, choice, summury):
    root = tk.Tk()
    root.title("Qriam")
    root.geometry("1920x1080")

    

    def print_sprint(data_bar, choice,que, right):
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
            print(color, x_l, y_l, x_l2, y_l2)
            canvas.create_rectangle(x_l +20,y_l, x_l2 +20, y_l2, fill=color, outline="")
            canvas.create_text(x_l2+20, y_l2+10, text=category, font=("Arial", 9))

            per_x += 120
            c+=1
        health = f'Задач "К выполнению" от общего объема: {sp[0]}\n\nЗадач "Снято" от общего объема: {sp[1]}\n\nИзменение бэклога: {sp[2]}'
        label = tk.Label(root, text=health, font=("Arial", 10), justify="left", anchor="w")
        label.grid(row=que+1,column= right)
        
        root.update()

    def grap():
        target_key = 'for_exect'
        values_for_print = [d[target_key] for d in data_bar]
        plt.plot(values_for_print)
        plt.xlabel('Словари')
        plt.ylabel('Значения')
        plt.title(f'График значений по ключу "{target_key}"')
        plt.show() 

    print(data_bar)
    #ГРАФИКИ
    
    


    #БАРЫ
    q = 3
    right = 0
    
    iters = 0
    for x in data_bar:
        if iters == 3:
            break
        print_sprint(x, choice, q, right)
        q +=2
        if q > 100:
            right += 1
            q = 0
        iters += 1
    
    
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(values)
    ax.set_title(f'График значений по ключу "{target_key}"')
    ax.set_xlabel('Словарь')
    ax.set_ylabel('Значение')

    button1 = tk.Button(root, text="MAIN", command=grap)
    button1.grid(row=0, column=1)

    ax.plot(x_values, y_values)

    choice = "Sprint 1"
    label = tk.Label(root, text=choice, font=("Arial", 14))
    label.grid(row=0,column=0)

    choice_temas = "Team1, Team2"
    label = tk.Label(root, text=choice_temas, font=("Arial", 14))
    label.grid(row=1, column=0)



    data_bar = ["124", '178', "123"]
    


    root.mainloop()













    
    

