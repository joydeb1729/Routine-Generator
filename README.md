# Academic Routine Generator

A Streamlit web application for generating academic routines based on teacher availability and course credits.

## Features

- Upload teachers and course credits data via CSV files
- Generate conflict-free academic routines
- View routine in an interactive table format
- Download routine as a beautifully formatted PDF
- Support for lab and theory courses
- Handles teacher availability constraints
- Color-coded year-wise schedule

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/routine-generator.git
cd routine-generator
```

2. Create and activate a virtual environment:
```bash
python -m venv r_env
source r_env/bin/activate  # On Windows: r_env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the displayed URL (usually http://localhost:8501)

3. Upload your CSV files:
   - Teachers.csv: Contains teacher information and availability
   - Credits.csv: Contains course credit information

4. Click "Generate Routine" to create the schedule

5. Download the generated routine as a PDF

## Input File Formats

### Teachers.csv
```csv
name,designation,rank,courses,sunday,monday,tuesday,wednesday,thursday
Dr John Doe,Professor,1,CSE101;CSE102,9_12,14_17,9_12,,14_17
```

- `name`: Teacher's full name
- `designation`: Academic position
- `rank`: Priority rank (lower number = higher priority)
- `courses`: Semicolon-separated list of course codes
- `sunday` through `thursday`: Available time slots (format: start_end)

### Credits.csv
```csv
course,credits
CSE101,3
CSE102,3
```

- `course`: Course code
- `credits`: Number of credit hours per week

## Project Structure

```
routine-generator/
├── src/
│   └── routine_generator/
│       ├── __init__.py
│       ├── utils.py
│       ├── scheduler.py
│       └── report.py
├── app.py
├── setup.py
├── requirements.txt
└── README.md
```

## License

MIT License 