package main

import (
    "log"
    "net/http"
    "os/exec"
    "runtime"
    "smart-tasks/controller"
)

func openBrowser(url string) {
    var cmd *exec.Cmd
    switch runtime.GOOS {
    case "windows":
        cmd = exec.Command("rundll32", "url.dll,FileProtocolHandler", url)
    case "darwin":
        cmd = exec.Command("open", url)
    case "linux":
        cmd = exec.Command("xdg-open", url)
    default:
        log.Fatalf("Unsupported platform")
    }
    err := cmd.Start()
    if err != nil {
        log.Fatalf("Failed to open browser: %v", err)
    }
}

func main() {
    // Настройка маршрутов
    http.HandleFunc("/", controller.ListTasks)
    http.HandleFunc("/add", controller.AddTask)
    http.HandleFunc("/complete", controller.CompleteTask)

    url := "http://localhost:8080"
    
    // Открытие браузера
    openBrowser(url)

    // Запуск сервера
    log.Println("Starting server on :8080")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatalf("Server failed to start: %v", err)
    }
}


