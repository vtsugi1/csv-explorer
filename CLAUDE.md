# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A personal project built with Streamlit for interactive CSV data exploration. This application combines Streamlit's web framework with pygwalker's visualization capabilities to create an easy-to-use tool for data analysis. Built as both a useful utility and a way to practice modern Python development patterns including Test-Driven Development.

## Development Environment

This project uses **uv** for Python environment and dependency management. All commands should be run within the uv virtual environment.

### Setup Commands
```bash
# Activate the uv virtual environment
uv venv
source .venv/bin/activate  # Linux/Mac
# OR
.venv\Scripts\activate     # Windows

# Install dependencies
uv pip install -r requirements.txt
```

### Common Development Commands
```bash
# Run the Streamlit app
uv run streamlit run app.py

# Run tests with TDD guard (auto-reruns on file changes)
uv run tdd-guard-pytest

# Run tests manually
uv run pytest

# Install new dependencies
uv add package_name
uv pip freeze > requirements.txt
```

## Architecture

### Core Components
- **app.py**: Main Streamlit application entry point
- **CSV Upload Handler**: Streamlit file uploader for CSV files with validation
- **pygwalker Integration**: Interactive data visualization and exploration interface
- **Data Processing Pipeline**: Pandas-based data loading and preprocessing
- **Error Handling**: Robust validation for malformed CSV files and data issues

### Data Flow
1. User uploads CSV file through Streamlit file uploader
2. File validation and pandas DataFrame creation
3. Data preview and summary statistics display
4. pygwalker visualization interface initialization
5. Interactive data exploration and analytics

### Key Dependencies
- **streamlit**: Web application framework for the UI
- **pygwalker**: Interactive data visualization and exploration
- **pandas**: Data manipulation and analysis
- **tdd-guard-pytest**: Test-driven development with auto-rerun

## File Structure
```
csv-explorer/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── tests/                 # Test suite
├── README.md             # Project documentation
└── CLAUDE.md             # This file
```

## Testing Strategy

Uses pytest with tdd-guard for continuous testing during development. Tests should cover:
- CSV file upload and validation
- Data processing edge cases
- pygwalker integration
- Error handling scenarios

## Development Workflow

1. Use `uv run tdd-guard-pytest` for TDD development
2. Write tests first for new features
3. Implement features to pass tests
4. Run `uv run streamlit run app.py` to test the web interface
5. Ensure all dependencies are managed through uv

## Performance Considerations

- Handle reasonably large CSV files efficiently with pandas
- Optimize pygwalker rendering for smooth user experience
- Implement proper error boundaries for file processing failures
- Focus on practical file sizes that individuals typically work with

## Project Goals

This is a personal learning project that aims to:
- Demonstrate modern Python development practices
- Create a genuinely useful tool for data exploration
- Practice Test-Driven Development methodology
- Build something that others can learn from and contribute to