# Copilot Instructions for M24CA1L106

This repository contains two main projects:

## 1. Python Lab Programs (M24CA1L106/)

A collection of Python programming exercises and utilities focusing on fundamental concepts.

### Key Components:

- **Graphics Package** (`graphics/`):
  - Basic geometric calculations for 2D shapes (`__init__.py`)
  - 3D shape calculations in `threeDgraphics/` submodule
  - Import pattern: `from graphics import circle, rectangle`
  - Example usage in `package.py`

### Common Patterns:

- File Operations:
  - Reading/writing text files (see `fileCopy.py`, `exp34.py`)
  - Error handling using try-except blocks for IO operations

- Input Processing:
  - Common pattern: `input().split()` for space-separated values
  - List comprehensions and lambda functions (see `exp28.py`, `exp29.py`)
  - Recursive function implementations (`exp30.py`)

## 2. React + Vite Application (WDL/My App/)

A modern React application using Vite as the build tool.

### Project Structure:
```
WDL/My App/
├── src/            # React components and assets
├── public/         # Static assets
└── package.json    # Dependencies and scripts
```

### Development Workflow:

1. **Available Scripts:**
   ```json
   "scripts": {
     "dev": "vite",      # Development server
     "build": "vite build",
     "lint": "eslint .",
     "preview": "vite preview"
   }
   ```

2. **ESLint Configuration:**
   - Custom rules in `eslint.config.js`
   - React Hooks and Refresh plugins enabled

### Component Patterns:
- Functional components with hooks (`App.jsx`)
- Array rendering with keys (`array.jsx`)
- CSS module pattern for styling

## General Guidelines

1. **Python Environment:**
   - Python 3.13 virtualenv
   - Package imports use absolute paths from project root

2. **React Development:**
   - React 19.1.1 with modern features
   - Use JSX for components
   - Follow ESLint rules defined in config