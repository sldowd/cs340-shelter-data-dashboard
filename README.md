# Animal Shelter Data Dashboard

A full-stack web application for managing and visualizing animal shelter data. Built with Python, MongoDB, and Plotly Dash to provide interactive data exploration and filtering capabilities.

## Project Overview

This application provides a comprehensive dashboard interface for animal shelter management, enabling users to:
- View and filter animal shelter outcome data
- Identify animals suitable for specific rescue training programs
- Visualize data through interactive charts and geolocation mapping
- Perform CRUD operations on the shelter database

## Tech Stack

- **Backend:** Python 3.9+, MongoDB
- **Frontend:** Plotly Dash, Dash Leaflet
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly Express, Matplotlib

## Architecture

The application follows the MVC (Model-View-Controller) design pattern:

- **Model:** MongoDB database with custom Python CRUD module
- **View:** Dash components (data tables, charts, maps)
- **Controller:** Python callback functions managing component interactions

## Features

### CRUD Operations Module
Custom Python class providing:
- **Create:** Insert new animal records into the database
- **Read:** Query and retrieve animal data with flexible filtering
- **Update:** Modify existing animal records
- **Delete:** Remove records from the database

All CRUD operations include proper error handling and return appropriate status indicators.

### Interactive Dashboard
- **Data Table:** Sortable, paginated view of all animal records
- **Filtering Options:** Radio buttons/dropdowns for rescue type filtering:
  - Water Rescue
  - Mountain/Wilderness Rescue
  - Disaster/Individual Tracking
  - Reset (unfiltered view)
- **Dynamic Charts:** Visualizations that update based on filtered data
- **Geolocation Map:** Interactive map showing animal locations in Austin, TX area

### Filter Queries
Pre-built queries for identifying animals suitable for different rescue types based on:
- Age requirements
- Breed characteristics
- Sex requirements
- Specific breed preferences per rescue type

## Project Structure

```
GraziosoSilvare/
├── venv/                              # Virtual environment
├── .env                               # Environment variables (credentials)
├── .gitignore                         # Git ignore file
├── animals.json                       # Sample data or export
├── animal_shelter.py                      # CRUD module
├── ModuleFourTestScript.ipynb         # Test script for CRUD operations
└── README.md
```

## Database Schema

MongoDB collection: `AAC.animals`

Key fields:
- `animal_id`: Unique identifier
- `animal_type`: Dog, Cat, etc.
- `breed`: Specific breed
- `name`: Animal name
- `age_upon_outcome`: Age in weeks
- `outcome_type`: Adoption, Transfer, etc.
- `sex_upon_outcome`: Sex classification
- `location_lat`: Latitude coordinate
- `location_long`: Longitude coordinate

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- MongoDB 5.0 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/sldowd/cs340-shelter-data-dashboard.git
cd cs340-shelter-data-dashboard
```

2. **Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install pymongo pandas plotly dash jupyter-dash dash-leaflet matplotlib numpy
```

4. **Import dataset into MongoDB**
```bash
mongoimport --type=csv --db=AAC --collection=animals --headerline --file=datasets/aac_shelter_outcomes.csv
```

5. **Create database user**
```javascript
// In mongosh:
use AAC
db.createUser({
  user: "aacuser",
  pwd: "SNHU1234",
  roles: [{role: "readWrite", db: "AAC"}]
})
```

6. **Configure authentication**
Update credentials in `animal_shelter.py` or use environment variables:
```python
username = os.getenv('DB_USERNAME', 'aacuser')
password = os.getenv('DB_PASSWORD', 'SNHU1234')
```

### Running the Application

**Option 1: Jupyter Notebook**
```bash
jupyter notebook ModuleFourTestScript.ipynb
```

**Future: Dashboard Application** (Project Two)
```bash
jupyter notebook ProjectTwoDashboard.ipynb
```
Run all cells to start the dashboard server.

**Option 2: Python Script** (future conversion)
```bash
python dashboard.py
```

Access the dashboard at: `http://localhost:8050`

## Usage

### Basic Operations

**Filtering Data:**
1. Select a rescue type from the filter options
2. Data table automatically updates to show matching animals
3. Charts and map refresh to display filtered results

**Viewing Animal Details:**
1. Click on any row in the data table
2. Map marker shows animal's location
3. Hover over marker for breed information
4. Click marker popup for animal name

**Resetting View:**
Select "Reset" option to return to unfiltered dataset.

## Development Status

### Completed (Project One)
- [x] MongoDB database setup and configuration
- [x] User authentication implementation
- [x] CRUD Python module with all operations
- [x] Test script for CRUD functionality

### In Progress (Project Two)
- [ ] Dashboard layout development
- [ ] Interactive filter implementation
- [ ] Query development for rescue type filtering
- [ ] Geolocation mapping functionality
- [ ] Additional chart visualization
- [ ] Data table enhancements (pagination, sorting)
- [ ] Logo and branding integration

### Planned
- [ ] Input validation and error handling
- [ ] Enhanced security features
- [ ] Performance optimization
- [ ] Unit test suite
- [ ] Deployment configuration

## Testing

### CRUD Module Tests
Located in test notebook (to be created):
```python
# Test Create
result = shelter.create(test_data)

# Test Read
results = shelter.read({"animal_type": "Dog"})

# Test Update
modified = shelter.update({"animal_id": "A123"}, {"name": "New Name"})

# Test Delete
deleted = shelter.delete({"animal_id": "TEST001"})
```

### Dashboard Testing
- Manual testing of all filter options
- Verification of data table updates
- Chart rendering validation
- Map marker accuracy checks

## Future Enhancements

- Role-based access control
- Data export functionality
- Advanced search capabilities
- Real-time data updates
- Mobile-responsive design
- Dashboard customization options

## Contributing

This is a course project for CS-340 (Client/Server Development) at Southern New Hampshire University. While this is academic work, feedback and suggestions are welcome as I continue to develop and extend this project.

## License

[To be determined]

## Contact

sarahlynnedowd@gmail.com
## Acknowledgments


- MongoDB documentation and community
- Plotly Dash documentation and examples