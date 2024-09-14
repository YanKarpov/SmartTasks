package controller

import (
    "html/template"
    "net/http"
    "strconv"
    "smart-tasks/model"
)

func ListTasks(w http.ResponseWriter, r *http.Request) {
    tasks := model.GetTasks()
    tmpl := template.Must(template.ParseFiles("view/template.html"))
    tmpl.Execute(w, tasks)
}

func AddTask(w http.ResponseWriter, r *http.Request) {
    if r.Method == http.MethodPost {
        title := r.FormValue("title")
        model.AddTask(title)
        http.Redirect(w, r, "/", http.StatusSeeOther)
    }
}

func CompleteTask(w http.ResponseWriter, r *http.Request) {
    idStr := r.URL.Query().Get("id")
    id, err := strconv.Atoi(idStr)
    if err != nil {
        http.Error(w, "Invalid ID", http.StatusBadRequest)
        return
    }
    model.CompleteTask(id)
    http.Redirect(w, r, "/", http.StatusSeeOther)
}
