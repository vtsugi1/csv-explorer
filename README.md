# CSV Explorer

An interactive CSV data exploration tool built with Streamlit and pygwalker. This project makes it easy to upload, analyze, and visualize your CSV data through a clean web interface, perfect for quick data insights and exploratory data analysis.

## What is this?

CSV Explorer is a personal project that combines the power of Streamlit's web framework with pygwalker's interactive visualization capabilities. Whether you're a data analyst, researcher, or just curious about your data, this tool helps you understand your CSV files quickly without writing any code.

I built this as a way to explore modern Python development practices while creating something genuinely useful for everyday data exploration tasks.

### Why I built this

- Quick data exploration shouldn't require complex setup or coding
- Interactive visualizations help uncover insights faster than static charts
- Wanted to practice Test-Driven Development with a real project
- Streamlit + pygwalker is a powerful combination that deserves more attention

## Features

- **Drag & Drop CSV Upload**: Simply upload your CSV file and start exploring
- **Automatic Data Summary**: Instantly see row counts, column types, and missing values
- **Interactive Visualizations**: Create charts and graphs with pygwalker's intuitive interface
- **Data Validation**: Built-in checks to ensure your data loads correctly
- **Responsive Design**: Works well on different screen sizes
- **Sample Data**: Try it out immediately with built-in sample data

## Quick Start

### Prerequisites

- Python 3.8 or higher
- [uv](https://docs.astral.sh/uv/) for dependency management (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/csv-explorer.git
cd csv-explorer

# Set up environment with uv (recommended)
uv venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
uv pip install -r requirements.txt
```

### Running the Application

```bash
# Start the app
uv run streamlit run app.py

# Open your browser to http://localhost:8501
```

That's it! Upload a CSV file or try the sample data to get started.

## How to Use

1. **Upload your CSV**: Use the file uploader in the sidebar
2. **Review the summary**: Check data types, missing values, and basic statistics
3. **Explore visually**: Use the interactive pygwalker interface to create charts
4. **Export insights**: Save visualizations or copy data for further analysis

## Project Structure

```
csv-explorer/
├── app.py              # Main Streamlit application
├── tests/              # Test suite with pytest
├── requirements.txt    # Python dependencies
├── pytest.ini        # Test configuration
└── README.md          # This file
```

## Development

This project follows Test-Driven Development (TDD) practices. If you want to contribute or modify the code:

### Running Tests

```bash
# Run tests with auto-reload during development
uv run tdd-guard-pytest

# Run tests once
uv run pytest

# Run specific test file
uv run pytest tests/test_app.py -v
```

### Development Workflow

1. Write a failing test for new functionality
2. Write minimal code to make the test pass
3. Refactor and improve the code
4. Repeat

The project includes validation functions that you can extend:

```python
# Example: Custom validation
is_valid, message = validate_csv_structure(
    df, 
    min_rows=10,                     # At least 10 rows
    required_columns=['name', 'id']  # Must have these columns
)
```

## Contributing

I'd love your help making this better! Here are some ways to contribute:

### Ideas for Contributions

- **Bug fixes**: Found something broken? Please report it or submit a fix
- **New validation rules**: Additional data quality checks
- **Performance improvements**: Better handling of large CSV files
- **UI enhancements**: Make the interface even more user-friendly
- **Documentation**: Help others understand and use the project
- **Examples**: Cool datasets or use cases to showcase

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your changes
4. Make your changes
5. Ensure tests pass (`uv run pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

Don't worry if you're new to open source - I'm happy to help guide you through the process!

## Technology Stack

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[pygwalker](https://github.com/Kanaries/pygwalker)**: Interactive data visualization
- **[pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[pytest](https://pytest.org/)**: Testing framework
- **[uv](https://docs.astral.sh/uv/)**: Fast Python package manager

## Roadmap

Some ideas I'm considering for future versions:

- Support for Excel files (.xlsx)
- Basic statistical analysis tools
- Data export functionality
- Shareable visualization links
- Simple data transformation features

## Learning Resources

If this project interests you, here are some resources that helped me build it:

- [Streamlit Documentation](https://docs.streamlit.io/)
- [pygwalker GitHub](https://github.com/Kanaries/pygwalker)
- [Test-Driven Development with Python](https://www.obeythetestinggoat.com/)
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Questions or Issues?

- Open an issue if you find a bug or have a feature request
- Start a discussion if you want to talk about the project or get help
- Feel free to reach out if you're interested in contributing

Happy data exploring!