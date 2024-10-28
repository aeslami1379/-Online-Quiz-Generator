# Quiz Application

This project is a command-line and server-based Quiz Application, designed to support various quiz modes, persistence options, and templating. The application allows users to interact via the REPL, a simple web interface, and JSON or plain text for data storage.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Running in REPL Mode](#running-in-repl-mode)
  - [Running the Web Server](#running-the-web-server)
- [Project Structure](#project-structure)

## Features

- **Multiple Persistence Options**: Supports both JSON and plain text for saving quiz data.
- **REPL Interface**: A command-line REPL interface for taking quizzes.
- **Web Server Support**: Built-in server using Bottle for a web-based quiz experience.
- **Templating**: Flexible templating for customizing quiz output.
  
## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/quiz-application.git
   cd quiz-application

## Usage
**Running in REPL Mode**

To start the quiz in REPL mode:

```bash

python quizREPL.py
```
**Running the Web Server**

To launch the web server and access the quiz via a browser:

```bash

python quizserver.py
```
Once the server is running, open a browser and navigate to http://localhost:8080 to start the quiz.

## Project Structure

  - persist_json.py: Manages data persistence using JSON files.
  - persist_ptext.py: Handles data persistence in plain text format.
  - quiz.py: Core logic for quiz management, including question handling and scoring.
  - quiz_templating.py: Templating functionality for customizing quiz displays.
  - quizBottle.py: Integrates the quiz with a Bottle server for web access.
  - quizREPL.py: Launches a command-line REPL for users to take quizzes.
  - quizserver.py: Main server script to run the quiz application as a web service.
  
