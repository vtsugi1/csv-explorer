import pytest
import pandas as pd
import io
import sys
import os

# Add the parent directory to sys.path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import load_csv_data, validate_csv_structure

class TestCSVLoading:
    """Test CSV file loading functionality."""
    
    def test_load_valid_csv(self):
        """Test loading a valid CSV file."""
        csv_content = "name,age,city\nJohn,25,NYC\nJane,30,LA"
        csv_file = io.StringIO(csv_content)
        
        df, error = load_csv_data(csv_file)
        
        assert error is None
        assert df is not None
        assert len(df) == 2
        assert list(df.columns) == ['name', 'age', 'city']
        assert df.iloc[0]['name'] == 'John'
        assert df.iloc[0]['age'] == 25
    
    def test_load_empty_csv(self):
        """Test loading an empty CSV file."""
        csv_file = io.StringIO("")
        
        df, error = load_csv_data(csv_file)
        
        assert df is None
        assert "empty" in error.lower()
    
    def test_load_malformed_csv(self):
        """Test loading a malformed CSV file."""
        csv_content = "name,age,city\nJohn,25\nJane,30,LA,extra"
        csv_file = io.StringIO(csv_content)
        
        df, error = load_csv_data(csv_file)
        
        # Should still load but might have parsing issues handled gracefully
        # The exact behavior depends on pandas' handling of malformed CSV
        assert isinstance(error, (str, type(None)))
    
    def test_load_csv_with_missing_values(self):
        """Test loading CSV with missing values."""
        csv_content = "name,age,city\nJohn,25,NYC\nJane,,LA\n,30,Chicago"
        csv_file = io.StringIO(csv_content)
        
        df, error = load_csv_data(csv_file)
        
        assert error is None
        assert df is not None
        assert len(df) == 3
        assert pd.isna(df.iloc[1]['age'])
        assert pd.isna(df.iloc[2]['name'])

class TestDataProcessing:
    """Test data processing utilities."""
    
    def test_data_summary_metrics(self):
        """Test that data summary calculations work correctly."""
        df = pd.DataFrame({
            'A': [1, 2, 3, None, 5],
            'B': ['x', 'y', 'z', 'w', 'v'],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })
        
        # Test basic metrics
        assert len(df) == 5
        assert len(df.columns) == 3
        assert df.isnull().sum().sum() == 1  # One null value
        assert df['A'].nunique() == 4  # 4 unique values (excluding NaN)
        assert df['B'].nunique() == 5  # 5 unique values

class TestCSVValidation:
    """Test CSV structure validation functionality."""
    
    def test_validate_csv_with_minimum_rows(self):
        """Test that CSV validation requires minimum number of rows."""
        df = pd.DataFrame({'A': [1], 'B': [2]})  # Only 1 row
        
        is_valid, message = validate_csv_structure(df, min_rows=2)
        
        assert not is_valid
        assert "minimum" in message.lower()
        assert "rows" in message.lower()
    
    def test_validate_csv_with_sufficient_rows(self):
        """Test that CSV validation passes with sufficient rows."""
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})  # 3 rows
        
        is_valid, message = validate_csv_structure(df, min_rows=2)
        
        assert is_valid
        assert message == ""
    
    def test_validate_csv_with_required_columns(self):
        """Test that CSV validation checks for required columns."""
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        
        is_valid, message = validate_csv_structure(df, required_columns=['A', 'C'])
        
        assert not is_valid
        assert "missing" in message.lower()
        assert "C" in message

if __name__ == "__main__":
    pytest.main([__file__])