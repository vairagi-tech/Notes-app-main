# Notes App

This is a simple notes application built with a React frontend and an Express/MongoDB backend. Users can register, log in, create, edit, and delete notes.

## Live Demo

The application is live at the following link:

[https://notes-app-jpyr.vercel.app/](https://notes-app-jpyr.vercel.app/)

## Features

- User authentication (register and login)
- Create, edit, and delete notes
- Search notes
- Responsive design

## Technologies Used

### Frontend

- React
- React Router
- Axios
- CSS

### Backend

- Express
- MongoDB
- Mongoose
- JWT (JSON Web Tokens)
- bcryptjs

## Getting Started

### Prerequisites

- Node.js
- MongoDB

### Installation

1. Clone the repository:

```sh
git clone https://github.com/your-username/notes-app.git
cd notes-app

### Install dependencies for the backend:
cd NotesApp_project/Notes-App-main/notes-app-backend
npm install

##  Install dependencies for the frontend:

cd ../../
npm install

# Running the Application
# Start the backend server:

cd NotesApp_project/Notes-App-main/notes-app-backend
npm start

# Start the frontend development server:

cd ../../
npm start

# The application should now be running on http://localhost:3000.

# Project Structure

Notes-app-main/
    NotesApp_project/
        Notes-App-main/
            .gitignore
            notes-app-backend/
                .gitignore
                models/
                    Note.js
                    User.js
                package.json
                routes/
                    auth.js
                    notes.js
                server.js
            package.json
            public/
                index.html
                manifest.json
                robots.txt
            src/
                App.css
                App.js
                App.test.js
                components/
                    Loader.css
                    Loader.js
                    LoginPage.css
                    ...
                index.css
                index.js
                reportWebVitals.js
                setupTests.js
        README.md


# Contributing
Contributions are welcome! Please open an issue or submit a pull request.

# License
This project is licensed under the MIT License.

