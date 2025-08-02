# CSV Explorer

A high-performance, enterprise-grade data exploration platform built with modern Python technologies. This application provides interactive data analysis capabilities through a web-based interface, designed for scalable data processing and advanced analytics workflows.

## Overview

CSV Explorer is a Streamlit-based data analytics platform that enables rapid exploration and visualization of tabular data. Built with a focus on performance, extensibility, and developer experience, it serves as a foundation for data engineering pipelines and machine learning workflows.

### Key Features

- **Interactive Data Visualization**: Powered by pygwalker for advanced charting and statistical analysis
- **Robust Data Validation**: Built-in CSV structure validation with configurable constraints
- **Memory-Optimized Processing**: Efficient handling of large datasets with pandas optimization
- **Real-Time Analytics**: Live data exploration with immediate feedback
- **Extensible Architecture**: Modular design supporting custom data processors and validators
- **Production-Ready**: Comprehensive testing framework and error handling

## Technical Architecture

### Core Components

```
├── app.py                    # Main application entry point
├── tests/                    # Comprehensive test suite
│   ├── test_app.py          # Core functionality tests
│   └── __init__.py
├── requirements.txt          # Dependency management
├── pytest.ini              # Testing configuration
└── CLAUDE.md               # Development guidelines
```

### Technology Stack

- **Frontend**: Streamlit 1.47.1 - Modern web application framework
- **Data Processing**: pandas 2.0+ - High-performance data manipulation
- **Visualization**: pygwalker 0.4+ - Interactive data exploration engine
- **Testing**: pytest with tdd-guard for continuous testing
- **Environment Management**: uv for fast, reliable dependency resolution

### Data Flow Architecture

1. **Data Ingestion**: Multi-format CSV upload with validation
2. **Processing Pipeline**: pandas-based data transformation and cleaning
3. **Validation Layer**: Configurable data quality checks
4. **Analytics Engine**: pygwalker integration for interactive exploration
5. **Visualization**: Real-time chart generation and statistical analysis

## Quick Start

### Prerequisites

- Python 3.8+
- uv package manager

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd csv-explorer

# Set up environment with uv
uv venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
uv pip install -r requirements.txt
```

### Running the Application

```bash
# Start the Streamlit server
uv run streamlit run app.py

# The application will be available at http://localhost:8501
```

### Basic Usage

1. **Upload Data**: Use the sidebar file uploader to select a CSV file
2. **Review Summary**: Examine data statistics, column types, and missing values
3. **Explore Interactively**: Use the pygwalker interface for visualization
4. **Export Results**: Generate charts and analysis for reporting

## Advanced Usage

### Data Validation

The platform includes a comprehensive validation framework:

```python
# Example: Custom validation rules
is_valid, message = validate_csv_structure(
    df, 
    min_rows=100,                    # Minimum dataset size
    required_columns=['id', 'date']  # Required column names
)
```

### Supported Validation Rules

- **Minimum Row Count**: Ensure datasets meet size requirements
- **Required Columns**: Validate presence of essential fields
- **Data Type Validation**: Automatic type inference and validation
- **Missing Value Analysis**: Comprehensive null value reporting

### Performance Optimization

For large datasets (>1GB):

```python
# Memory-efficient processing
df = pd.read_csv(file, chunksize=10000)  # Process in chunks
df.info(memory_usage='deep')             # Monitor memory usage
```

## Development Workflow

### Test-Driven Development

This project follows TDD methodology for reliable, maintainable code:

```bash
# Run tests with auto-reload
uv run tdd-guard-pytest

# Run specific test suites
uv run pytest tests/test_app.py::TestCSVValidation -v

# Run all tests
uv run pytest
```

### Development Commands

```bash
# Install new dependencies
uv add package_name
uv pip freeze > requirements.txt

# Run with hot reload
uv run streamlit run app.py --server.runOnSave true

# Code quality checks
uv run pytest --cov=app tests/
```

### Testing Framework

- **Unit Tests**: Core functionality validation
- **Integration Tests**: End-to-end workflow testing
- **Performance Tests**: Memory and speed benchmarking
- **Continuous Testing**: Auto-rerun with tdd-guard-pytest

## API Reference

### Core Functions

#### `load_csv_data(uploaded_file)`
Loads and validates CSV data from uploaded files.

**Parameters:**
- `uploaded_file`: Streamlit uploaded file object

**Returns:**
- `tuple`: (DataFrame, error_message) where error_message is None on success

#### `validate_csv_structure(df, min_rows=1, required_columns=None)`
Validates CSV structure against specified requirements.

**Parameters:**
- `df`: pandas DataFrame to validate
- `min_rows`: Minimum required row count
- `required_columns`: List of required column names

**Returns:**
- `tuple`: (is_valid, validation_message)

#### `display_data_summary(df)`
Generates comprehensive data summary with statistics and metadata.

**Parameters:**
- `df`: pandas DataFrame to analyze

## Performance Considerations

### Memory Management
- Streaming data processing for large files
- Efficient pandas operations with vectorization
- Memory usage monitoring and optimization

### Scalability
- Configurable chunk processing for large datasets
- Async data loading capabilities
- Horizontal scaling support for distributed processing

### Production Deployment
- Container-ready architecture
- Environment variable configuration
- Health check endpoints
- Logging and monitoring integration

## Contributing

### Code Standards
- Follow PEP 8 style guidelines
- Comprehensive test coverage (>90%)
- Type hints for all public functions
- Docstring documentation

### Development Process
1. Create feature branch from main
2. Implement with TDD approach
3. Ensure all tests pass
4. Submit pull request with documentation

### Testing Requirements
- Unit tests for all new functions
- Integration tests for user workflows
- Performance benchmarks for data processing
- Documentation updates for API changes

## Technology Roadmap

### Planned Enhancements
- Machine learning model integration
- Real-time data streaming support
- Advanced statistical analysis modules
- Multi-format data import (JSON, Parquet, Excel)
- API endpoints for programmatic access

### Architecture Evolution
- Microservices decomposition
- Event-driven processing pipeline
- MLOps integration capabilities
- Advanced caching and optimization

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For technical support, feature requests, or contributions, please refer to the project's issue tracker and documentation.