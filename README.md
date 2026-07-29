# 📊 GitHub User Activity CLI

A simple **Command Line Interface (CLI)** tool built in Python to fetch and display recent activity of any GitHub user.  
This project is inspired by the [roadmap.sh GitHub User Activity project](https://roadmap.sh/projects/github-user-activity) and is designed to help beginners practice working with APIs, JSON data, and CLI applications.

---

## 📖 Overview
The GitHub User Activity CLI lets you:
- Fetch recent events of any GitHub user using the GitHub REST API
- Display event type, repository name, and timestamp
- Handle errors gracefully (invalid user, API limits)
- Extend functionality to fetch commits directly from repositories

---

## ⚙️ Features
- **Fetch user activity** (`PushEvent`, `WatchEvent`, `ForkEvent`, etc.)
- **Show repo name and timestamp**
- **Limit output** (e.g., show only 10 latest events)
- **Error handling** for invalid usernames or API issues
- **Optional authentication** with a GitHub token for higher rate limits

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <(https://github.com/HimanshuBhamaniya/gtihub-activity.git)>
cd github-activity
