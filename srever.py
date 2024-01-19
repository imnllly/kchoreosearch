from flask import Flask, render_template, redirect, abort

filters = [
    {
        "name": "Мужчина",
        "is_done": False
    },
    {
        "name": "Женщина",
        "is_done": False
    },
    {
        "name": "Один мембер",
        "is_done": False
    },
    {
        "name": "Два мембера",
        "is_done": False
    },
    {
        "name": "три и больше",
        "is_done": False
    },
]

app = Flask(__name__)
# Эта страница показывает список задач
@app.route('/')
def index():
    # Чтобы показать прогресс бар с кол-вом выполненых задач, передадим в шаблон, сколько сделано и сколько их всего
    done_count = len([task for task in filters if task['is_done']])
    count = len(filters)
    return render_template("tasks.html", tasks=filters, done_count=done_count, count=count)

# Чтобы пометить, что задача выполена, сделаем страницу /tasks/НОМЕРЗАДАЧИ/done
@app.route('/tasks/<int:id>/done')
def make_done(id):
    if id < 0 or id >= len(filters):
        abort(404)

    filters[id]["is_done"] = True

    # Поскольку у нас уже есть страница с отображением списка задач, можем просто перенаправить туда пользователя
    return redirect('/')


@app.route('/tasks/<int:id>/undone')
def make_undone(id):
    if id < 0 or id >= len(filters):
        abort(404)

    filters[id]["is_done"] = False

    return redirect('/')


app.run(debug=True)
