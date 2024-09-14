package model

import "sync"

type Task struct {
    ID        int    `json:"id"`
    Title     string `json:"title"`
    Completed bool   `json:"completed"`
}

var (
    tasks = []Task{}
    idCounter = 1
    mu sync.Mutex
)

func AddTask(title string) Task {
    mu.Lock()
    defer mu.Unlock()
    task := Task{ID: idCounter, Title: title, Completed: false}
    idCounter++
    tasks = append(tasks, task)
    return task
}

func GetTasks() []Task {
    mu.Lock()
    defer mu.Unlock()
    return tasks
}

func CompleteTask(id int) {
    mu.Lock()
    defer mu.Unlock()
    for i, task := range tasks {
        if task.ID == id {
            tasks[i].Completed = true
            break
        }
    }
}
